---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-03_cacti-unauthenticated-remote-code-execution.md
original_filename: 2023-01-03_cacti-unauthenticated-remote-code-execution.md
title: 'Cacti: Unauthenticated Remote Code Execution'
category: documents
detected_topics:
- command-injection
- sso
- access-control
- ssrf
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- sso
- access-control
- ssrf
- automation-abuse
- api-security
language: en
raw_sha256: afc3216e50923af7359bc5962ead02f1486ae38df639b8b9adabceb9c0c733b5
text_sha256: f9763089374294500a2c049984bbd0a76dc307d689aecf8a9bdd4c7caccd6f1b
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Cacti: Unauthenticated Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-03_cacti-unauthenticated-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, sso, access-control, ssrf, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `afc3216e50923af7359bc5962ead02f1486ae38df639b8b9adabceb9c0c733b5`
- Text SHA256: `f9763089374294500a2c049984bbd0a76dc307d689aecf8a9bdd4c7caccd6f1b`


## Content

---
title: "Cacti: Unauthenticated Remote Code Execution"
page_title: "Cacti: Unauthenticated Remote Code Execution | Sonar"
url: "https://www.sonarsource.com/blog/cacti-unauthenticated-remote-code-execution/"
final_url: "https://www.sonarsource.com/blog/cacti-unauthenticated-remote-code-execution/"
authors: ["Stefan Schiller (@scryh_)"]
programs: ["Cacti"]
bugs: ["RCE", "Authentication bypass", "OS command injection", "Security code review"]
publication_date: "2023-01-03"
added_date: "2023-01-11"
source: "pentester.land/writeups.json"
original_index: 1703
---

## TL;DR overview

  * Sonar's security researchers found a critical unauthenticated remote code execution vulnerability in Cacti, a widely deployed network monitoring framework, that allows attackers to run arbitrary commands without valid credentials.
  * The vulnerability is present in an HTTP endpoint that handles data source selection—user-supplied input is passed unsanitized to a system command, creating a classic command injection scenario.
  * This vulnerability affects organizations running exposed Cacti instances and can lead to full infrastructure compromise if exploited.
  * Organizations using Cacti should immediately apply the available patch, restrict Cacti access to trusted internal networks, and audit their instances for signs of exploitation.

Cacti is an open-source, web-based monitoring solution with a long-standing history dating back to its first release in 2001. Nowadays, it is well established, actively maintained, and deployed worldwide. A quick Shodan search reveals that thousands of organizations publicly expose their instances to the internet.

To continuously improve the technology behind our Code Quality solution, we regularly scan open-source projects and evaluate the results. In the case of Cacti, our engine reported a promising command injection vulnerability. Analyzing this finding revealed that an unauthenticated attacker can exploit the vulnerability by leveraging an authentication bypass.

This article will outline the impact and deep dive into the technical details of the discovered vulnerabilities. Furthermore, we will determine the root cause of the vulnerabilities and explain how the applied patches mitigate them.

## Impact

The vulnerabilities affect Cacti version 1.2.22 and below and are tracked as CVE-2022-46169 with a CVSS score of 9.8. Unauthenticated attackers could exploit a vulnerable Cacti instance if any monitored device uses a specific data source. Exploiting allows attackers to run arbitrary commands under the same user as the web server process is running.

The following video demonstrates the exploitation of a server running a vulnerable version of Cacti:

The [security advisory](https://github.com/Cacti/cacti/security/advisories/GHSA-6p93-p743-35gf) contains a patch that system administrators must apply manually for Cacti versions 1.2.22 and below. The patch will be released as part of versions 1.2.23 and 1.3.0.

**We strongly recommend applying the provided patches and updating to a new version once available.**

## Technical Details

In this section, we look at the vulnerability reported by SonarQube Cloud and determine how an attacker can exploit it. The attack we demonstrate is made of two distinct code vulnerabilities:

  1. Authentication Bypass: a hostname-based authorization check is not implemented safely for most installations of Cacti
  2. Command Injection: unsanitized user input is propagated to a string used to execute an external command

### Authentication Bypass

The script `remote_agent.php` is supposed to be accessed by authorized clients only. For this reason, there is an authorization check at the beginning of the file:

**cacti/remote_agent.php**

Copy to clipboard
  
  
  <?php
  // ...
  if (!remote_client_authorized()) {
  print 'FATAL: You are not authorized to use this service';
  exit;
  }

The function `remote_client_authorized` retrieves the IP address of the client (`$client_addr`), resolves it to the corresponding hostname (`$client_name`) and checks if the `poller` table contains an entry with this hostname:

**cacti/lib/html_utility.php**

Copy to clipboard
  
  
  <?php
  // ...
  function remote_client_authorized() {
  // ...
  $client_addr = get_client_addr();
  // ...
  $client_name = gethostbyaddr($client_addr);
  // ...
  $pollers = db_fetch_assoc('SELECT * FROM poller', true, $poller_db_cnn_id);
  foreach($pollers as $poller) {
  if (remote_agent_strip_domain($poller['hostname']) == $client_name) {
  return true;
  // ...

The above code snippet shows that the function `get_client_addr` retrieves the IP address of the client. This function takes into account a variety of attacker-controllable HTTP headers when determining the IP address:

**cacti/lib/functions.php**

Copy to clipboard
  
  
  <?php
  // ...
  function get_client_addr($client_addr = false) {
  $http_addr_headers = array(
  // ...
  'HTTP_X_FORWARDED',
  'HTTP_X_FORWARDED_FOR',
  'HTTP_X_CLUSTER_CLIENT_IP',
  'HTTP_FORWARDED_FOR',
  'HTTP_FORWARDED',
  'HTTP_CLIENT_IP',
  'REMOTE_ADDR',
  );
  
  $client_addr = false;
  foreach ($http_addr_headers as $header) {
  // ...
  $header_ips = explode(',', $_SERVER[$header]);
  foreach ($header_ips as $header_ip) {
  // ...
  $client_addr = $header_ip;
  break 2;
  }
  }
  return $client_addr;
  }
  

While the `REMOTE_ADDR` variable is set to the source IP address from the connection to the web server, variables beginning with `HTTP_` are populated by the corresponding HTTP headers received from the client. Attackers can fully control these values if there is no instance between the client and the web server (i.e., a reverse proxy) that would filter these HTTP headers.

Coming back to the former code snippet, the `poller` table contains a default entry with the hostname of the server running Cacti. Because of this, attackers can bypass the `remote_client_authorized` check by, e.g., providing the HTTP header `X-Forwarded: <TARGET-IP>`. This way, the function `get_client_addr` returns the IP address of the server running Cacti. The call to `gethostbyaddr` resolves this IP address to the hostname of the server, which will pass the poller hostname check because of the default entry.

This allows unauthenticated attackers to access the functionality of `remote_agent.php`. 

### Command Injection Vulnerability

Scanning Cacti with SonarQube Cloud revealed an interesting command injection vulnerability in `remote_agent.php`. You can inspect the finding directly on SonarQube Cloud:

[**Try it by yourself on SonarQube Cloud!**](https://sonarcloud.io/project/issues?resolved=false&types=VULNERABILITY&id=SonarSourceResearch_cacti-blogpost&open=AYVi68k7Wm9EF-_N9Gwb)

According to the outlined injection flow, the user-provided parameter `poller_id` is propagated to the first parameter of `proc_open` without any sanitization or escaping. This introduces a command injection vulnerability in the `poll_for_data` function.

Attackers can trigger the vulnerable function by setting the `action` parameter to `polldata`:

**cacti/remote_agent.php**

Copy to clipboard
  
  
  <?php
  // ...
  switch (get_request_var('action')) {
  case 'polldata':
  poll_for_data();

In the beginning, the `poll_for_data` function retrieves the parameters `host_id` and `poller_id`. However, there is an essential difference: The `host_id` parameter comes from `get_filter_request_var`, while the `poller_id` parameter comes from `get_nfilter_request_var`; notice the additional `n` character here:

**cacti/remote_agent.php**

Copy to clipboard
  
  
  <?php
  // ...
  function poll_for_data() {
  // ...
  $host_id  = get_filter_request_var('host_id');
  $poller_id  = get_nfilter_request_var('poller_id');

While the `get_filter_request_var` function verifies that the retrieved parameter is an integer, `get_nfilter_request_var`, which is used to retrieve the `poller_id` parameter, allows arbitrary strings.

Further following the injection flow, we can see that poller items are retrieved from the database. If the action of one of these items is set to `POLLER_ACTION_SCRIPT_PHP`, the vulnerable call to `proc_open` is issued:

**cacti/remote_agent.php**

Copy to clipboard
  
  
  <?php
  
  // ... retrieve poller items from database ...
  
  foreach($items as $item) {
  switch ($item['action']) {
  // ...
  case POLLER_ACTION_SCRIPT_PHP: /* script (php script server) */
  // ...
  $cactiphp = proc_open(read_config_option('path_php_binary') . ' -q ' . $config['base_path'] . '/script_server.php realtime ' . $poller_id, $cactides, $pipes);

This means that attackers can leverage the `poller_id` parameter to inject an arbitrary command when an item with the `POLLER_ACTION_SCRIPT_PHP` action exists. This is very likely on a productive instance because this action is added by some predefined templates like `"Device - Uptime"` or `"Device - Polling Time"`.

The attacker must provide the corresponding id to make the database query return such an item. Since the ids are numbered in ascending order and hundreds of ids can be sent in a single request by providing an array, attackers can easily discover a valid identifier.

## Patches

### Authentication Bypass

The authentication bypass was mitigated by allowing the administrator to configure which HTTP proxy headers should be honored when determining the IP address of a client. Only the `REMOTE_ADDR` server variable is used by default, ensuring a secure default configuration.

Additionally, this patch allows administrators to use HTTP proxy headers, e.g., in scenarios where the Cacti instance is behind a reverse proxy.

### Command Injection

The command injection vulnerability was mitigated with two fixes applied to the source (retrieval of user input) and the sink (call to `proc_open`). At the source, the function `get_nfilter_request_var` was replaced with `get_filter_request_var` to ensure that the `poller_id` parameter is an integer:

**cacti/remote_agent.php**

Copy to clipboard
  
  
  <?php
  // ...
  function poll_for_data() {
  // ...
  $poller_id  = get_filter_request_var('poller_id');

At the sink, the `$poller_id` variable was escaped via `cacti_escapeshellarg` before being inserted into the command string of `proc_open`:

**cacti/remote_agent.php**

Copy to clipboard
  
  
  <?php
  // ...
  $cactiphp = proc_open(read_config_option('path_php_binary') . ' -q ' . $config['base_path'] . '/script_server.php realtime ' . cacti_escapeshellarg($poller_id), $cactides, $pipes);

This second fix may seem unnecessary, as the validation at the source already ensures that the variable contains an integer. However, adjusting the source code may change this assumption in the future, reintroducing a critical vulnerability. 

Because of this, both fixes are essential: user input should always be validated and restricted to the assumed values (an integer in this case). Furthermore, values should always be escaped before being passed to sensitive functions like `proc_open`.

## Timeline

**Date**| **Action**  
---|---  
2022-12-02| We report all issues to vendor  
2022-12-02| Vendor confirmes the issues  
2022-12-02| Vendor provides patch via security advisory  
  
Based on our information, the same vulnerabilities were independently discovered by [@stevenseeley](http://infosec.exchange/@stevenseeley) and reported via ZDI on 2022-11-25. Further details are not available at the time of writing.

## Summary

In this article, we detailed a critical command injection vulnerability in the IT monitoring solution Cacti. This code vulnerability is automatically detected by our scanning engine. We also uncovered a bug in the authentication mechanism, allowing its exploitation from an unauthenticated position. We also looked at the patches applied to fix the vulnerabilities.

The patches and the fact that either of the two applied fixes for the command injection vulnerability would have prevented it highlights how important it is to apply security on all layers. Because of this, an essential part of our [Code Quality approach](https://www.sonarsource.com/solutions/clean-code/) is to embed security as an integral part of development. This ensures that security considerations are not only applied to the current state of the source code, reducing the risk of introducing new vulnerabilities.

Finally, we would like to thank the Cacti maintainers ([@netniV](https://github.com/netniV), [@TheWitness](https://github.com/TheWitness)), who almost instantly verified the issues and provided a comprehensive patch!

## Related Blog Posts

  * [Checkmk: Remote Code Execution by Chaining Multiple Bugs (1/3)](https://www.sonarsource.com/blog/checkmk-rce-chain-1/)
  * [Zabbix - A Case Study of Unsafe Session Storage](https://www.sonarsource.com/blog/zabbix-case-study-of-unsafe-session-storage/)
