---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-17_re-moo-te-code-execution-in-mailcow-always-sanitize-error-messages.md
original_filename: 2024-06-17_re-moo-te-code-execution-in-mailcow-always-sanitize-error-messages.md
title: 'Re-moo-te Code Execution in Mailcow: Always Sanitize Error Messages'
category: documents
detected_topics:
- command-injection
- xss
- api-security
- sso
- path-traversal
- automation-abuse
tags:
- imported
- documents
- command-injection
- xss
- api-security
- sso
- path-traversal
- automation-abuse
language: en
raw_sha256: 03d83a75887bf44ab7f977f6e539698c46a3a4c06818a8deef91d9cac61f2bea
text_sha256: 1c50047a6ae66243e3d6cd6a0d1f132fd009eae247dfe3ebc98dacbb059234c7
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Re-moo-te Code Execution in Mailcow: Always Sanitize Error Messages

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-17_re-moo-te-code-execution-in-mailcow-always-sanitize-error-messages.md
- Source Type: markdown
- Detected Topics: command-injection, xss, api-security, sso, path-traversal, automation-abuse
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `03d83a75887bf44ab7f977f6e539698c46a3a4c06818a8deef91d9cac61f2bea`
- Text SHA256: `1c50047a6ae66243e3d6cd6a0d1f132fd009eae247dfe3ebc98dacbb059234c7`


## Content

---
title: "Re-moo-te Code Execution in Mailcow: Always Sanitize Error Messages"
page_title: "Re-moo-te Code Execution in Mailcow: Always Sanitize Error Messages | Sonar"
url: "https://www.sonarsource.com/blog/remote-code-execution-in-mailcow-always-sanitize-error-messages/"
final_url: "https://www.sonarsource.com/blog/remote-code-execution-in-mailcow-always-sanitize-error-messages/"
authors: ["Paul Gerste"]
programs: ["Mailcow"]
bugs: ["RCE", "Path traversal", "Arbitrary file overwrite", "XSS", "Security code review"]
publication_date: "2024-06-17"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 242
---

## TL;DR overview

  * Mailcow contains a remote code execution vulnerability where unsanitized error messages from external commands are reflected into shell-interpreted contexts, allowing an attacker to inject OS commands via crafted inputs that produce predictable error output.
  * The lesson: error messages, log output, and diagnostic strings are as much of an injection risk as direct user input—any external data that reaches a shell, eval(), or template render must be treated as untrusted.
  * Sanitizing error messages requires treating the error string as untrusted input regardless of its source, applying the same escaping and validation logic used for direct user input.
  * Mailcow users should apply the available patch; developers building applications that incorporate external command output into secondary operations should audit all error-handling code paths for injection risks.

Mailcow is an easy-to-use email solution that can be set up in minutes. It features SMTP, IMAP, and POP3 servers, a webmail client, an admin panel, and more. All of its components are open-source and some are written in PHP.

While scanning mailcow's code base, [SonarQube Cloud found a Path Traversal vulnerability](https://sonarcloud.io/project/issues?open=AZAH6aEtnR0c9UoLDzir&id=SonarSourceResearch_mailcow-blogpost) which looked like it could lead to Remote Code Execution. We then started investigating the code manually, confirmed the issue, and found an additional Cross-Site Scripting (XSS) flaw. Both vulnerabilities can be combined to take over a mailcow instance with a single email viewed by an admin.

In this blog post, we will cover the code intricacies that led to the vulnerabilities. We will first go over the details of the XSS vulnerability and then explore the Path Traversal flaw. We will also cover how the mailcow maintainers have tackled these issues and give advice on how to avoid such vulnerabilities in your code.

## Impact

The vulnerabilities we found and reported are tracked as [CVE-2024-31204](https://nvd.nist.gov/vuln/detail/CVE-2024-31204) (XSS) and [CVE-2024-30270](https://nvd.nist.gov/vuln/detail/CVE-2024-30270) (Path Traversal). They have been fixed in mailcow 2024-04 and seem to have existed for at least three years.

An attacker can combine both vulnerabilities to execute arbitrary code on the admin panel server of a vulnerable mailcow instance. The requirement for this is that an admin user views a malicious email while being logged into the admin panel. The victim does not have to click a link inside the email or perform any other interaction with the email itself, they only have to continue using the admin panel after viewing the email.

The following video demonstrates the flow of an attack on our test instance:

## Technical Details

The journey of these vulnerabilities begins in the code of mailcow's admin panel. It is written in PHP and has, among others, an API endpoint that is implemented in `json_api.php`. To capture API errors and show them to the user, mailcow registers a custom exception handler:

[data/web/inc/prerequisites.inc.php](https://github.com/mailcow/mailcow-dockerized/blob/2024-02/data/web/inc/prerequisites.inc.php#L147-L167):

Copy to clipboard
  
  
  function exception_handler($e) {
      if ($e instanceof PDOException) {
        // ...
      }
      else {
        $_SESSION['return'][] = array(
          'type' => 'danger',
          'log' => array(__FUNCTION__),
          'msg' => 'An unknown error occured: ' . print_r($e, true)
        );
        return false;
      }
  }
  if(!$DEV_MODE) {
    set_exception_handler('exception_handler');
  }

This handler saves exception details in the session's `return` array. From there, they are processed and passed on to the base template when the UI is rendered the next time:

[data/web/inc/footer.inc.php](https://github.com/mailcow/mailcow-dockerized/blob/2024-02/data/web/inc/footer.inc.php#L11-L24):

Copy to clipboard
  
  
  $alertbox_log_parser = alertbox_log_parser({% mark yellow %}$_SESSION{% mark %});
  $alerts = [];
  if (is_array($alertbox_log_parser)) {
    foreach ($alertbox_log_parser as $log) {
      $message = strtr($log['msg'], ["\n" => '', "\r" => '', "\t" => '<br>']);
      $alerts[trim($log['type'], '"')][] = trim($message, '"');
    }
    $alert = array_filter(array_unique($alerts));
    foreach($alert as $alert_type => $alert_msg) {
      // html breaks from mysql alerts, replace ` with '
      {% mark yellow %}$alerts[$alert_type] = implode('<hr class="alert-hr">', str_replace("`", "'", $alert_msg));{% mark %}
    }
    unset($_SESSION['return']);
  }

The base template takes them and inserts the data into JavaScript function calls inside of an inline script block:

[data/web/templates/base.twig](https://github.com/mailcow/mailcow-dockerized/blob/2024-02/data/web/templates/base.twig#L211-L213):

Copy to clipboard
  
  
  {% for alert_type, alert_msg in alerts %}
      mailcow_alert_box('{{ alert_msg|raw|e("js") }}', '{{ alert_type }}');
  {% endfor %}

  
Finally, when the page is rendered in the browser, mailcow's JavaScript renders an alert box for each error using a jQuery-based notification library:

[data/web/js/build/013-mailcow.js](https://github.com/mailcow/mailcow-dockerized/blob/2024-02/data/web/js/build/013-mailcow.js#L13-L23):

Copy to clipboard
  
  
  window.mailcow_alert_box = function({% mark yellow %}message{% mark %}, type) {
    msg = $('<span/>').text(message).text();
    if (type == 'danger' || type == 'info') {
      auto_hide = 0;
      $('#' + localStorage.getItem("add_modal")).modal('show');
      localStorage.removeItem("add_modal");
    } else {
      auto_hide = 5000;
    }
    $.notify({{% mark yellow %}message: msg{% mark %}},{z_index: 20000, delay: auto_hide, type: type,placement: {from: "bottom",align: "right"},animate: {enter: 'animated fadeInUp',exit: 'animated fadeOutDown'}});
  }

  
And the result looks like this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/463b9b35-bd11-4217-a231-55cab7f0b0d4/mailcow-error-wholepage.png)

Did you spot the vulnerability?

### CVE-2024-31204: XSS in the Admin Panel

If you guessed that an attacker could directly insert malicious JavaScript into the inline script block in the `base.twig` template, then you're wrong. It's a good idea, but Twig's escaping properly handles all characters so it's not possible to leave the string context.

The correct answer is that the jQuery-based notification library does not escape HTML entities, causing a Cross-Site Scripting (XSS) vulnerability when attackers can control an exception that is being raised. This is given away by the fact that there were raw `<hr>` elements added in `footer.inc.php`.

But is this just a functional bug, or an exploitable security vulnerability? Can an attacker control the content of an exception and inject a malicious JavaScript payload? The answer is yes! Let's see how that can happen.

Since the exception handler uses `print_r()` to convert the exception to a string, we can see that not only the error's location and error message are included, but also the arguments to functions in the call stack! This happens because the [`zend.exception_ignore_args`](https://www.php.net/manual/en/ini.core.php#ini.zend.exception-ignore-args) configuration directive is set to _Off_ in mailcow's PHP container, which inherits the setting from the official PHP-FPM Docker image. The resulting string representation looks like this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/88da3c3f-30fc-45b8-8904-ce206623a5f6/mailcow-error-closeup.png)

### Controlled Arguments

There are plenty of locations where an attacker can control arguments to functions, so now all they need is a function that reliably errors on a certain input. One great example is `explode()` which is used very early in the API handler script:

[data/web/json_api.php](https://github.com/mailcow/mailcow-dockerized/blob/2024-02/data/web/json_api.php#L50-L56):

Copy to clipboard
  
  
  if (isset($_GET['query'])) {
    $query = {% mark %}explode('/', $_GET['query']){% mark %};
    $action =     (isset($query[0])) ? $query[0] : null;
    $category =   (isset($query[1])) ? $query[1] : null;
    $object =     (isset($query[2])) ? $query[2] : null;
    $extra =      (isset($query[3])) ? $query[3] : null;
    // ...
  }

The `explode()` function expects two strings, and the second one is provided from a query parameter (`$_GET['query']`). So when does this function error? If it receives an argument with the wrong type!

Since PHP performs ["extended" query parameter parsing](https://stackoverflow.com/a/9547490), it is possible to make `$_GET['query']` an array: `json_api.php?query[]=<script>alert(1)</script>`

In such a case, the output of `print_r($exception)` will look like this:

Copy to clipboard
  
  
  An unknown error occured: TypeError Object(
     [message:protected] => explode(): Argument #($string) must be of type string, array given
      [string:Error:private] => 
      [code:protected] => 0
      [file:protected] => /web/json_api.php
      [line:protected] => 52
      [trace:Error:private] => Array(
          [0] => Array(
              [file] => /web/json_api.php
              [line] => 52
              [function] => explode
              [args] => Array(
                  [0] => /
                  [1] => Array(
                      [0] => <script>alert(1)<script>
                  )
              )
          )
      )
      [previous:Error:private] =>
  )

  
As we can see, the attacker-controlled string from the `query` parameter is included as-is and will be rendered in the victim's session the next time they load a page.

But how can the attacker control this query parameter in a victim's session? If they just send the link, the victim might get suspicious by the weird API response, or not even click. A more convenient way for the attacker is to do it via email! Since mailcow comes with a webmail client, this is an interesting option.

### A Malicious Email

The admin panel and the webmail client live under different paths on the same host (`/` and `/SOGo/` respectively). This means that they share all the cookies but also that many web isolation mechanisms, such as CORS or cookie SameSite attributes, no longer apply.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/7b133f4b-bb20-456d-a04d-c4ab4297a7af/mailcow-same-origin.png)

An attacker can craft an HTML email that contains a CSS background image which is loaded from a remote URL. When that URL points to the API endpoint, it can contain an XSS payload in the `query` parameter:

Copy to clipboard
  
  
  <div id=a>
    <a href="https://mail.mailcow.example/debug">Read important admin message here.</a>
  </div>
  <style>
    #a { background: url("/json_api.php?{% mark yellow %}query[]{% mark %}={% mark red %}%3Cscript%3Ealert(1)%3C%2Fscript%3E{% mark %}') }
  </style>

Normally, mailcow and other email clients try to block resources loaded from remote sources by default. Since the background image URL is relative (it points to a resource on the same host), mailcow's webmail client, [SOGo](https://github.com/Alinto/sogo), does not prevent it from being loaded. This causes the browser to make the malicious request immediately upon opening the email:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/8da54a93-05f2-49fb-b1a9-1552e2be1923/mailcow-img-request.png)

After that, the victim's session is poisoned with the XSS payload which will be rendered and executed the next time the victim visits the admin panel. With this, the attacker could already control basically the whole mailcow instance by changing configurations, setting passwords, and so on. But is this the final impact?

### CVE-2024-30270: Arbitrary File Overwrite, detected by SonarQube Cloud

While scanning mailcow's codebase with SonarQube Cloud, we found another vulnerability that would lead to the execution of arbitrary commands on the server. You can open the issue [here](https://sonarcloud.io/project/issues?impactSoftwareQualities=SECURITY&resolved=false&id=SonarSourceResearch_mailcow-blogpost&open=AZAH6aEtnR0c9UoLDzir) to follow along with the blog post (no account required):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/2deff93e-ed25-4713-895e-45bba4a44e79/sc-issue-item.png)

The corresponding code looks like this:

Copy to clipboard
  
  
  function rspamd_maps($_action, $_data = null) {
    // ...
    switch ($_action) {
      case 'edit':
        // ...
        $maps = (array)$_data['map'];
        foreach ($maps as $map) {
          foreach ($RSPAMD_MAPS as $rspamd_map_type) {
            if (!in_array($map, $rspamd_map_type)) { // {% mark yellow %}[1]{% mark %}
              $_SESSION['return'][] = array(
                'type' => 'danger',
                'log' => array(__FUNCTION__, $_action, '-'),
                'msg' => array('global_map_invalid', $map)
              );
              continue; // {% mark yellow %}[2]{% mark %}
            }
          }
          try {
            if (file_exists('/rspamd_custom_maps/' . $map)) { // {% mark yellow %}[3]{% mark %}
              $map_content = trim($_data['rspamd_map_data']);
              $map_handle = fopen('/rspamd_custom_maps/' . $map, 'w'); // {% mark yellow %}[4]{% mark %}
              // ...
              fwrite($map_handle, $map_content . PHP_EOL); // {% mark yellow %}[5]{% mark %}
              fclose($map_handle);
              // ...
            }
          }
     // ...
  }

User input is passed to the `rspamd_maps` function via the `$_data` parameter. At `[1]`, the extracted `$map` value is checked to be part of a predefined list of map types. However, at `[2]`, the loop is not aborted but continues when an invalid value is encountered. This makes the validation logic obsolete, allowing an attacker to pass any value into `$map`.

This untrusted value is then used to construct a file path, where an attacker could insert a relative path traversal payload, such as `../etc/passwd`. This path is first used to check if the resulting file exists at `[3]`. This prevents an attacker from creating arbitrary files and limits the impact of this vulnerability to file **over** writes instead of arbitrary file writes. Subsequently, at `[4]`, a file handle is created from the untrusted path. Finally, at `[5]`, the value of `$map_content` is written to the file, which is also entirely attacker-controlled as it comes from the `$_data` parameter.

Since the admin panel is a PHP application, a straightforward way of exploiting such a file write vulnerability would be to find a suitable PHP file, overwrite it with malicious PHP code, and finally send a request to execute the malicious code.

However, the mailcow maintainers did a good job setting all file permissions to read-only inside their Dockerfile! This shows how important defense-in-depth is, as it can make the attacker's life much harder.

### Writable Template Cache

In the case of mailcow, there was one location left that could not be write-protected: the cache directory of mailcow's templating engine, [Twig](https://twig.symfony.com/). Twig will compile a template to a PHP file when it is first used. After that, the PHP file is executed to render the template because it's much faster than interpreting the template every time it is used. This is how a template looks in its original form vs. its compiled form:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/403d8f87-562c-409a-942d-9bb18971311f/twig-template-comparison-small.png)

However, that also means the PHP app itself has to be able to write PHP files in that cache directory. The attacker can take advantage of this by simply overwriting an already compiled template with their malicious code. The filenames of these files look quite random and unpredictable, but they are [entirely based on the content of the raw, original template file](https://github.com/twigphp/Twig/blob/b46e93c/src/Cache/FilesystemCache.php#L32-L37), so they are always the same per template file on all instances that run the same version of mailcow.

To trigger the execution of the overwritten file, the attacker just has to request the respective page on the admin panel that uses the template.

After that, the attacker would usually deploy a standard PHP web shell to move deeper into the target system. However, the mailcow team applied defense-in-depth again with a robust PHP config: They disabled many of the classic ways of executing OS commands from PHP, such as `system()` or `passthru()`, using the [disable_functions](https://www.php.net/manual/en/ini.core.php#ini.disable-functions) config directive.

But they did not disable one function that is known to bypass these restrictions, which is, fittingly, the `mail()` function. [This blog post of ours](https://www.sonarsource.com/blog/why-mail-is-dangerous-in-php/) explains more about the dangers of this function and how attackers could use it to bypass `disable_functions`.

With all these tricks in their toolbelt, the attacker can now craft an email containing multiple stages of payloads that will eventually execute malicious OS commands on the admin panel's server. Luckily, all parts of mailcow run in separate Docker containers, so the attacker cannot easily escape and compromise the whole host system.

### Patch

To fix the XSS vulnerability (CVE-2024-31204), the mailcow maintainers chose the straight-forward way of encoding all HTML special characters in the exception details before passing them to the template:

Copy to clipboard
  
  
  $alerts = [];
   if (is_array($alertbox_log_parser)) {
     foreach ($alertbox_log_parser as $log) {
  -    $message = strtr($log['msg'], ["\n" => '', "\r" => '', "\t" => '<br>']);
  +    $message = htmlspecialchars($log['msg'], ENT_QUOTES);
  +    $message = strtr($message, ["\n" => '', "\r" => '', "\t" => '<br>']);
       $alerts[trim($log['type'], '"')][] = trim($message, '"');
     }
     $alert = array_filter(array_unique($alerts));

For the file write vulnerability (CVE-2024-30270), the mailcow team opted for fixing the validation logic that was already present. This is a good idea, since the check now properly enforces the allowlist of permitted map types, making the check robust:

Copy to clipboard
  
  
          return false;
         }
         $maps = (array)$_data['map'];
  +      $valid_maps = array();
         foreach ($maps as $map) {
           foreach ($RSPAMD_MAPS as $rspamd_map_type) {
             if (!in_array($map, $rspamd_map_type)) {
                 'log' => array(__FUNCTION__, $_action, '-'),
                 'msg' => array('global_map_invalid', $map)
               );
  -            continue;
  +          } else {
  +            array_push($valid_maps, $map);
             }
           }
  +      }
  +      foreach ($valid_maps as $map) {
           try {
             if (file_exists('/rspamd_custom_maps/' . $map)) {
               $map_content = trim($_data['rspamd_map_data']);

The mailcow maintainers did not stop there but also implemented additional hardening measures to avoid similar exploits in the future! This is a great idea and at the same time not surprising as we've previously seen in their code that they are fans of defense-in-depth, just like us.

To avoid `GET` requests coming from the webmail client to cause API requests, they are now checking special browser headers to determine if the request was intended for the API. First, they opted for the `Referer` header:

Copy to clipboard
  
  
  +// deny requests from /SOGo locations
  +if (isset($_SERVER['HTTP_REFERER'])) {
  +  if (strpos(strtolower($_SERVER['HTTP_REFERER']), '/sogo') !== false) {
  +    header('HTTP/1.1 403 Forbidden');
  +    exit;
  +  }
  +}
  +
   if (isset($_GET['query'])) {
     $query = explode('/', $_GET['query']);

However, an attacker could prevent this header from being sent at all, for example by setting the `referrerpolicy` attribute to `no-referrer` on an image tag. That's why they now use the [Sec-Fetch-Dest header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Dest) that the browser uses to signal where the response of a request will be used. In this case, API requests should always originate from `fetch()` calls, so the server can safely ignore calls that indicate something else:

Copy to clipboard
  
  
  -// deny requests from /SOGo locations
  -if (isset($_SERVER['HTTP_REFERER'])) {
  -  if (strpos(strtolower($_SERVER['HTTP_REFERER']), '/sogo') !== false) {
  -    header('HTTP/1.1 403 Forbidden');
  -    exit;
  -  }
  +// Block requests not intended for direct API use by checking the 'Sec-Fetch-Dest' header.
  +if (isset($_SERVER['HTTP_SEC_FETCH_DEST']) && $_SERVER['HTTP_SEC_FETCH_DEST'] !== 'empty') {
  +  header('HTTP/1.1 403 Forbidden');
  +  exit;
   }
   
   if (isset($_GET['query'])) {

## Timeline

**Date**| **Action**  
---|---  
2024-03-22| We report all issues to the mailcow maintainers  
2024-04-02| The maintainers confirm the issues and propose fixes  
2024-04-03| We suggest minor changes to the fixes  
2024-04-04| The maintainers release [version 2024-04](https://mailcow.email/posts/2024/release-2024-04/), containing the fixes  
  
## Summary

In this blog post, we covered two vulnerabilities in mailcow, an easy-to-use mail server solution. We showed that attackers can combine the XSS and Path Traversal vulnerabilities to execute arbitrary code on vulnerable mailcow instances. We also discussed how emails are a tool used by attackers to deliver malicious payloads to their victims.

We also discussed how such vulnerabilities can be avoided, and showed the importance of security-in-depth. SonarQube Cloud can help keep your code base clean and flag vulnerabilities like mailcow's Path Traversal before they reach production.

Finally, kudos to the mailcow team for their fast fixes and their friendly communication!

## Related Blog Posts

  * [Why mail() is dangerous in PHP](https://www.sonarsource.com/blog/why-mail-is-dangerous-in-php/)
  * [Reply to calc: The Attack Chain to Compromise Mailspring ](https://www.sonarsource.com/blog/reply-to-calc-the-attack-chain-to-compromise-mailspring/)
  * [Joomla: PHP Bug Introduces Multiple XSS Vulnerabilities](https://www.sonarsource.com/blog/joomla-multiple-xss-vulnerabilities/)
  * [Pitfalls of Desanitization: Leaking Customer Data from osTicket](https://www.sonarsource.com/blog/pitfalls-of-desanitization-leaking-customer-data-from-osticket/)
