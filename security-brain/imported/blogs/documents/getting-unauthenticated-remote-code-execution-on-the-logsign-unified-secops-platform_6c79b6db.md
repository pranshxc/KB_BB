---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-01_getting-unauthenticated-remote-code-execution-on-the-logsign-unified-secops-plat.md
original_filename: 2024-07-01_getting-unauthenticated-remote-code-execution-on-the-logsign-unified-secops-plat.md
title: Getting Unauthenticated Remote Code Execution On The Logsign Unified Secops
  Platform
category: documents
detected_topics:
- command-injection
- rate-limit
- sso
- password-reset
- otp
- api-security
tags:
- imported
- documents
- command-injection
- rate-limit
- sso
- password-reset
- otp
- api-security
language: en
raw_sha256: 6c79b6db3ae837951fa886190a94110d4e14a240a2455f52318b7f7c4ac3f4d6
text_sha256: 3407582b2e231a5058b5483d9a67b71d70e7d41b9f4fecbe4c902243b52d405d
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Getting Unauthenticated Remote Code Execution On The Logsign Unified Secops Platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-01_getting-unauthenticated-remote-code-execution-on-the-logsign-unified-secops-plat.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, sso, password-reset, otp, api-security
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `6c79b6db3ae837951fa886190a94110d4e14a240a2455f52318b7f7c4ac3f4d6`
- Text SHA256: `3407582b2e231a5058b5483d9a67b71d70e7d41b9f4fecbe4c902243b52d405d`


## Content

---
title: "Getting Unauthenticated Remote Code Execution On The Logsign Unified Secops Platform"
page_title: "Zero Day Initiative — Getting Unauthenticated Remote Code Execution on the Logsign Unified SecOps Platform"
url: "https://www.zerodayinitiative.com/blog/2024/7/1/getting-unauthenticated-remote-code-execution-on-the-logsign-unified-secops-platform"
final_url: "https://www.zerodayinitiative.com/blog/2024/7/1/getting-unauthenticated-remote-code-execution-on-the-logsign-unified-secops-platform"
authors: ["Yulin Sung", "Mehmet INCE (@mdisec)"]
programs: ["Logsign"]
bugs: ["RCE", "Authentication bypass", "OS command injection", "Security code review"]
publication_date: "2024-07-01"
added_date: "2024-07-08"
source: "pentester.land/writeups.json"
original_index: 212
---

# Blog

#  Getting Unauthenticated Remote Code Execution on the Logsign Unified SecOps Platform 

__ July 01, 2024

__ Yulin Sung

Earlier this year, the Trend Micro Zero Day Initiative (ZDI) acquired several vulnerabilities in the Logsign Unified SecOps Platform. These were all reported to the ZDI by Mehmet INCE (@mdisec) from PRODAFT.com. According to Logsign’s [website](https://www.logsign.com/):

_Logsign provides comprehensive_ _visibility and control of your data lake by allowing security analysts to collect and store unlimited data, investigate and detect threats, and respond automatically._

_Logsign offers a single, unified whole security operation platform to alleviate the challenges associated with deploying multiple cybersecurity tools while reducing the costs and complexities that come with managing them individually._

Logsign runs as a Python-based web server. Users have the ability to interact with the web server through a variety of APIs. This blog looks at two separate vulnerabilities that can be combined to achieve remote, unauthenticated code execution on the web server via HTTP requests.

**CVE-2024-5716 – Authentication Bypass**

This vulnerability allows remote attackers to bypass authentication on affected installations of Logsign Unified SecOps Platform. The specific flaw exists within the password reset mechanism. The issue results from the lack of restrictions on excessive password reset attempts. An attacker can leverage this vulnerability to reset a user's password and bypass authentication on the system. 

Anyone who can access TCP port 443 on the web server can request a password reset for a username. Once requested, the server sends a `reset_code`, which is a 6-digit number, to the email address associated with the username. Under normal operations, the user then uses the `reset_code` to reset their password.

The vulnerability is due to there being no rate limiting for requesting a `reset_code`. Since there is a default user named “admin”, an attacker can send multiple requests to reset the admin’s password until they brute force the correct `reset_code`. The attacker can then reset the admin’s password and log in as an administrator.

This vulnerability is located in `/opt/logsign-api/api.py`:

If we send a POST request to `https://LOGSIGNIP/api/settings/forgotpassword`, the server will use this function to handle it. 

\-- On line [1], it gets the `username` parameter from the POST request.  
\-- On line [2], it checks if this user is not `from_ldap`, which is the default configuration. It then sets `reset_code` to `random_int(6)`.

`reset_code` is set to a randomly-selected string of 6 decimal digits. Finally, the server stores the username and `reset_code` pair, and sends `reset_code` to the user's email.

If we send a POST request to `https://LOGSIGN_IP/api/settings/verify_reset_code`, the server will use the above function to handle it. If the username and `reset_code` are correct, the server responds with `verification_code`. Once in possession of this `verification_code`, the attacker will be permitted to reset the password. 

On the line marked [1] in the code snippet above, we find a 3-minute time check. However, this is merely a check against the expiry time of the `reset_code` and not a rate-limiter. An attacker can make numerous attempts at guessing the `reset_code` by calling `verify_reset_code` as many times as possible within the 3-minute window. If the attacker fails within these 3 minutes, they can send another request to `https://LOGSIGNIP/api/settings/forgotpassword` and repeat the brute-force attack until they succeed. Since there are only 1 million possible values for `reset_code`, it is feasible to enumerate within the allotted time a significant proportion of all possible codes. 

Once the attacker has guessed the `reset_code` and successfully obtained the `verification_code`, the attacker can call the `reset_user_password` endpoint, passing the `verification_code`:

When the server receives the correct username and `verification_code`, it allows the attacker to reset the user’s password.

**The Exploit**

The exploit is designed to use as many threads as possible to guess the `reset_code`.

We tested this with Logsign installed on a VMware virtual machine with 8 CPUs and 16GB of memory. Our attacker machine was capable of running 20 threads, which equated to roughly 15,000 attempts within 3 minutes.

**CVE-2024-5717 – Post-Auth Command Injection**

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Logsign Unified SecOps Platform. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed.

The specific flaw results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

This vulnerability resides in `/opt/logsign-api/settings_api.py`:

If a user sends a POST request to `https://LOGSIGNIP/api/settings/demomode`, the server will use this function to handle the request.

\-- On line [1], we see that the user needs to be authenticated to make this request. Hence this a post-authentication vulnerability.

The POST data for this request is as follows:

\-- On line [2], the server takes value of the `list` parameter from the POST data and passes it to `escapeshellarg`. It then takes the result of `escapeshellarg`, encloses it in single-quotes, and adds it as a parameter to a shell command using string concatenation.

To a PHP programmer, it seems that the `escapeshellarg()` function sanitizes the `list` string and makes this code secure. Unfortunately, this is Python, and `escapeshellarg()` is not a built-in function in Python. (Note that Python ships with its [own](https://docs.python.org/3/library/subprocess.html#security-considerations) [mechanisms](https://docs.python.org/3/library/shlex.html#shlex.quote) for sanitizing shell parameters.) Instead, what appears here as `escapeshellarg()`is a custom implementation that can be trivially bypassed.

The `escapeshellarg()` function is defined in `/opt/logsign-commons/python/logsign/commons/helpers.pyc`. Using [python_uncompyle6](https://github.com/rocky/python-uncompyle6) to decompile `helpers.pyc`, we obtain the following Python script:

`escapeshellarg()` only escapes single quote characters! Therefore, we can use any command injection technique as long as it doesn’t rely on single quotes.

This command injection works only once. If you want to subsequently execute another command, you need to first issue a request changing `enable` back to `false`. Then you can send the first request again to perform another command injection.

**The Exploit**

The exploit for this vulnerability is relatively simple. We will use backticks as a means of shell command injection, since this does not require single quotes. We can execute any shell command we wish, provided that our command does not itself contain any single quotes.

**Combining CVE-2024-5716 and CVE-2024-5717**

While the command injection vulnerability is post-auth, we can combine it with the authentication bypass to make it a pre-auth code execution. We use CVE-2024-5716 to reset the admin’s password, then log in with the admin’s credential and execute the command injection.

In this exploit, we use the command injection to get a reverse shell. We use a Python reverse shell, since Logsign installs Python by default.

**Conclusion**

Logsign patched these and other vulnerabilities with [version 6.4.8](https://support.logsign.net/hc/en-us/articles/19316621924754-03-06-2024-Version-6-4-8-Release-Notes). Combining these bugs shows why even post-authentication bugs are worth fixing. When paired with an authentication bypass, a post-auth bug becomes pre-auth relatively quickly. We have seen situations like this at Pwn2Own competitions, in which a vendor believed that the addition of authentication was sufficient for defense.

The authentication bypass vulnerability shown here is a textbook example of the problems that can arise when implementing your own authentication mechanism. (See [Web Application Hacker’s Handbook](https://www.barnesandnoble.com/w/the-web-application-hackers-handbook-dafydd-stuttard/1112113643?ean=9781118175248), Chapter 6, Forgotten Password Functionality, Hack Step 5.) The presence of this rudimentary vulnerability should prompt the vendor to perform a full audit of their software.

I hope you enjoyed this blog and remember not to be daunted by authentication. Until my next post, you can follow the team on [Twitter](https://www.twitter.com/thezdi), [Mastodon](https://infosec.exchange/@thezdi), [LinkedIn](https://www.linkedin.com/company/zerodayinitiative), or [Instagram](https://www.instagram.com/thezdi) for the latest in exploit techniques and security patches.

  * [Logsign](/blog/tag/Logsign)
  * [Research](/blog/tag/Research)
  * [Exploit](/blog/tag/Exploit)
