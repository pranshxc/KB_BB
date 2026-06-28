---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-12_pfsense-security-sensing-code-vulnerabilities-with-sonarcloud.md
original_filename: 2023-12-12_pfsense-security-sensing-code-vulnerabilities-with-sonarcloud.md
title: 'pfSense Security: Sensing Code Vulnerabilities with SonarCloud'
category: documents
detected_topics:
- command-injection
- xss
- sso
- file-upload
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- xss
- sso
- file-upload
- automation-abuse
- api-security
language: en
raw_sha256: 6e310b5959a36a5f7210546541a3e4e43b238dccd8995e807a6066bc17e9029e
text_sha256: d1bb5feccb27794d9fffd0cbc93d7fee8d5a1044cea8c9a59bc7d1f9579a6f0a
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# pfSense Security: Sensing Code Vulnerabilities with SonarCloud

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-12_pfsense-security-sensing-code-vulnerabilities-with-sonarcloud.md
- Source Type: markdown
- Detected Topics: command-injection, xss, sso, file-upload, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `6e310b5959a36a5f7210546541a3e4e43b238dccd8995e807a6066bc17e9029e`
- Text SHA256: `d1bb5feccb27794d9fffd0cbc93d7fee8d5a1044cea8c9a59bc7d1f9579a6f0a`


## Content

---
title: "pfSense Security: Sensing Code Vulnerabilities with SonarCloud"
page_title: "pfSense Security: Sensing Code Vulnerabilities with SonarCloud | Sonar"
url: "https://www.sonarsource.com/blog/pfsense-vulnerabilities-sonarcloud/"
final_url: "https://www.sonarsource.com/blog/pfsense-vulnerabilities-sonarcloud/"
authors: ["Oskar Zeino-Mahmalat"]
programs: ["pfSense"]
bugs: ["Reflected XSS", "OS command injection", "Security code review"]
publication_date: "2023-12-12"
added_date: "2024-01-02"
source: "pentester.land/writeups.json"
original_index: 635
---

## TL;DR overview

  * Sonar's research using SonarQube Cloud uncovered multiple vulnerabilities in pfSense—one of the most widely deployed open source firewall platforms—including cross-site scripting and command injection flaws in the web administration interface.
  * The web admin interface of a firewall is an especially critical attack surface: XSS in the admin panel can be leveraged to execute privileged commands or exfiltrate network configuration data with no further exploitation needed.
  * The findings were responsibly disclosed to the pfSense team and patched; they illustrate that even security-focused infrastructure software benefits from continuous static analysis.
  * Organizations running pfSense should apply security updates promptly and restrict administrative interface access to trusted network segments with strong authentication.

pfSense is a popular open-source firewall solution by Netgate. It is sold as pfSense Plus installed on ready-made firewall appliances to protect and manage office networks and also distributed for free as the pfSense Community Edition (CE). The [r/PFSENSE](https://www.reddit.com/r/PFSENSE/) subreddit has a large community with over 100 thousand members, lending credibility to [pfSense's tagline](https://www.pfsense.org/) "world's most trusted open source network security solution".

As part of our ongoing commitment to open-source security and to enhance our Code Quality technology, we routinely perform scans on open-source projects using SonarCloud and assess the results. Importantly, anyone can do this for free! [SonarCloud](https://sonarcloud.io) is available at no cost for open-source projects, regardless of their language or size.

During these scans, SonarCloud discovered two Cross-Site Scripting (XSS) vulnerabilities and a Command Injection vulnerability in pfSense CE. In combination, these security vulnerabilities allowed an attacker to execute arbitrary commands on a pfSense appliance. Security inside a local network is often more lax as network administrators trust their firewalls to protect them from remote attacks. Potential attackers could have used the discovered vulnerabilities to spy on traffic or attack services inside the local network.

In this article, we will cover two of the three security vulnerabilities in detail. We show how SonarCloud found these vulnerabilities using [taint analysis](https://www.sonarsource.com/blog/what-is-taint-analysis/), how they could have been exploited, and what the patch from Netgate looks like.

## pfSense Vulnerabilities Impact

**pfSense CE 2.7.0 and below, pfSense Plus 23.05.1 and below** are vulnerable to **two XSS** vulnerabilities and **a Command Injection** vulnerability ([CVE-2023-42325](https://nvd.nist.gov/vuln/detail/CVE-2023-42325), [CVE-2023-42327](https://nvd.nist.gov/vuln/detail/CVE-2023-42327), [CVE-2023-42326](https://nvd.nist.gov/vuln/detail/CVE-2023-42326)). The security vulnerabilities are fixed in pfSense CE 2.7.1 and pfSense Plus 23.09. Attackers can combine the vulnerabilities to **execute arbitrary code** on the pfSense appliance remotely. An attacker can trick an authenticated pfSense user into clicking on a maliciously crafted link containing an XSS payload that exploits the command injection vulnerability.

The victim user needs to be an admin user or at least have access to specific subsections of the pfSense WebGui. pfSense admins can check the user manager for non-admin users with these permissions:

  * Reflected XSS ([CVE-2023-42325](https://nvd.nist.gov/vuln/detail/CVE-2023-42325)):
  * WebCfg - Status: System Logs: Firewall (Dynamic View)
  * WebCfg - Status: Logs: Settings
  * Reflected XSS ([CVE-2023-42327](https://nvd.nist.gov/vuln/detail/CVE-2023-42327)):
  * WebCfg - AJAX: Get Service Providers
  * Command injection ([CVE-2023-42326](https://nvd.nist.gov/vuln/detail/CVE-2023-42326)):
  * WebCfg - Interfaces: GIF: Edit
  * WebCfg - Interfaces: GRE: Edit

  

## pfSense Security Vulnerabilities Technical Details

In this section, we first give a quick refresher on taint analysis, the technology that SonarCloud used to discover all three vulnerabilities. Then we explain the details and the taint flow for two of the three vulnerabilities:

  * Reflected XSS ([CVE-2023-42325](https://nvd.nist.gov/vuln/detail/CVE-2023-42325)): An unencoded filter string is reflected into a script tag.
  * Command Injection ([CVE-2023-42326](https://nvd.nist.gov/vuln/detail/CVE-2023-42326)): Unescaped user input is used inside a management shell command.
  * The second Reflected XSS vulnerability ([CVE-2023-42327](https://nvd.nist.gov/vuln/detail/CVE-2023-42327)) is similar to the first one, so we won't cover it in this post.

### Taint analysis

SonarCloud found the vulnerability using taint analysis. This type of static analysis tracks data flow from user-controllable data sources to dangerous sinks.

In the case of PHP, the sources include all data from a web request like URL parameters, the request body, cookies, and other headers. The taint flow from these sources is tracked through variables in the code, across several files. If the user-controllable data is validated, properly sanitized, or encoded during the flow, the flow is no longer tracked to ensure fewer false positive findings. Dangerous sinks include functions that invoke system commands, the reflection of data into the HTML page returned by the server, or other sensitive functions.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/4e3fb1ea-1942-4ee8-bc85-257db6467bb2/Taint%20analysis.png)

If SonarCloud finds a taint flow from source to sink, an issue is raised. The SonarCloud UI displays the discovered taint so that developers can easily understand and fix the issue. These features also helped us to quickly discover and verify the three reported vulnerabilities in pfSense.

### Reflected XSS (CVE-2023-42325)

One of the vulnerabilities discovered by SonarCloud was an XSS vulnerability on the `status_logs_filter_dynamic.php` page of the pfSense web GUI. This page provides a filterable live view of the firewall logs of pfSense. The filter selected by the user is sent as part of the URL query string to the pfSense server. To make the logs live, some JavaScript code in the page requests the newest filtered log entries every 30 seconds. These requests have to use the same filter as the original request. So the corresponding query string is constructed by server-side PHP code and reflected in the script tag.

  

The SonarCloud analysis found that there is a taint flow where parts of the reflected query string are user-controllable. Let's look into that flow to confirm this potential vulnerability. The numbered steps of the taint flow are marked in brackets.

  

[**View pfSense XSS issue on SonarCloud**](https://sonarcloud.io/project/issues?resolved=false&id=SonarSourceResearch_pfsense-blogpost&open=AYtcW5T0YkAG6r383NYb "pfSense XSS issue on SonarCloud")

  

First, a URL query parameter is returned by the utility function `getGETPOSTsettingvalue` in `guiconfig.inc`. SonarCloud detects the source array `$_GET` as tainted because the URL query parameters are user-controllable [1-3]. From here on, operation results containing the tainted return value of the function are also tainted.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/6751b6ea-bb6d-46a4-8853-a88c78344d8a/XSS%201%20Source.png)

The `getGETPOSTsettingvalue` function is used to set the `$interfacefilter` global variable [4-5]. This variable usually contains a filter string to filter the firewall logs. But the taint flow going through here shows that it can also contain attacker-controlled malicious values.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/31d0edd5-b2f1-4fd4-84da-53393481cb17/XSS%202.png)

Following the taint flow to the end, we see that the value of `$interfacefilter` is concatenated without encoding into `$filter_query_string`. `$filter_query_string` in turn is reflected on the page inside a script block as a JavaScript string, leading to the XSS vulnerability. SonarCloud correctly reports this taint flow as vulnerable, as no encoding or sanitization was used that would make the reflection harmless. Note that another variable `$filtertext` is also concatenated and encoded using `json_encode()` [8], suggesting that encoding for `$interfacefilter` was simply forgotten.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/bb69d19f-2d82-409c-bc4d-109f2a8f2534/XSS%203%20Sink.png)

An attacker could exploit this reflected XSS vulnerability by terminating the JS string and inserting their own code afterward. Leftover parts of the string after the injection point of the `interface` query parameter can be commented out. 

Copy to clipboard
  
  
  /status_logs_filter_dynamic.php?filtersubmit=1&interface=foo";alert(origin)//
  
  var filter_query_string = "<?= $filter_query_string . '&logfile=' . $logfile_path . '&nentries=' . $nentries?>";
  
  var filter_query_string = "type=raw&filter=&interfacefilter=foo";alert(origin) //&logfile=/var/log/filter.log&nentries=500";"

The attacker could then send a link with this crafted query parameter to an authenticated user of pfSense. After the victim clicks on the link, the JavaScript payload gets executed in the victim's browser and can perform actions in the pfSense firewall with the victim's permissions.

  

If the victim is an administrator of pfSense, the attacker can use that privilege to access the `diag_command.php` page. This page allows pfSense admins to execute arbitrary system commands on the pfSense firewall appliance.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/e6dab81e-26b3-46f3-97b6-9a28d59d47af/pfsense%20command%20execution.png)

So if an administrator user is targeted, the attacker could gain remote code execution (RCE) capabilities as root on the appliance. With RCE capabilities, the attacker can manipulate the firewall, spy on local network traffic, or attack services inside the local network.

  

But what if the victim of the XSS attack does not use the administrator account, out of caution or in a multi-user scenario? Is the RCE attack thwarted in that scenario? Unfortunately no, as we discovered a Command Injection vulnerability that also gives an attacker remote code execution capabilities while targeting a low-privilege pfSense user.

### Command Injection (CVE-2023-42326)

A key feature of the pfSense web UI is the network interfaces’ configuration of the server. The pfSense server code implements this by constructing shell command strings to call standard Linux binaries like `ifconfig`. The arguments in these shell commands are often taken from the configuration provided by the user, for example, the name of a network interface. This approach is vulnerable to Command Injection if the inserted arguments are not correctly validated or escaped.

  

SonarCloud found two similar vulnerable taint flows on the `interfaces_gif_edit.php` and `interfaces_gre_edit.php` pages. These flows started with user-controllable HTTP POST request data and ended in the `exec()` function, which executes shell commands without any validation or escaping of the data in between. We'll describe the first of the two taint flows, as they are almost identical.

  

[**View pfSense Command Injection issue on SonarCloud**](https://sonarcloud.io/project/issues?resolved=false&id=SonarSourceResearch_pfsense-blogpost&open=AYtcW5TLYkAG6r383NWA)

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/666ecd5d-dd3f-4362-85fb-e37aa3de27c8/Command%20Injection.png)

On the `interfaces_gif_edit.php` page, a new [Generic tunneling InterFace (GIF)](https://docs.netgate.com/pfsense/en/latest/interfaces/gif.html) can be created or an existing one edited. When a user creates a new GIF, all submitted form parameters like IP addresses (`remote-addr`) and the used network interface (`if`) are validated to contain expected, safe values. When editing an existing GIF, a hidden input element is inserted into the HTML form that holds the `gifif` form parameter. This parameter contains the name of the edited GIF. In both cases, all form parameters are passed as an array to the `interface_gif_configure()` function. Note that the `gifif` parameter was not validated at this point.

Copy to clipboard
  
  
  if (!$input_errors) {
  $gif = array();
  list($gif['if'], $gif['ipaddr']) = explode("|", $_POST['if']);
  // ...
  $gif['remote-addr'] = $_POST['remote-addr'];
  // ...
  $gif['gifif'] = $_POST['gifif'];
  $gif['gifif'] = interface_gif_configure($gif); // <--- HERE

The function `interface_gif_configure()` in the `interfaces.inc` file creates a new GIF or recreates the specified GIF using the supplied `$gif` array parameter. This is achieved by calling `ifconfig` and other shell commands with the `mwexec()` util function, which is just a thin wrapper around `exec()`. `escapeshellarg()` is used in an attempt to securely construct the shell command, but the function is only used on variables that are believed to be user-controllable, like `$gif[`'`remote-addr']`. The `$gif['gifif']` variable should contain the name of an already existing GIF that is recreated. So it is assumed that the value is safe and does not need to be escaped. But this assumption is wrong, as shown by the taint flow. `$gif['gifif']` is completely user-controllable, leading to a Command Injection vulnerability.

Copy to clipboard
  
  
  if (platform_booting() || !(empty($gif['gifif']))) {
  pfSense_interface_destroy($gif['gifif']);
  pfSense_interface_create2($gif['gifif']);
  $gifif = $gif['gifif'];
  } else {
  $gifif = pfSense_interface_create2("gif");
  }
  // ...
  mwexec("/sbin/ifconfig {$gifif} tunnel {$realifip} " .  escapeshellarg($gif['remote-addr']));

An attacker could exploit this vulnerability by inserting a semicolon to start a new shell command and commenting out the unwanted rest of the original command with a hashtag. Because the pfSense process runs as root to be able to change networking settings, the attacker can execute arbitrary system commands as root using this attack. The attacker needs access to a user account with permission to access the `interface_gif_edit.php/interface_gre_edit.php` page, which can be done with the previously shown XSS vulnerability.

Copy to clipboard
  
  
  ; whoami #
  
  mwexec("/sbin/ifconfig {$gifif} tunnel {$realifip} " .  escapeshellarg($gif['remote-addr']));
  
  /sbin/ifconfig ; whoami # tunnel 192.168.0.3 1.2.3.4

### pfSense Vulnerabilities Patches

Reflected XSS and Command Injection are both Injection vulnerabilities. To patch Injection vulnerabilities, it is necessary to encode/escape all inserted data for the context it is inserted into. We thank the Netgate team, who swiftly responded with patch commits:

  

In the Reflected XSS case on the `status_logs_filter_dynamic.php` page, the injection context is a JavaScript string. The pfSense maintainers at Netgate [patched](https://github.com/pfsense/pfsense/commit/f387c974a9a597bf01ab86ec049cca186a1e050c "pfsense/pfsense: f387c97") the security vulnerability by using the `json_encode()` and `urlencode()` functions, which were already used on neighboring variables.

Copy to clipboard
  
  
  if ($filtersubmit) {	# Raw mode.
  -  $filter_query_string = "type=raw&filter=" . urlencode(json_encode($filtertext )) . "&interfacefilter=" . $interfacefilter;
  +  $filter_query_string = "type=raw&filter=" . urlencode(json_encode($filtertext)) . "&interfacefilter=" . urlencode(json_encode($interfacefilter));
  }
  ...
  ?>
  var filter_query_string = "<?=$filter_query_string . '&logfile=' . $logfile_path . '&nentries=' . $nentries?>";

While `json_encode()` eliminates all ways for injected values to escape the string context here, the function is intended for encoding JSON, which is different from a JavaScript string inside a script block. In general, injections can still be possible if the wrong encoding function is used. To aid developers in choosing the right fix, each SonarCloud issue has a "How to fix it?" tab. Looking at [the tab for this issue](https://sonarcloud.io/project/issues?resolved=false&types=VULNERABILITY&id=SonarSourceResearch_pfsense-blogpost&open=AYtcW5T0YkAG6r383NYb&tab=how_to_fix), we see that the recommendation for reflected contents inside a script block is to use a data attribute. With an attribute, the context is HTML, and the `htmlentities()` function can be used safely. Unfortunately, there is no PHP function that makes reflecting user input inside script blocks completely safe in all cases, so this approach should be used instead.

Copy to clipboard
  
  
  <script data-filter="<?= htmlentities($interfacefilter) ?>">
  const filter = document.querySelector("[data-filter]").dataset.filter;
  </script>

For the Command Injection vulnerability, the injection context is a shell command. The maintainers used the `escapeshellarg()` function to [patch](https://github.com/pfsense/pfsense/commit/d69d6c8424ab4299234fb5ec6964682e2e6cbcdd "pfsense/pfsense: d69d6c8") the security vulnerability, which was also already used on neighboring variables. The function wraps its input argument in single quotes and escapes single quotes already present in the input. The shell will take everything wrapped in single quotes as a singular string argument to the current command, which prevents injected values from executing additional malicious commands.

Copy to clipboard
  
  
  - mwexec("/sbin/ifconfig {$gifif} tunnel {$realifip} " . escapeshellarg($gif['remote-addr']));
  + mwexec("/sbin/ifconfig " . escapeshellarg($gifif) . " tunnel " . escapeshellarg($realifip) . " " . escapeshellarg($gif['remote-addr']));

Additionally, the [patch](https://github.com/pfsense/pfsense/commit/d69d6c8424ab4299234fb5ec6964682e2e6cbcdd "pfsense/pfsense: d69d6c8") checks if the user input starts with a safe prefix to avoid an [Argument Injection vulnerability](https://sonarsource.github.io/argument-injection-vectors/explained/). If the input starts with a dash or two dashes and is used as an argument in the shell command, most programs would parse that as an option. This can have a serious impact as we have shown in [past publications](https://www.sonarsource.com/blog/securing-developer-tools-a-new-supply-chain-attack-on-php/).

Copy to clipboard
  
  
  + if (empty($_POST['gifif']) ||
  +  preg_match("/^gif[0-9]+$/", $_POST['gifif'])) {
  +  /* Attempt initial configuration of the GIF if the
  +  * submitted interface is empty or looks like a GIF
  +  * interface. */
  +  $gif['gifif'] = $_POST['gifif'];
  +  $gif['gifif'] = interface_gif_configure($gif);
  + } else {
  +  $input_errors[] = gettext("Invalid GIF interface.");
  + }

In both cases, encoding/escaping was already used, just not on every variable interpolated into a dangerous context. The wrong assumptions about which variables are user-controllable then lead to the shown vulnerabilities. That is why we recommend encoding/escaping all variables regardless of source, as there is usually no harm in doing so. This approach also hardens your code against future changes or bugs elsewhere in the codebase, contributing to a Code Quality state.

## Timeline

**Date**| **Action**  
---|---  
2023-07-03| We report all issues to Netgate  
2023-07-05| Netgate acknowledges all issues and publishes patch commits  
2023-10-31| Netgate publishes [advisories](https://docs.netgate.com/advisories/index.html) for all issues  
2023-11-06| Netgate releases patched version pfSense Plus 23.09  
2023-11-16| Netgate releases patched version pfSense CE 2.7.1  
  
## pfSense Vulnerabilities Summary

This blog post showcased two of the three security vulnerabilities SonarCloud discovered in pfSense. The vulnerable code samples highlighted that it is not easy for developers to remember encoding every user-controllable value in sensitive contexts, especially in large codebases. SonarCloud can help developers keep their code clean by finding injection and other vulnerabilities, all before the vulnerabilities make it into production.

## Related Blog Posts

  * [Unzipping Dangers: OpenRefine Zip Slip Vulnerability](https://www.sonarsource.com/blog/openrefine-zip-slip/)
  * [Pimcore: One click, two security vulnerabilities](https://www.sonarsource.com/blog/pimcore-one-click-two-security-vulnerabilities/)
  * [OpenEMR - Remote Code Execution in your Healthcare System](https://www.sonarsource.com/blog/openemr-remote-code-execution-in-your-healthcare-system/)
  * [Cacti: Unauthenticated Remote Code Execution](https://www.sonarsource.com/blog/cacti-unauthenticated-remote-code-execution/)
