---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-05_multiple-vulnerabilities-in-extreme-networks-extremexos.md
original_filename: 2023-12-05_multiple-vulnerabilities-in-extreme-networks-extremexos.md
title: Multiple Vulnerabilities In Extreme Networks ExtremeXOS
category: documents
detected_topics:
- command-injection
- csrf
- access-control
- ssrf
- api-security
- jwt
tags:
- imported
- documents
- command-injection
- csrf
- access-control
- ssrf
- api-security
- jwt
language: en
raw_sha256: 0894f00b9978bbdda65b4e4d45bcc7d21af504b9feb37b30903976b0dfe1f9cc
text_sha256: a77163722e339b69654641e9f8b399bb80aaae60368778f03c2cc4426e4208a4
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple Vulnerabilities In Extreme Networks ExtremeXOS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-05_multiple-vulnerabilities-in-extreme-networks-extremexos.md
- Source Type: markdown
- Detected Topics: command-injection, csrf, access-control, ssrf, api-security, jwt
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `0894f00b9978bbdda65b4e4d45bcc7d21af504b9feb37b30903976b0dfe1f9cc`
- Text SHA256: `a77163722e339b69654641e9f8b399bb80aaae60368778f03c2cc4426e4208a4`


## Content

---
title: "Multiple Vulnerabilities In Extreme Networks ExtremeXOS"
page_title: "Multiple Vulnerabilities In Extreme Networks ExtremeXOS - Rhino Security Labs"
url: "https://rhinosecuritylabs.com/research/extreme-networks-extremexos-vulnerabilities/"
final_url: "https://rhinosecuritylabs.com/research/extreme-networks-extremexos-vulnerabilities/"
authors: ["David Yesland (@daveysec)"]
programs: ["Extreme Networks"]
bugs: ["Arbitrary file read", "Arbitrary file write", "SSRF", "RCE", "Privilege escalation", "Local Privilege Escalation", "CSRF", "Security code review"]
publication_date: "2023-12-05"
added_date: "2023-12-26"
source: "pentester.land/writeups.json"
original_index: 652
---

[ Technical Blog ](https://rhinosecuritylabs.com/blog-technical)

____

[Research](https://rhinosecuritylabs.com/research/)

![](https://rhinosecuritylabs.com/wp-content/uploads/2021/03/blog-background-1140x400.png)

# Multiple Vulnerabilities In Extreme Networks ExtremeXOS

David Yesland

## Introduction

## Affected Product

During an external network pentest, we came across a switch administration interface running ExtremeNetworks’ Extreme Operating System (EXOS). This is a network operating system designed to manage ExtremeNetworks’ wide range of Ethernet switches. 

There was a virtual machine (VM) of EXOS available to download, so we downloaded the latest version to see if there were any vulnerabilities that could be exploited to gain access to the device. 

At the time of these findings there were over 1000 devices exposed to the internet running the vulnerable EXOS versions, determined using a Shodan search.

**Vendor:** Extreme Networks

**Product:** Switch Engine (EXOS)

**Advisories:**

  * CVE-2023-43121: [Unauthenticated root file read disclosing password hashes for the device](https://extreme-networks.my.site.com/ExtrArticleDetail?an=000114376)
  * CVE-2023-43120: [Privilege escalation from read-only user to read-write admin](https://extreme-networks.my.site.com/ExtrArticleDetail?an=000114377)
  * CVE-2023-43118: [Cross-Site Request Forgery to Remote Code Execution](https://extreme-networks.my.site.com/ExtrArticleDetail?an=000114379)
  * CVE-2023-43119: [Arbitrary file write as root via read-only user](https://extreme-networks.my.site.com/ExtrArticleDetail?an=000114378)

**Patched Versions:**

  * Fixed in 22.7.5.1-patch1-6 or later.
  * Fixed in 31.3.100.20 or later.
  * Fixed in 31.7.2.28-patch1-35 or later.
  * Fixed in 32.5.1.5-patch1-5 or later.

## Unauthenticated File Read (CVE-2023-43121)

First, the VM of EXOS was downloaded and imported. Although EXOS does not intentionally provide root shell access on the device, it was possible to open the file system from the virtual disk that was created, allowing analysis of the full file system. The first goal was to find the files that handled the main web application, this application is referred to as Chalet in EXOS. Locating these files was accomplished by grepping for path names that were shown when navigating to Chalet in a browser.

The Chalet application is written in Python using the CherryPy web framework. The Python files related to the application were compiled into pyc files but could all be decompiled to their original Python code using Uncompyle6. Knowing CherryPy is in use makes it fairly easy to discover a number of the routes for the application by searching for the string “@cherrypy.expose” which is a decorator to tell CherryPy to expose a particular method for an endpoint.

Once a mapping of a number of endpoints was obtained, we could start looking at the endpoints which were exposed with no authentication and look for vulnerabilities in those. This quickly led to finding the /terminal endpoint, which is a web console terminal that the device exposes in the web UI. It uses websockets to send and receive commands to the device as though you were connected to its console. Access to the terminal still requires valid credentials to use it.

The /terminal endpoint exposes a method that is used to load the static files for the application. This method contained a path traversal vulnerability allowing users to read arbitrary files on the device.

As you can see, the functions are exposed at the index (/) and “/_static” paths of the “/terminal” endpoint, and if the path contains a “filename” parameter the value will be concatenated with the path and the contents of the file path will be read and returned back to the user. Since the application runs as root we can read any file on the system. This includes the default XML configuration file used by EXOS, which contains the hashes for all the users on the system and all other configuration data of EXOS.

EXOS has two different application user level permissions, a read-only user and an admin user with read-write permissions. If not installed using “Enhanced Security Mode,” EXOS by default contains a read-only user and admin user with documented default passwords. 

If the default users are not enabled, once we have the hashes for the users it may be possible to crack them and gain access to the device as one of those users. In older devices the hashes are stored as MD5Crypt and in newer devices the hashes are SHA-256.

## Privilege Escalation from ‘Read-Only’ User to Admin (CVE-2023-43120) 

After discovering a method of initial access, we turned our attention to what you could do once authenticated as a read-only user, with the main question being whether we could go from a read-only user to admin, or better yet, root.

Focusing on this privilege escalation goal, we looked at the authentication and authorization features of the app. This revealed an endpoint (/auth/token) which, if valid credentials were provided in a GET request, would return a JWT for that user. Simple enough, but this does not give any additional permissions. 

We discovered that the code for the /auth/token endpoint also contained a bypass for localhost which if the source IP was coming from localhost (127.0.0.1) it would treat it as a privileged request and issue an admin token. This is intended for interprocess communication, allowing the application to issue internal admin requests. 

You can see the /auth/token endpoint is exposed and requests are handled by the exos.httpd.authentication.Auth() class, which contains the localhost bypass code:

This meant that if a Server-Side Request Forgery (SSRF) vulnerability was found it would be possible to obtain an admin JWT and gain administrator privileges. So the next goal was to find a way to force the application to make an HTTP request and read it.

### Finding SSRF For Privilege Escalation 

As mentioned, the application exposes a web console which allows you to interact with the device as though you have direct console access to it. The EXOS console exposes a number of tools to the user to perform diagnostics and configuration on the device.

As a user with read-only permissions you only have access to a subset of these tools and should not be able to perform write actions. But one of the tools you do have access to is a limited telnet command. The telnet command is enough to forge an HTTP request to localhost. Abusing this allows you to issue a basic HTTP request to localhost to obtain an admin JWT token and escalate from read-only user to a read-write admin user.

Using the issued JWT token you can make privileged calls as an admin to the web APIs and execute commands on the device.

## Admin to Root Privilege Escalation (No CVE)

_Important Note: At this stage of the research we pursued further escalation from Admin to root user to gain full control of the device.__In response to this disclosure The vendor does not consider this a vulnerability as it’s expected the Admin user has full control of the device.__While we decided to include the following section for those interested, there is no corresponding CVE for this section._

Some execution of device management commands are done the command line utility “exsh,” which handles execution of commands with the same permissions as the authenticated user. This utility is called in an insecure way from the API endpoint /jsonrpc, which can be used to execute EXOS console commands as root via the web API. 

When a “cli” method request is sent to the /jsonrpc endpoint, the backend code calls the exsh utility with some static flags and concatenates the “params” JSON parameter with the command. This leads to argument injection, where injecting the -d (debug) flag forces the command to be executed with root permissions.

Looking at the help command for exsh you can see that it allows a -d flag, which is only allowed when it is executed as root. Since calling the exsh command via the /jsonrpc endpoint is executed by the application running as root, this requirement is met and forces exsh to execute with root privileges. We can now abuse the built in EXOS command “run script shell <some command>” command and gain command execution as root using this injection.

You can see trying to execute a command that requires root permissions fails.

Adding the injected -d flag succeeds with no error output, confirming the command ran with root privileges.

## Additional CVEs Discovered During Testing

### CSRF to RCE (CVE-2023-43118)

The Chalet application fails to protect requests from Cross-Site Request Forgery across the entire application. There are no Anti-CSRF tokens used, the cookies’ SameSite flag is set to “None” and there are insecure CORS headers set that allow arbitrary requests cross-domain.

These vulnerabilities make any arbitrary request (including to sensitive endpoints) to be susceptible to CSRF, where an authenticated user can unintentionally make the request by viewing a malicious page.

In short, an attacker can get code execution on the device by getting an authenticated admin user to view an attacker-controlled page.

### Arbitrary Root File Write (CVE-2023-43119)

Similar to how telnet was abused to make an internal HTTP request, telnet can also be abused to communicate with a local Redis instance running on the device. Since the redis instance has no authentication and runs as root, it is possible to abuse it to write files as root using a well known method (<https://book.hacktricks.xyz/network-services-pentesting/6379-pentesting-redis#php-webshell>). This can be done with only read-only user permissions on the device.

## Conclusion

## Disclosure Timeline

When installing a new EXOS device, we  _highly_ recommend using the “Enhanced Security Mode”, which improves configuration security and requires user-defined (non-default) passwords.

Moreover, it is an essential security measure to change the default passwords of all deployed devices on your network, irrespective of their perceived criticality. Often, these devices with unchanged default passwords can serve as convenient entry points for potential attackers. Lastly, it’s recommended to avoid exposing management interfaces to the internet. These interfaces usually have privileged functionality, and exposing them unnecessarily broadens the attack surface.

Thank you to Extreme Networks for working with us in a timely manner to fix these issues.

We have added proof-of-concepts to our [CVE GitHub repository](https://github.com/RhinoSecurityLabs/CVEs#rhino-cve-proof-of-concept-exploits) that demonstrate these vulnerabilities. As always, feel free to follow us on Twitter for more releases and blog posts [@RhinoSecurity](https://twitter.com/RhinoSecurity) and [@daveysec](https://twitter.com/daveysec) and also chat with us on Discord: [https://discord.gg/8vFE7ucx9W](https://discord.gg/8vFE7ucx9W).

7/06/2023 | Issues reported to Extreme Networks  
---|---  
7/14/2023 | Receipt of disclosures requested by Rhino  
7/14/2023 | Receipt of disclosure acknowledged by Extreme Networks  
8/17/2023 | 45 day extension requested and agreed by Rhino  
9/28/2023 | Extreme Networks notifies Rhino of requested and issued CVEs  
10/19/2023 | Rhino confirms with Extreme Networks that they are ready for disclosure  
  
## Related Resources

### Referral Beware, Your Rewards are Mine (Part 1)

[](https://rhinosecuritylabs.com/research/referral-beware-your-rewards-are-mine-part-1/)

### Multiple CVEs in Infoblox NetMRI: RCE, Auth Bypass, SQLi, and File Read Vulnerabilities 

[](https://rhinosecuritylabs.com/research/infoblox-multiple-cves/)

### CVE-2025-26147: Authenticated RCE In Denodo Scheduler 

[](https://rhinosecuritylabs.com/research/cve-2025-26147-authenticated-rce-in-denodo/)

## Interested in more information?

20603 

[ Contact Us Today  __ ](https://rhinosecuritylabs.com/contact/)
