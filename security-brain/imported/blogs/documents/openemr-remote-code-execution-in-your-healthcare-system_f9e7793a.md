---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-26_openemr-remote-code-execution-in-your-healthcare-system.md
original_filename: 2023-01-26_openemr-remote-code-execution-in-your-healthcare-system.md
title: OpenEMR - Remote Code Execution in your Healthcare System
category: documents
detected_topics:
- xss
- path-traversal
- command-injection
- supply-chain
- sqli
- file-upload
tags:
- imported
- documents
- xss
- path-traversal
- command-injection
- supply-chain
- sqli
- file-upload
language: en
raw_sha256: f9e7793a6ef8e9aaac3030abbacbe76b7368128d5aa440b39f25f423b9bbf6a3
text_sha256: 8b7535930ab03d0785215b955431ec70f513202e8f98e5648d0782a21a4ef6d5
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# OpenEMR - Remote Code Execution in your Healthcare System

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-26_openemr-remote-code-execution-in-your-healthcare-system.md
- Source Type: markdown
- Detected Topics: xss, path-traversal, command-injection, supply-chain, sqli, file-upload
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `f9e7793a6ef8e9aaac3030abbacbe76b7368128d5aa440b39f25f423b9bbf6a3`
- Text SHA256: `8b7535930ab03d0785215b955431ec70f513202e8f98e5648d0782a21a4ef6d5`


## Content

---
title: "OpenEMR - Remote Code Execution in your Healthcare System"
page_title: "OpenEMR - Remote Code Execution in your Healthcare System | Sonar"
url: "https://www.sonarsource.com/blog/openemr-remote-code-execution-in-your-healthcare-system/"
final_url: "https://www.sonarsource.com/blog/openemr-remote-code-execution-in-your-healthcare-system/"
authors: ["Dennis Brinkrolf (@DBrinkrolf)"]
programs: ["OpenEMR"]
bugs: ["RCE", "XSS", "LFI", "Arbitrary file read", "Security code review"]
publication_date: "2023-01-26"
added_date: "2023-01-31"
source: "pentester.land/writeups.json"
original_index: 1623
---

## TL;DR overview

  * Sonar's research identified a remote code execution vulnerability in OpenEMR—one of the most widely deployed open source electronic health record systems—enabling attackers to compromise healthcare servers and access patient data.
  * The vulnerability leverages an insecure PHP code path where user-controlled input reaches an execution function without proper sanitization, a classic injection flaw that automated static analysis is designed to catch.
  * OpenEMR's widespread adoption in clinics and hospitals makes this a high-impact supply chain risk: organizations running unpatched versions expose patient records and may face significant regulatory consequences under HIPAA.
  * Healthcare IT teams should verify they are running patched OpenEMR versions and implement SonarQube scanning for any self-developed or customized healthcare software.

OpenEMR is the most popular open-source software for electronic health records and medical practice management. It is used worldwide to manage sensitive patient data, including information about medications, laboratory values, and diseases. Patients use OpenEMR to schedule appointments, communicate with physicians, and pay online invoices. Specifically, in these tumultuous times of an ongoing pandemic, this is highly sensitive data, and protecting it is a concern for everyone. 

During our security research of popular web applications, we discovered several code vulnerabilities in OpenEMR. A combination of these vulnerabilities allows remote attackers to execute arbitrary system commands on any OpenEMR server and to steal sensitive patient data. In the worst case, they can compromise the entire critical infrastructure.

Our SAST engine discovered two code vulnerabilities that, in combination, led to unauthenticated remote code execution. This blog post analyzes the technical causes of the vulnerabilities, their impact, and how you can prevent them in your code. 

## Impact

We discovered the following vulnerabilities in OpenEMR:

  * Unauthenticated File Read 
  * Authenticated Local File Inclusion
  * Authenticated Reflected XSS

An unauthenticated, remote attacker can chain these vulnerabilities to gain code execution on a server running OpenEMR version lower than 7.0.0.

We reported all issues responsibly to the OpenEMR maintainers, who immediately released a [patch](https://www.open-emr.org/wiki/index.php/OpenEMR_Patches#7.0.0_Patch_.2811.2F30.2F22.29) to version 7.0.0 to protect all users.

## Technical Details

In this section, we dive deep into the technical details of three vulnerabilities. First, we show how a rogue MySQL server can read arbitrary files from an OpenEMR instance. Then we discuss two other vulnerabilities and show how their combination allows unauthenticated, remote code execution.

### Unauthenticated Arbitrary File Read

In OpenEMR, the installer does not delete itself after a successful installation. Furthermore, the setup is divided into several steps, and an unauthenticated user can perform some of these via the user-controlled parameter `$state`**.**

A complete reinstallation is impossible, but attackers can specify a configuration during the setup steps by setting the properties of the `Installer` class (`$_REQUEST`). Afterward, the method `displayNewThemeDiv` is called:

**setup.php**

Copy to clipboard
  
  
  <?php
  // ...
  $state = isset($_POST["state"]) ? ($_POST["state"]) : '';
  $installer = new Installer($_REQUEST);
  // ...
  if ($state == 7) {
  // ...
  $installer->displayNewThemeDiv();

The `displayNewThemeDiv` method invokes the `getCurrentTheme` method. During this call, a MySQL query is executed, which reads the current theme from the database. Since no database connection is established yet, a new one is created with the attacker-controlled properties set via the `Installer` constructor:

**library/classes/Installer.class.php**

Copy to clipboard
  
  
  <?php
  // ...
  class Installer
  {
  public function __construct($cgi_variables)
  {
  $this->server = $cgi_variables['server'];
  $this->port = $cgi_variables['port'];
  $this->login = $cgi_variables['login'];
  $this->pass = $cgi_variables['pass'];
  $this->dbname = $cgi_variables['dbname'];
  // ...
  }
  // ...
  
  private function connect_to_database($server, $user, $password, $port, $dbname = '')
  {
  $ok = mysqli_real_connect($mysqli, $server, $user, $password, $dbname,  $port);
  // ...
  }
  
  public function user_database_connection()
  {
  $this->dbh = $this->connect_to_database($this->server, $this->login, $this->pass, $this->port, $this->dbname);
  // ...
  }
  // ...
  
  public function getCurrentTheme()
  {
  $current_theme =  $this->execute_sql("SELECT gl_value FROM globals WHERE gl_name LIKE '%css_header%'");
  // ...
  }

To conclude, an unauthenticated attacker can perform a database query on their own server. But how does that lead to an arbitrary file read?

The MySQL statement `LOAD DATA` can be used to load the contents of a file into a database table. If the modifier `LOCAL` is given, the file is read from the client instead of the server. The MySQL packets exchanged during this command look like this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/3fa38690-5701-4cbe-88e3-12facbffec3b/OpenEMR%20graphics.png)

As the image shows, the server actively requests the contents of the specified file. A malicious server can request the content of another file, even in response to a totally different query from the client.

Since this feature is insecure, it has been disabled by default for the PHP MySQL client. However, OpenEMR uses the `LOAD DATA` statements to load, e.g., definitions of diseases, into the database. For this reason, it is expected that the directive `mysqli.allow_local_infile=On` is set via `php.ini`.

In other words, if OpenEMR is set up correctly, an unauthenticated attacker can read files like certificates, passwords, tokens, and backups from an OpenEMR instance via a rogue MySQL server.

### Unauthenticated Remote Code Execution using an Exploit Chain

This section demonstrates how we can achieve unauthenticated remote code execution using two different vulnerabilities discovered by our SAST engine. As an entry point, a reflected Cross-Site-Scripting (XSS) is used to execute arbitrary JavaScript in the victim's browser. Since an attacker can issue requests on behalf of the victim, they have the same privileges as the victim. As a first step, the attacker can upload a PHP file. However, the uploaded PHP file is located in a folder where a `.htaccess` file blocks direct access, preventing the PHP file from being executed. Therefore, a second vulnerability, which allows attackers to include local files (LFI), is used to achieve remote code execution.

Let's take a look at the root cause of the reflected XSS. The attacker-controlled `REQUEST_URI` is passed as a string to the JavaScript function `dopopup`. Furthermore, the `dopopup` function is the target of the `onclick` event handler inside the HTML `<a>` Tag. The event handlers in the browser have a unique behavior that we will discuss briefly, but first, we need to look at the `REQUEST_URI`:

**interface/forms/eye_mag/php/eye_mag_functions.php**

Copy to clipboard
  
  
  <a onclick="dopopup('<?php echo $_SERVER['REQUEST_URI'] . '&display=fullscreen&encounter=' . $encounter; ?>');"
  href="JavaScript:void(0);"></a>

[**XSS: Try it by yourself on SonarQube Cloud!**](https://sonarcloud.io/project/issues?resolved=false&sonarsourceSecurity=xss&types=VULNERABILITY&id=SonarSourceResearch_openemr-blogpost&open=AYXtQ1qyDgoxwr2lUbaj)

The user-controlled input `REQUEST_URI` contains the entire URI that the browser uses to request the PHP file. In all modern browsers, single and double quotes are URL-encoded inside an HTTP query string. That's why an attacker can't easily break out a quoted context. However, this is where an attacker can take advantage of the unique behavior of event handlers in the browser.

A browser has different orders of how each component is rendered. In our case, the HTML is rendered first, followed by the JavaScript context. As a result, HTML entities can be used within an event handler since the browser decodes them. An `&apos;` thus becomes a single quote. Note that the two characters needed to represent an HTML entity: `&` and `;` are not URL-encoded by the browser. 

In the following table, the individual steps are shown. The first column of the table represents the request by the browser, while the second column shows the HTTP response. In the third step, the browser "normalizes" the HTML entity `&apos;` leading to a reflected XSS. 

**1\. Request URI**| **2\. HTTP Response**| **3\. Browser rendering**  
---|---|---  
index.php?a=1&apos;);alert(1);//| < a onlick=”dopopup(‘/index.php?a=1&apos;);alert(1);// ’)”>| < a onlick=”dopopup(‘/index.php?a=1’);alert(1);// ’)”>  
  
The second vulnerability is a straightforward Local File Inclusion (LFI) vulnerability. As the following code snippet shows, the user-controlled variable `$formname` is concatenated to a path. If the file exists, it is included:

**interface/forms/LBF/new.php**

Copy to clipboard
  
  
  <?php
  // ...
  $formname = isset($_GET['formname']) ? $_GET['formname'] : '';
  // ...
  if (!$from_trend_form) {
  $fname = $GLOBALS['OE_SITE_DIR'] . "/LBF/$formname.plugin.php";
  if (file_exists($fname)) {
  include_once($fname);
  }
  }

[**LFI: Try it by yourself on SonarQube Cloud!**](https://sonarcloud.io/project/issues?resolved=false&sonarsourceSecurity=file-manipulation&id=SonarSourceResearch_openemr-blogpost&open=AYXtQ1vlDgoxwr2lUbcp)

Since the user-controlled variable `$formname` is not sanitized, an attacker can select other folders on the server via a path traversal payload like `a/LBF/../../var/www/`. However, the filename is restricted to files with the suffix `.plugin.php`. 

In order to upload such a file, an attacker can leverage the file upload functionality shown in the following code snippet. The name of uploaded files is composed of the PHP function `time` and the attacker-controlled name of the uploaded file `$_FILES['uploaded']['name']`. Since there is no file extension check, files with the suffix `.plugin.php` can be uploaded. Note that the `time` function returns the current Unix timestamp and provides no security:

**interface/billing/edi_271.php**

Copy to clipboard
  
  
  <?php
  // ...
  if (isset($_FILES) && !empty($_FILES)) {
  $target = time() . basename($_FILES['uploaded']['name']);
  // ...
  $file_moved = move_uploaded_file($_FILES['uploaded']['tmp_name'], $target);
  // ...
  }
  

In summary, an attacker can use the reflected XSS, upload a PHP file named `payload.plugin.php` and then use the path traversal via the Local File Inclusion to execute the PHP file. It takes a few tries to figure out the appropriate Unix timestamp but eventually leads to remote code execution.

## Patch

The OpenEMR maintainers addressed all vulnerabilities and hardened the application further:

  * A combination of sessions and CSRF checks are used to patch the arbitrary file read vulnerability and to restrict the installation process more. An unauthenticated attacker must go through the installation steps in the correct order. When a config file already exists in an installed OpenEMR instance, the setup process fails in the first step. In the future, it is planned to remove the need for `mysqli.allow_local_infile=On` ([0ea6e580](https://github.com/openemr/openemr/commit/0ea6e5802566fbd6cf1c7a4f279654f34a7f9d36)).
  * The function `attr_js,` which calls the PHP function `htmlspecialchars` encodes the important character `&` for an HTML entity into an entity. As a result, escaping the context is no longer possible, which prevents the XSS vulnerability ([4b915404](https://github.com/openemr/openemr/commit/4b915404cc7bfd4f4e90d1f34fbf74cff5c143a3)).
  * To prevent the Local File Inclusion vulnerability, the user-controlled parameter is sanitized by a regex, allowing only alphanumeric chars, to prevent path traversal. The file upload feature now checks for PHP extensions ([10b3cb3b](https://github.com/openemr/openemr/commit/10b3cb3bccfb21db8a79c959c9ba968012133064)).

OpenEMR cannot always guarantee that the setup process will completely delete the installation files. If you develop an application with a built-in setup flow, you must decide whether you deliberately keep them (in the case of OpenEMR) or try to delete them. In any case, you should always check if the application is already installed first. If so, the execution should be terminated as soon as possible. Moreover, always try to sanitize every user input and apply the respective sanitizer in the specific context.

## Timeline

**Date**| **Action**  
---|---  
2022-10-24| We report all issues to the vendor.  
2022-10-30| Vendor confirms the issues and sends us patches.  
2022-11-30| Vendor releases version 7.0.0.  
  
## Summary

In this blog post, we analyzed three code vulnerabilities found in OpenEMR, the most popular open-source software for electronic health records and medical practice management.

We outlined how an attacker-controlled MySQL configuration could lead to an arbitrary file read. We also demonstrated how combining two code vulnerabilities, Cross-Site Scripting, and Local File Inclusion both detected by our SAST engine, can lead to a takeover of any OpenEMR instance. Furthermore, we discussed the patches and showed how to prevent such issues in your PHP code.

If you are using OpenEMR, we strongly recommend updating to the fixed versions mentioned above. Finally, we want to thank the OpenEMR team for their professional and fast responses and patches!

## Related Blog Posts

  * [Code vulnerabilities put health records at risk](https://www.sonarsource.com/blog/openemr-5-0-2-1-command-injection-vulnerability/)
  * [Pandora FMS 742: Critical Code Vulnerabilities Explained](https://www.sonarsource.com/blog/pandora-fms-742-critical-code-vulnerabilities-explained/)
  * [Remote Code Execution in Melis Platform](https://www.sonarsource.com/blog/remote-code-execution-in-melis-platform/)
