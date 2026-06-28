---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-15_checkmk-remote-code-execution-by-chaining-multiple-bugs-33.md
original_filename: 2022-11-15_checkmk-remote-code-execution-by-chaining-multiple-bugs-33.md
title: 'Checkmk: Remote Code Execution by Chaining Multiple Bugs (3/3)'
category: documents
detected_topics:
- command-injection
- password-reset
- automation-abuse
- ssrf
- path-traversal
- otp
tags:
- imported
- documents
- command-injection
- password-reset
- automation-abuse
- ssrf
- path-traversal
- otp
language: en
raw_sha256: 196c12ad8996c155abea4ba8c58739907288f9973f337660a3619de34293f0f0
text_sha256: 76dfdb675024b451a7c08ccc8af245201857270a0d8da674220a838464773b81
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: true
---

# Checkmk: Remote Code Execution by Chaining Multiple Bugs (3/3)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-15_checkmk-remote-code-execution-by-chaining-multiple-bugs-33.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, automation-abuse, ssrf, path-traversal, otp
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: True
- Raw SHA256: `196c12ad8996c155abea4ba8c58739907288f9973f337660a3619de34293f0f0`
- Text SHA256: `76dfdb675024b451a7c08ccc8af245201857270a0d8da674220a838464773b81`


## Content

---
title: "Checkmk: Remote Code Execution by Chaining Multiple Bugs (3/3)"
page_title: "Checkmk: Remote Code Execution by Chaining Multiple Bugs (3/3) | Sonar"
url: "https://blog.sonarsource.com/checkmk-rce-chain-3/"
final_url: "https://www.sonarsource.com/blog/checkmk-rce-chain-3/"
authors: ["Stefan Schiller (@scryh_)"]
programs: ["Checkmk"]
bugs: ["RCE", "Code injection", "SSRF", "Line Feed injection", "Arbitrary file read", "Authentication bypass", "Security code review"]
publication_date: "2022-11-15"
added_date: "2022-11-17"
source: "pentester.land/writeups.json"
original_index: 1912
---

## TL;DR overview

  * The final part of Sonar's Checkmk research presents the complete end-to-end exploit chain, demonstrating unauthenticated remote code execution against a default Checkmk Server installation.
  * The chain begins with an authentication bypass, progresses through a logic flaw to gain elevated API access, and terminates in a command injection that achieves OS-level code execution.
  * The responsible disclosure resulted in Checkmk releasing patches for all identified issues; organizations should update immediately to close the attack surface.
  * This research reinforces the importance of static analysis and security code review in infrastructure monitoring tools, where the combination of network exposure and privileged access creates outsized risk.

This is the third and last article in the _Checkmk - Remote Code Execution by Chaining Multiple Bugs_ series ([first article](https://blog.sonarsource.com/checkmk-rce-chain-1/), [second article](https://blog.sonarsource.com/checkmk-rce-chain-2/)). Within the series of articles, we take a detailed look at multiple vulnerabilities we identified in Checkmk and its NagVis integration, which can be chained together by an unauthenticated, remote attacker to fully take over the server running a vulnerable version of Checkmk.

In the last article, we evaluated the ability of an attacker to forge arbitrary LQL queries. This allows the attacker to exfiltrate monitoring data and issue external Nagios commands, which can be leveraged to delete arbitrary files. We could demonstrate that this ability could be combined with a file race condition to bypass the authentication of the NagVis component. 

In this third and last article, we complete our deep dive into the technical details of the vulnerability chain. At this point, the attacker has gained access to the NagVis component. Based on this, we will outline how the attacker can escalate this access to the Checkmk GUI itself by exploiting an authenticated file read vulnerability in NagVis.

At last, we take a detailed look at an authenticated code injection vulnerability in Checkmk, which forms the final step to remote code execution.

## Technical Details

We start this section by briefly recapping the vulnerabilities and exploitation chain. After this, we look at the arbitrary file read vulnerability in NagVis and the code injection vulnerability in Checkmk.

### Exploitation Chain

As a reminder, the following picture summarizes the exploitation chain enabling an unauthenticated attacker to gain remote code execution:

![Checkmk-Remote Code Execution](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/58c9af12-5aba-4ba4-8b00-5d6c57d23180/Checkmk-Remote%20Code%20Execution_1.png)

In the last two articles, we covered the first two vulnerabilities (1, 2) and an arbitrary file deletion, which can be exploited by an unauthenticated attacker to gain access to the NagVis component. Within this article, we determine how an attacker can escalate to the Checkmk automation user by exploiting an authenticated arbitrary file read in NagVis (3). With access to the Checkmk automation user, an attacker can ultimately gain code execution by exploiting a code injection vulnerability in Checkmk’s watolib (4):

![Checkmk-Remote Code Execution diagram](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/3c94a175-19b0-4b4b-b7a2-0079e07542ba/Checkmk-Remote%20Code%20Execution_2.png)

### Arbitrary File Read in NagVis (CVE-2022-46945)

After an attacker has gained access to NagVis, the exposed attack surface is greatly increased because authenticated endpoints can now be accessed. For one of these endpoints, our automatic scan with [SonarQube Cloud](https://sonarcloud.io/) discovered an interesting path injection vulnerability:

[Try it by yourself in SonarQube Cloud!](https://sonarcloud.io/project/issues?issues=AYRRCmHFmKnN7I1rUBls&open=AYRRCmHFmKnN7I1rUBls&id=SonarSourceResearch_checkmk-blogpost)

The endpoint is implemented in the `CoreModGeneral` class. This class offers different actions which an authenticated user can trigger. One of these actions is called `getHoverUrl`:

**share/nagvis/htdocs/server/core/classes/CoreModGeneral.php**

Copy to clipboard
  
  
  class CoreModGeneral extends CoreModule {
  ...
  public function handleAction() {
  $sReturn = '';
  
  if($this->offersAction($this->sAction)) {
  switch($this->sAction) {
  ...
  case 'getHoverUrl':
  $sReturn = $this->getHoverUrl();
  break;
  ...

Within the `getHoverUrl` method, `getCustomOptions` is called to retrieve user-provided GET and POST parameters. In this case, the parameter `url` is retrieved, which is supposed to be an array containing URLs. For each provided URL, a new `NagVisHoverUrl` object is created. The response, which is stored in `$arrReturn`, contains the requested URL (`url`) as well as the string representation of the `NagVisHoverUrl` object (`code`):

**share/nagvis/htdocs/server/core/classes/CoreModGeneral.php**

Copy to clipboard
  
  
  private function getHoverUrl() {
  $arrReturn = Array();
  
  // Parse view specific uri params
  $aOpts = $this->getCustomOptions(Array('url' => MATCH_STRING_URL));
  
  foreach($aOpts['url'] AS $sUrl) {
  $OBJ = new NagVisHoverUrl($this->CORE, $sUrl);
  $arrReturn[] = Array('url' => $sUrl, 'code' => $OBJ->__toString());
  }
  
  $result = json_encode($arrReturn);
  ...
  return $result;
  }

Within the constructor of the `NagVisHoverUrl` class, the method `readHoverUrl` is called.

This method uses `file_get_contents` to retrieve the requested URL:

**share/nagvis/htdocs/server/core/classes/NagVisHoverUrl.php**

Copy to clipboard
  
  
  private function readHoverUrl() {
  ...
  if(!$content = file_get_contents($this->url)) {
  throw new NagVisException(l('couldNotGetHoverUrl', Array('URL' => $this->url)));
  }
  ...
  $this->code = $content;
  }

Since an authenticated user can fully control the URLs provided, the `getHoverUrl` action can be used to read arbitrary files by using the `file:///` scheme.

This vulnerability further increases the attacker’s ability to read arbitrary files accessible by the webserver user. The impact depends on the presence of accessible files with sensitive content. Unfortunately, for automation users, these files exist.

### Checkmk Automation Users

Checkmk provides two types of user accounts: normal users and automation users. A normal user has a regular password and can log in to the GUI. An automation user can be used as a convenient way to automate certain activities that would normally be done via the GUI. Instead of a regular password, an automation user is authenticated by an _automation secret_. This secret can usually not be used to log in to the GUI but is provided as an additional GET parameter to the accessed endpoint.

The default automation user is called `automation` and is preconfigured with a random secret. The hash of this secret and the hash of regular passwords are by default stored in an `htpasswd` file:

Though, the secret is additionally stored in a plaintext file, which is called `automation.secret`:

Since the file contains the plaintext secret, the aforementioned arbitrary file read vulnerability can be leveraged by an attacker to retrieve it without requiring to crack the hash stored in the `htpasswd` file.

Although this secret can be used to access authenticated endpoints, it cannot be used to log in to the GUI with it. Let’s have a look at the corresponding code. When a user logs in, the function `check_credentials` is called:

**checkmk/cmk/gui/userdb/htpasswd.py**

Copy to clipboard
  
  
  def check_credentials(self, user_id: UserId, password=***REDACTED*** -> CheckCredentialsResult:
  ...
  if self._is_automation_user(user_id):
  raise MKUserError(None, _("Automation user rejected"))
  ...

As we can see, the function `_is_automation_user` checks if the provided `user_id` corresponds to an automation user. If that is the case, an error is raised, and the GUI login fails. This is what the `_is_automation_user` function looks like:

**checkmk/cmk/gui/userdb/htpasswd.py**

Copy to clipboard
  
  
  def _is_automation_user(self, user_id: UserId) -> bool:
  return Path(cmk.utils.paths.var_dir, "web", str(user_id), "automation.secret").is_file()

Accordingly, the presence of the `automation.secret` file is used in order to determine if the user is an automation user.

By leveraging the Linefeed Injection vulnerability and the Nagios `PROCESS_FILE` command outlined in the [second article](/blog/checkmk-rce-chain-2/), an attacker has not only the ability to read arbitrary files but also to delete them. This means that the attacker can delete the `automation.secret` file after reading it. Since the login process verifies the provided credentials via the `htpasswd` file and the `automation.secret` file is not present, the automation user is assumed to be a normal user, and access to the GUI is granted:

![Checkmk-Remote Code Execution sheet](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/642df998-1cc9-4be2-8d77-0ff229927ab7/Checkmk-Remote%20Code%20Execution_3.png)

After the successful login, an attacker can exploit an authenticated code injection vulnerability.

### Code Injection watolib auth.php (CVE-2022-46836)

In order to seamlessly integrate NagVis into Checkmk, a file called `auth.php` is generated, which contains information about users, roles, and groups present in the Checkmk GUI. This file is updated when the corresponding data changes (e.g., user settings) by a function called `_create_auth_file`. This function loads the required data and calls `_create_php_file`:

**checkmk/cmk/gui/watolib/auth_php.py**

Copy to clipboard
  
  
  def _create_auth_file(callee, users=None):
  if users is None:
  users = userdb.load_users()
  ...
  _create_php_file(callee, users, get_role_permissions(), groups)

Within `_create_php_file` the content of the `auth.php` file is created and written to disk. In order to format the user data, the function `_format_php` is called:

**checkmk/cmk/gui/watolib/auth_php.py**

Copy to clipboard
  
  
  def _create_php_file(callee, users, role_permissions, groups):
  # Do not change WATO internal objects
  nagvis_users = copy.deepcopy(users)
  ...
  content = """<?php
  // Created by Multisite UserDB Hook (%s)
  global $mk_users, $mk_roles, $mk_groups;
  $mk_users  = %s;
  ...
  ?>
  """ % (
  callee,
  _format_php(nagvis_users),
  ...
  )
  
  store.makedirs(_auth_php().parent)
  store.save_text_to_file(_auth_php(), content)

The function `_format_php` converts the given data into the corresponding PHP representation. Data of type str is inserted into a single-quoted `string`. Single quotes within the data itself are escaped by prepending a backslash (`\`) to prevent the string context can be escaped:

**checkmk/cmk/gui/watolib/auth_php.py**

Copy to clipboard
  
  
  def _format_php(data, lvl=1):
  s = ""
  ...
  elif isinstance(data, str):
  s += "'%s'" % data.replace("'", "\\'")
  ...

The replacement does not take into account that the data can contain a backslash itself, followed by a single quote (`\'`). When encountering this sequence, the single quote is prepended by a backslash, which is escaped by the already present backslash (`\\'`). This way the string context can be escaped and arbitrary PHP code can be injected into the file.

An attacker can exploit the vulnerability after authenticating with the default automation user and then changing the profile settings. After the `auth.php` file is automatically updated, it contains the attacker-injected PHP code. The attacker now only needs to access the NagVis component, which includes the `auth.php` file and executes the injection code.

### Patch

The arbitrary file read vulnerability was [patched](https://github.com/NagVis/nagvis/commit/71aba7f46f79d846e1df037f165d206a2cd1d22a) in NagVis 1.9.34, which was [integrated](https://github.com/tribe29/checkmk/commit/84712e97760f6ecd9383b12b1f2b009377aad139) into Checkmk version 2.1.0p11 by limiting the requested scheme to `http` and `https`:

**nagvis/share/nagvis/htdocs/server/core/classes/NagVisHoverUrl.php**

Copy to clipboard
  
  
  private function readHoverUrl() {
  ...
  $aUrl = parse_url($this->url);
  if(!isset($aUrl['scheme']) || $aUrl['scheme'] == '' || ($aUrl['scheme'] != 'http' && $aUrl['scheme'] != 'https'))
  throw new NagVisException(l('problemReadingUrl', Array('URL' => $this->url, 'MSG' => l('Not allowed url'))));
  ...

The [code injection vulnerability](https://checkmk.com/werk/14383) was patched with Checkmk version 2.1.0p11 by escaping both single-quote characters and backslash characters ([commit](https://github.com/tribe29/checkmk/commit/a8a47e0269d21a26608a2051232c8914348101aa)):

**checkmk/cmk/gui/watolib/utils.py**

Copy to clipboard
  
  
  def format_php(data: object, lvl: int = 1) -> str:
  """Format a python object for php"""
  s = ""
  ...
  elif isinstance(data, str):
  s += "'%s'" % re.sub(r"('|\\)", r"\\\1", data)
  ...

## Timeline

**Date**| **Action**  
---|---  
2022-08-22| We report all issues to Checkmk.  
2022-08-23| Vendor confirms all issues.  
2022-08-29| NagVis patched version 1.9.34 is released.  
2022-08-30| Checkmk version 2.1.0p11 is released containing NagVis 1.9.34.  
  
## Summary

In this last article in the series, we detailed an authenticated, arbitrary file read vulnerability in NagVis, which enables an attacker to gain access to the Checkmk automation user. We further took a look at how Checkmk identifies automation users. This revealed that an attacker could leverage the arbitrary file deletion once more to gain access to the Checkmk GUI. This access can further be leveraged to exploit a code injection vulnerability in Checkmk’s watolib.

The arbitrary file read vulnerability is caused by a missing validation of the URL scheme. The impact of this vulnerability is greatly increased because the automation secret is stored in plaintext. Whether it be a file or a database, sensitive values, which can directly be used by an attacker to gain more privileges, should not be stored in plaintext. These sensitive values can for example be passwords, authentication tokens, or password reset tokens.

Dynamic code generation, like creating PHP files, can be very dangerous and should be avoided if possible. There is no built-in method that escapes values in the context of code generation for another language. Thus a custom implementation is required, and some cases can easily be missed. The outlined code injection vulnerability showed that a single mistake in the escaping implementation directly leads to code execution.

## Series Wrap-Up

This article completes the _Checkmk - Remote Code Execution by Chaining Multiple Bugs_ series. The series showcased how an attacker successively gained more abilities and access by chaining one vulnerability after another.

In general, web applications have become more secure in the past few years. Vulnerabilities instantly leading to remote code execution are far less common. This requires attackers to leverage less impactful vulnerabilities and chain them together. These chains are often only possible because the security precautions tend to be lower the higher the level of authentication.

The assumption that an attacker lacks a particular ability is dangerous and can quickly lead to a domino effect when an initial security boundary is breached. It is essential to apply security on all layers. Even one seemingly unimportant, additional security check can mitigate one link in an exploit chain and thus break the whole chain.

This is why Sonar believes in the [Code Quality approach](https://www.sonarsource.com/solutions/clean-code/), which embeds security as an integral part of the development. Handling security issues should not be a painful aftermath. Directly addressing and preventing these when the code is being developed saves time, work, and frustration. Our unique Clean as You Code approach addresses issues upfront, and no new issues end up in the released code. If you haven’t discovered the power of the Sonar solution yet, [you can learn more here](https://www.sonarsource.com/solutions/power-of-clean-code/).

Finally, we would like to highlight the professional reaction of the Checkmk team. There are security issues in each and every software. The difference is how these issues are dealt with. All of our reported issues were quickly verified, handled with absolute transparency, and fixed by providing comprehensive patches. Thank you!

## Related Blog Posts

  * [Checkmk: Remote Code Execution by Chaining Multiple Bugs (1/3)](https://www.sonarsource.com/blog/checkmk-rce-chain-1/)
  * [Checkmk: Remote Code Execution by Chaining Multiple Bugs (2/3)](https://www.sonarsource.com/blog/checkmk-rce-chain-2/)
  * [Zabbix - A Case Study of Unsafe Session Storage](https://www.sonarsource.com/blog/zabbix-case-study-of-unsafe-session-storage/)
  * [Path Traversal Vulnerabilities in Icinga Web](https://www.sonarsource.com/blog/path-traversal-vulnerabilities-in-icinga-web/)
