---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-15_checkmk-remote-code-execution-by-chaining-multiple-bugs-23.md
original_filename: 2022-11-15_checkmk-remote-code-execution-by-chaining-multiple-bugs-23.md
title: 'Checkmk: Remote Code Execution by Chaining Multiple Bugs (2/3)'
category: documents
detected_topics:
- command-injection
- ssrf
- sqli
- path-traversal
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- ssrf
- sqli
- path-traversal
- api-security
- mobile-security
language: en
raw_sha256: 9e8a3490d60e60b8a51c77b085ba1b514b0075641532d040d24554b6178e5e06
text_sha256: e980dd70c7bc79e6b13bb23b7fcbfbd39797a38ea4fbf3e821f66c827a1f5980
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Checkmk: Remote Code Execution by Chaining Multiple Bugs (2/3)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-15_checkmk-remote-code-execution-by-chaining-multiple-bugs-23.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, sqli, path-traversal, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `9e8a3490d60e60b8a51c77b085ba1b514b0075641532d040d24554b6178e5e06`
- Text SHA256: `e980dd70c7bc79e6b13bb23b7fcbfbd39797a38ea4fbf3e821f66c827a1f5980`


## Content

---
title: "Checkmk: Remote Code Execution by Chaining Multiple Bugs (2/3)"
page_title: "Checkmk: Remote Code Execution by Chaining Multiple Bugs (2/3) | Sonar"
url: "https://blog.sonarsource.com/checkmk-rce-chain-2/"
final_url: "https://www.sonarsource.com/blog/checkmk-rce-chain-2/"
authors: ["Stefan Schiller (@scryh_)"]
programs: ["Checkmk"]
bugs: ["RCE", "Code injection", "SSRF", "Line Feed injection", "Arbitrary file read", "Authentication bypass", "Security code review"]
publication_date: "2022-11-15"
added_date: "2022-11-17"
source: "pentester.land/writeups.json"
original_index: 1912
---

## TL;DR overview

  * Part two of the Checkmk series builds on the initial authentication bypass to demonstrate how command injection in a downstream component enables attackers to execute arbitrary OS commands on the Checkmk server.
  * The chained exploit moves from limited API access to full server compromise by exploiting improper sanitization of monitoring check parameters that are passed to shell commands.
  * This research illustrates a common pattern in monitoring and operations tooling: privileged system access creates a large attack surface, and insufficient input validation in any component can lead to full compromise.
  * IT teams should treat Checkmk—and similar monitoring platforms—as security-critical infrastructure, applying patches promptly and restricting management interfaces to trusted networks.

This is the second of three articles in the  _Checkmk - Remote Code Execution by Chaining Multiple Bugs_ series ([first article](https://blog.sonarsource.com/checkmk-rce-chain-1/)). The series of articles outlines the results of our effort to help secure the open-source world and better understand real-world vulnerabilities by auditing the open-source edition of Checkmk. Our research resulted in the discovery of multiple vulnerabilities in Checkmk and its NagVis integration, which can be chained together by an unauthenticated, remote attacker to fully take over the server running a vulnerable version of Checkmk.

In the [first article](https://blog.sonarsource.com/checkmk-rce-chain-1/) of the series, we started by getting an overview of all identified vulnerabilities and got a basic understanding of the Checkmk architecture. Furthermore, we determined the severe impact of chaining the identified vulnerabilities together. We also deep-dived into the technical details of the first two vulnerabilities.

In this second article, we will have a more detailed look at the LQL interface and derive the impact of an attacker’s ability to forge arbitrary queries. We will then look at Checkmk’s NagVis integration and how some minor implementation differences between Checkmk and NagVis enable an attacker to bypass the NagVis authentication.

## Technical Details

We start this section by briefly recapping the vulnerabilities and exploitation chain. After this, we focus on the LQL interface and outline how an attacker can leverage it to exfiltrate monitoring data and bypass the NagVis authentication.

### Exploitation Chain

As a reminder the following picture summarizes the exploitation chain enabling an unauthenticated attacker to gain remote code execution:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/a105e576-1cdd-4631-bdda-105523ae763a/body-fee129ee-2bd1-496a-9e34-2cbabbf0e3b2_checkmk-chain-all.png)

In the [first article](https://blog.sonarsource.com/checkmk-rce-chain-1/), we covered the first two vulnerabilities: a Server-Side Request Forgery in the agent-receiver (1) as well as a Line Feed Injection (2), which can be exploited by an unauthenticated attacker to forge arbitrary LQL queries. Before an attacker can further leverage the Arbitrary File Read vulnerability (3) followed by the Code Injection (4) vulnerability, authenticated access to NagVis is required.

Within this article, we unveil the impact of an attacker’s ability to forge arbitrary LQL queries. We start by determining how an attacker can exfiltrate monitoring data. After this, we describe how the LQL interface can be leveraged to delete arbitrary files and furthermore bypass the NagVis authentication:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/c1c62328-3efb-4966-8fee-1ea9f7144eac/body-17eb433a-9704-4b80-9946-9474a5e79c4e_checkmk-part2.png)

### Monitoring Data Exfiltration

The LQL interface is mainly used to retrieve data from the monitoring core. This data consists for example of internal hostnames and IP addresses of monitored hosts, running services, contact persons, and their email addresses. Although this data is not highly sensitive, it can be useful for an attacker to mount further attacks. Thus an attacker might be interested in retrieving this data.

**Blind Data Exfiltration**

Although an attacker is able to forge arbitrary LQL queries by leveraging the two vulnerabilities we covered so far, the response cannot be read by the attacker. The reason for this is that neither the vulnerable endpoint `/ajax_graph_images.py` directly outputs the retrieved data, nor can the SSRF, which is leveraged to request this endpoint, be used to read the response. Thus the attacker is dealing with a blind LQL injection.

This scenario can be compared with a blind SQL injection. Attackers typically use a time-based approach to exploit this vulnerability. For example, the following SQL query could be used to determine if the first character of the first `name` in the table `users` is `'a'`:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/425b9172-9c14-4576-b16d-3831062e3b7c/body-fd07ab5f-3548-4d9d-83f8-6172342997e7_checkmk-sql.png)

If the condition is satisfied, the call to `SLEEP(5)` delays the response of the query by five seconds. By iterating over each possible character and measuring the time the response takes, the first character can be determined. This process can be repeated with the second character and so forth until the whole username is exfiltrated.

**LQL Blind Data Exfiltration**

An attacker can use a similar approach to blindly retrieve data from the LQL interface by using [time delays](https://docs.checkmk.com/latest/en/livestatus.html#_time_delays_wait). The purpose of time delays is that some data needs to be retrieved only if a specific condition is satisfied. For example, the disk usage of a host should be reported when the CPU load of this host exceeds a specific threshold.

The headers required to use time delays are prefixed with `Wait`. The relevant headers for our considerations are these:

  * `WaitObject`: Name identifying the object for which a condition should be satisfied.
  * `WaitCondition`: Condition, which should be satisfied.
  * `WaitTimeout`: Limit in milliseconds after which the query will be executed even if the condition was not satisfied.

The `WaitObject` header is required, which means that an attacker has to know the name of the object, whose data the attacker wants to retrieve. The easiest but also noisiest approach an attacker may use is a word list attack. By using the following query, an attacker could determine if a host with the name `ldap` exists:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/0c8c5ada-e1c3-42c4-8722-12c8dcb934c1/body-dea4b1bc-ef9a-40aa-addf-5b8547458188_checkmk-exfil-1.png)

If there is no host with the name `ldap`, the query immediately returns. If the host exists, the condition is never satisfied, and the query times out after 2000 ms verifying the existence of the host.

A more efficient way to determine the name of monitored hosts is to use the `hostgroups` table. By default, each host is added to the default host group `check_mk`. This is the name of the `hostgroups` object within this table and can thus be used for the `WaitObject` header. The table contains a column called `members`, which contains all hostnames within this host group. For example, a request to this table may look like this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/5efbc240-6dc8-46f1-804b-abb34fdbea02/body-1604919f-b9f0-4750-ab0a-7be0add3997b_checkmk-exfil-2.png)

The response contains the name of all hosts:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/4bc3f41b-7b96-4418-a0e4-7c161d15f5cf/body-6d69a322-9e4c-472a-b25e-9cd943596fc6_checkmk-exfil-3.png)

By setting the `WaitCondition` on this column and using a regular expression, all hostnames can be exfiltrated character by character. The following query determines, if there is a hostname that begins with "`serv`":

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/7ee8d7b5-b8bc-4071-a984-a8ac4bbb0b73/body-e7c35000-2530-495d-a374-93bfa6bb6a6e_checkmk-exfil-4.png)

Once all hostnames have been exfiltrated, an attacker can use these names for the `WaitObject` header on the `hosts` table in order to retrieve all data from a given host, for example, the IP address:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/3887a137-b25b-49ca-9c78-cf36c74232e6/body-60209a45-9478-4015-b454-2bbe011a44a6_checkmk-exfil-5.png)

Also, the name of the contact responsible for the host can be exfiltrated:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/31829741-7351-451e-83f2-dee054cf31d4/body-198f5e2c-7153-4b3b-b118-389536d9ce05_checkmk-exfil-6.png)

After having retrieved the name of a contact, further information about this contact can be retrieved via the `contacts` table:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/179d978a-2892-4070-870f-a3ba06b4f2b2/body-388e9e29-3296-4737-bbd6-d134c338043b_checkmk-exfil-7.png)

The fact that the values in a column of one table often contain the names of objects in another table makes it possible to gradually exfiltrate the whole data set.

The following video illustrates how the two vulnerabilities detailed in the first article are used by an unauthenticated, remote attacker to exfiltrate monitoring data from a vulnerable Checkmk server:

After this quick look at the possibilities of data exfiltration, let’s continue with the exploitation chain by determining how an attacker can gain access to Checkmk’s NagVis component:

### NagVis Authentication Bypass

The LQL interface can not only be used to retrieve data but also to send external commands to the monitoring core by issuing a `COMMAND` request. Although the term command might suggest immediate code execution, the abilities are very limited.

**Nagios External Commands**

The [documented commands](https://docs.checkmk.com/latest/en/livestatus_references.html#commands) are supported by the open-source Raw Edition as well as the Enterprise Editions. These commands can for example be used to enable or disable checks and notifications. Since the open-source Raw Edition uses a Nagios monitoring core, there are a few additional commands listed in the [Nagios documentation](https://assets.nagios.com/downloads/nagioscore/docs/externalcmds/). Nevertheless, sensitive commands like `CMD_CHANGE_HOST_CHECK_COMMAND`, which alter the command executed to perform host checks, were disabled for security reasons back [in 2008](https://github.com/NagiosEnterprises/nagioscore/commit/3207e91193cb507401858a6136fc6e3fc257a236).

One additional Nagios command, which is still enabled, is called [PROCESS_FILE](https://assets.nagios.com/downloads/nagioscore/docs/externalcmds/cmdinfo.php?command_id=131). The format of this command is structured like this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/50d0f777-bd51-4bea-b5be-9dfa37a8e26d/body-742911a4-25ec-4011-a90c-afa985252365_checkmk-exfil-8.png)

Issuing this command directs the Nagios core to read the file specified by `<file_name>` and execute each line in the file as an external command. This does not increase the attack surface per se because there is no difference from directly issuing an external command. However, if the second parameter `<delete>` is non-zero, the file will be deleted after it has been processed. The deletion of the file does not depend on its contents. Even if the file does not contain any valid external command, it will be deleted: **this command gives an attacker an arbitrary file deletion primitive**. In order to understand how this can be leveraged by an attacker, let’s have a look at how Checkmk’s authentication mechanism works.

**Checkmk Authentication Mechanism**

After a successful login, a session cookie is created, which identifies the user. This cookie is structured like this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/d6a4a7bb-5835-47c1-87d4-1b4cc3636914/body-550adf61-aa44-4765-ba5c-427945619af3_checkmk-auth-1.png)

For example, a cookie for the `cmkadmin` user may look like this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/77013624-1191-4e61-a1e7-8e553b304352/body-45445a7a-9ab1-4cdc-80d9-67b553e48e04_checkmk-auth-2.png)

The hash at the end of the cookie is created by `_generate_auth_hash`, which calls `_generate_hash`:

**checkmk/cmk/gui/login.py**

Copy to clipboard
  
  
  def _generate_auth_hash(username: UserId, session_id: str) -> str:
  return _generate_hash(username, username + session_id)
  
  def _generate_hash(username: UserId, value: str) -> str:
  """Generates a hash to be added into the cookie value"""
  secret = _load_secret()
  serial = _load_serial(username)
  return sha256((value + str(serial) + secret).encode()).hexdigest()

Accordingly, the hash is calculated like this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/f26deb5b-344b-4030-b39d-4670d1b1af4b/body-0689d41d-2d37-4ddd-9001-394a77ae84f8_checkmk-auth-3.png)

To verify a cookie, the Checkmk GUI recalculates the hash and compares it with the hash from the cookie:

**checkmk/cmk/gui/login.py**

Copy to clipboard
  
  
  def check_parsed_auth_cookie(username: UserId, session_id: str, cookie_hash: str) -> None:
  # ...
  if cookie_hash != _generate_auth_hash(username, session_id):
  raise MKAuthException(_("Invalid credentials"))

An attacker, who wants to forge a valid cookie, needs to know all four values from the hash calculation. The `username` and `session_id` are part of the cookie itself and are thus known. The `serial` value of a user is initialized with `0` and incremented by one each time the user’s password is changed, or the user account gets locked. Thus an attacker can simply test successive values starting with `0`. The last value called `secret` is retrieved via the `_load_secret function`:

**checkmk/cmk/gui/login.py**

Copy to clipboard
  
  
  def _load_secret() -> str:
  # ...
  secret_path = htpasswd_path.parent.joinpath("auth.secret")
  
  secret = ""
  if secret_path.exists():
  with secret_path.open(encoding="utf-8") as f:
  secret = f.read().strip()
  # ...
  if secret == "" or len(secret) == 32:
  secret = _generate_secret()
  with secret_path.open("w", encoding="utf-8") as f:
  f.write(secret)
  
  return secret

The `secret` value is read from a file called `auth.secret`. If the content of this file is empty or only 32 bytes in length, a new secret is generated and written to the file. The `_generate_secret` function returns 256 random characters:

**checkmk/cmk/gui/login.py**

Copy to clipboard
  
  
  def _generate_secret() -> str:
  return utils.get_random_string(256)

This value is unknown to an attacker and cannot easily be guessed. Without this value it is not possible to forge a valid session cookie:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/78e49387-0b12-4223-b693-d6d67631477d/body-82379d59-8115-479e-883b-fc98db0c7b24_checkmk-auth-4.png)

There are two important aspects to highlight here:

  1. `_load_secret` does always return 256 random characters, even if the `auth.secret` file was not present or was not read properly.
  2. The `auth.secret` file is recreated if it is not present.

**Leveraging Arbitrary File Deletion**

An attacker could try to achieve that the `secret` value is empty and thus known. Though, if the attacker uses the arbitrary file deletion primitive to delete the `auth.secret` file, it would be recreated on the fly, and the `secret` value would be populated with a new value, unknown to the attacker. Thus the ability to delete arbitrary files does not seem to enable an attacker to bypass the authentication of the Checkmk GUI.

When getting a basic overview of the Checkmk architecture in the [first article](https://example.com/) of this series, we outlined that Checkmk integrates the NagVis PHP component. This integration is seamless from an authentication point of view, meaning that a user authenticated to the Checkmk GUI can also access the NagVis component. In order to make this possible, the NagVis class `CoreLogonMultisite` verifies the session cookie within the `checkAuthCookie` function:

**nagvis/share/nagvis/htdocs/server/core/classes/CoreLogonMultisite.php**

Copy to clipboard
  
  
  private function checkAuthCookie($cookieName) {
  // ...
  list($username, $sessionId, $cookieHash) = explode(':', $cookieValue, 3);
  // ...
  $users = $this->loadAuthFile($this->serialsPath);
  // ...
  $user_secret = $users[$username];
  // ...
  $hash = $this->generateHash($username, $sessionId, (string) $user_secret);
  // ...
  // Validate the hash
  if ($cookieHash != $hash) {
  throw new Exception();
  }
  // ...
  return $username;
  }

At first, the cookie is separated into its three components: `$username`, `$sessionId`, and `$cookieHash`. The `$user_secret` value read via the `loadAuthFile` function is the serial value we have already encountered. The function `generateHash` is used to calculate the hash with the given parameters. If the calculated hash matches the hash from the cookie, the user is assumed to be authenticated. Advanced readers may have noticed a [type juggling vulnerability](https://checkmk.com/werk/14291) here, which we reported additionally (CVE-2022-3979). Its exploitation is far more laborious and its presence is not relevant for our considerations. So let’s continue with the `generateHash` function, which is similar to its Checkmk GUI Python equivalent:

**nagvis/share/nagvis/htdocs/server/core/classes/CoreLogonMultisite.php**

Copy to clipboard
  
  
  private function generateHash($username, $session_id, $user_secret) {
  $secret = $this->loadSecret();
  return hash("sha256", $username . $session_id. $user_secret . $secret);
  }

Though, the implementation of the called `loadSecret` function is less complex than its Python equivalent:

**nagvis/share/nagvis/htdocs/server/core/classes/CoreLogonMultisite.php**

Copy to clipboard
  
  
  private function loadSecret() {
  return trim(file_get_contents($this->secretPath));
  }

The function reads the `$secret` value from the `auth.secret` file, but it does neither handle any file reading errors nor recreate the file if it is not present.

The goal of an attacker would be to make the `$secret` value empty and thus known. Let’s determine what happens if `file_get_contents` is called on a non-existent file:

Copy to clipboard
  
  
  php > var_dump(file_get_contents('/tmp/not.existing'));
  PHP Warning:  file_get_contents(/tmp/not.existing): Failed to open stream: No such file or directory in php shell code on line 1
  bool(false)

A warning is raised and the function returns `false`. Due to the error handlers, NagVis employed, this warning triggers an exception, which prevents further code from being executed. Thus simply deleting the `auth.secret` file does not yield an empty `$secret` value.

**Winning The File Race**

However, an attacker can leverage an important characteristic of the `_load_secret` function in the Checkmk GUI. This function recreates the `auth.secret` file with a new secret value if the file is not existing. The creation of the file (`open`) and the writing of the new secret value to it (`write`) are two distinct operations. If the `loadSecret` PHP function calls `file_get_contents` right after the `auth.secret` file was recreated, but the new secret value has not yet been written, `file_get_contents` simply operates on an existing but empty file, and an empty string is returned:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/14c06b0b-0862-4495-af25-e0808aa45162/body-cccc6d5f-ffa1-4248-a30c-41aa687b183a_checkmk-auth-5.png)

(1) At first, an attacker can leverage the SSRF and LF Injection vulnerabilities to trigger an LQL query with the `PROCESS_FILE` command to delete the `auth.secret` file. After this, the attacker can quickly trigger two requests: (2) one request to the Checkmk GUI to recreate the `auth.secret` file and (3) another request to NagVis with a forged cookie assuming an empty `$secret` value. If the resulting `file_get_contents` call in NagVis is executed at the right time, the `$secret` value is empty, and access to NagVis is granted. If the attempt fails, the process can simply be repeated.

The mere ability of an unauthenticated attacker to delete arbitrary files leads to an authentication bypass, even without the presence of an additional vulnerability. Although this attack requires a few attempts, it can reliably be exploited to gain access to NagVis. The more fail-safe implementation in the Checkmk GUI itself prevents an attacker from exploiting it here. Though with access to NagVis, an attacker has crossed another security boundary, and the exposed attack surface is further increased.

## Timeline

**Date**| **Action**  
---|---  
2022-08-22| We report all issues to Checkmk.  
2022-08-23| Vendor confirms all issues.  
2022-09-15| Vendor releases patched version 2.1.0p12.  
  
## Summary

In this second article in a series of three, we outlined the impact of an attacker’s ability to forge arbitrary LQL queries. Firstly, a time-based approach could be used to exfiltrate data from the monitoring core, which can be useful to mount further attacks. Furthermore, an attacker can use the `PROCESS_FILE` command to delete arbitrary files and leverage this to bypass the authentication of NagVis. This is achieved by making two simultaneous requests, which results in an empty secret value if the single file operations are executed in a specific order.

The NagVis authentication bypass is only possible because an attacker already has the ability to delete arbitrary files. Nevertheless, the slightly different implementations in NagVis and the Checkmk GUI make a great difference. Since the Checkmk GUI implementation assures that the secret value cannot be empty, the outlined technique does not work here. This approach follows a  _defense-in-depth_ mindset and should generally be applied. It prevents an attacker from easily escalating privileges once an initial security boundary is breached.

The next article in this series will continue where we left off here: an attacker has gained access to the NagVis component exposing a new attack surface. This allows the attacker to exploit an authenticated, arbitrary file read vulnerability in NagVis, which can be used to gain access to the Checkmk GUI itself. At last, we take a detailed look at an authenticated code injection vulnerability in Checkmk, which can, at this point, be exploited by the initially unauthenticated attacker to gain remote code execution.

We would like to thank the Checkmk team very much for quickly responding to our report, handling each issue with absolute transparency, and providing a comprehensive patch for all reported vulnerabilities.

## Related Blog Posts

  * [Checkmk: Remote Code Execution by Chaining Multiple Bugs (1/3)](https://www.sonarsource.com/blog/checkmk-rce-chain-1/)
  * [Checkmk: Remote Code Execution by Chaining Multiple Bugs (3/3)](https://www.sonarsource.com/blog/checkmk-rce-chain-3/)
  * [Zabbix - A Case Study of Unsafe Session Storage](https://www.sonarsource.com/blog/zabbix-case-study-of-unsafe-session-storage/)
  * [Path Traversal Vulnerabilities in Icinga Web](https://www.sonarsource.com/blog/path-traversal-vulnerabilities-in-icinga-web/)
