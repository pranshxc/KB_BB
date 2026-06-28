---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-04_microsoft-remote-desktop-web-access-authentication-timing-attack.md
original_filename: 2021-02-04_microsoft-remote-desktop-web-access-authentication-timing-attack.md
title: Microsoft Remote Desktop Web Access Authentication Timing Attack
category: documents
detected_topics:
- mfa
- mobile-security
- idor
- command-injection
- rate-limit
- automation-abuse
tags:
- imported
- documents
- mfa
- mobile-security
- idor
- command-injection
- rate-limit
- automation-abuse
language: en
raw_sha256: 983be4165a59e6fc54a08b93d1f939a790ccc893b28f8529e95522faa75f4bd5
text_sha256: 3576bfdb907588cf01cf07d8570c3f90c0cb4763d3ff53e55558bba8e562f841
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft Remote Desktop Web Access Authentication Timing Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-04_microsoft-remote-desktop-web-access-authentication-timing-attack.md
- Source Type: markdown
- Detected Topics: mfa, mobile-security, idor, command-injection, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `983be4165a59e6fc54a08b93d1f939a790ccc893b28f8529e95522faa75f4bd5`
- Text SHA256: `3576bfdb907588cf01cf07d8570c3f90c0cb4763d3ff53e55558bba8e562f841`


## Content

---
title: "Microsoft Remote Desktop Web Access Authentication Timing Attack"
page_title: "Metasploit Module: MS Remote Desktop Auth Timing Attack"
url: "https://raxis.com/blog/rd-web-access-vulnerability"
final_url: "https://raxis.com/blog/rd-web-access-vulnerability"
authors: ["Matt Dunn"]
programs: ["Microsoft"]
bugs: ["Timing attack", "Broken authentication"]
publication_date: "2021-02-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3939
---

# New Metasploit Module: Microsoft Remote Desktop Web Access Authentication Timing Attack

[Exploits](https://raxis.com/blog/category/exploits/) [How To](https://raxis.com/blog/category/how-to/)

![The Exploit Blog](https://raxis.com/wp-content/uploads/2025/10/the-exploit-light.svg)

# Penetration Testing Blog

![The rdp_web_login Metasploit Module in Use](https://raxis.com/wp-content/uploads/2021/02/Title-1.webp)

Published on February 25, 2021

[Written by Raxis Research Team](https://raxis.com/author/raxis-sys-admin/)

_**Editor’s note:** Congratulations to Raxis Lead Penetration Tester Matt Dunn for discovering the following exploit and publishing it as a Metasploit Module. This is a tremendous professional milestone for Matt and for Raxis._

> “RD Web Access is susceptible to an anonymous authentication timing attack that can validate usernames within an Active Directory domain. Furthermore, RD Web Access exposes the connected domain name if the Remote Procedure Call (RPC) endpoint is accessible on the target server.”
> 
> Raxis Lead Penetration Tester, Matt Dunn

Microsoft’s Remote Desktop Web Access application (RD Web Access) is a popular web-based remote desktop client. It allows an organizations’ users to access their remote desktop services through a web browser. Recently, I discovered that RD Web Access is susceptible to an anonymous authentication timing attack that can validate usernames within an Active Directory domain. Furthermore, RD Web Access exposes the connected domain name if the Remote Procedure Call (RPC) endpoint is accessible on the target server. An anonymous attacker can exploit this behavior to gather intelligence about an organization’s Active Directory environment and build a list of valid domain users for use in secondary attacks.

###### **Description**

A similar timing-based authentication vulnerability exists for the Outlook Web Application (OWA), that reveals valid usernames based on comparing the response times between authentication attempts using both valid and invalid usernames. Valid usernames are likewise identified by the RD Web Access application by the differences in these response times. An example of an incorrect username authentication attempt with a response time of over 4 seconds can be seen here:

![Long Response Time with Invalid Username Authentication Attempt ](https://raxis.com/wp-content/uploads/2023/05/Picture1-3-1.webp)

However, when authenticating with a valid domain and username pair but an incorrect password, the response time is much shorter (232 milliseconds), as seen here:

![Quick Response Time with Valid Domain and Username Authentication Attempt ](https://raxis.com/wp-content/uploads/2023/05/Picture2-1.webp)

By analyzing how quickly the target server responds to these requests, we can determine that login attempts with valid usernames have significantly shorter response times than login attempts with invalid usernames. The timing difference is significant enough that we can use it to determine username validity.

Note that knowing the target’s Active Directory domain is a prerequisite for this attack. However, if RPC is accessible, retrieving this information from the server is trivial. After issuing a specially crafted NTLM challenge, the encoded response will reveal the target’s Active Directory domain, as seen here:

![Active Directory Domain Revealed in Response ](https://raxis.com/wp-content/uploads/2023/05/Picture3-1.webp)

With the Active Directory domain in hand, we can now fully enumerate the valid usernames for the domain.

###### **Affected Versions**

Raxis has confirmed the following Windows Server versions running the Remote Desktop Web Access application are vulnerable to this attack:

  * Windows Server 2016
  * Windows Server 2019

###### **Metasploit Module**

The original OWA/CAS timing authentication vulnerability was disclosed in 2014, and published tools are available to enumerate usernames and discover the domain from servers hosting the OWA. However, my research found that there were no readily available tools to exploit this vulnerability against a hosted RD Web Access instance. I took this opportunity to create a Metasploit module to automate and streamline the attack workflow. The module provides options for domain discovery, username enumeration, and password login attempts. The full module configuration options are shown below:

![Module Configurations for rdp_web_login Auxiliary Module](https://raxis.com/wp-content/uploads/2023/05/Picture4-1.webp)

After performing the enumeration, the module stores the discovered credentials in the database. An example of this Metasploit module successfully being used to enumerate valid usernames and passwords is shown below:

![rdp_web_login Metasploit Module in Use Against a Test Environment ](https://raxis.com/wp-content/uploads/2023/05/Picture5-1.webp)

The new auxiliary module (_auxiliary/scanner/http/rdp_web_login_) has been approved by Rapid7 and merged to their master branch. The following links provide details to the module, its documentation, and the original pull request:

  * Module Code: <https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/scanner/http/rdp_web_login.py>
  * Module Documentation: <https://github.com/rapid7/metasploit-framework/blob/master/documentation/modules/auxiliary/scanner/http/rdp_web_login.md>
  * Original Module Pull Request: <https://github.com/rapid7/metasploit-framework/pull/14544>
  * Module on Exploit-DB: <https://www.exploit-db.com/exploits/49599>

###### **Remediation**

The remediation for this attack is similar to the remediation for the related OWA authentication timing attack. Raxis recommends any of the following actions to mitigate the threat this attack poses:

  * Protect the Remote Desktop Web Access service from the Internet by requiring a VPN connection to access it.
  * Proxy the Remote Desktop Web Access traffic either through an ISA or Microsoft Federation Service as this mitigates the time-based attack.
  * Enforce Multi-Factor Authentication (MFA) for Remote Desktop Services to prevent unauthorized logins from discovered usernames

###### **Disclosure Timeline**

  * **January 6th, 2021** – Vulnerability reported to Microsoft
  * **January 6th, 2021** – Microsoft begins investigation into report
  * **February 4th, 2021** – Microsoft declines to service this vulnerability
  * **February 24th, 2021** – Metasploit Module accepted and merged by Rapid7

Be sure to check back for updates to this post as the status may change.

![Raxis Research Team](https://raxis.com/wp-content/uploads/2025/01/Raxis-Square@4x-80-bks.png)

### [Raxis Research Team](https://raxis.com/author/raxis-sys-admin/)

The Raxis Research Team is dedicated to staying ahead of the threat landscape. Our experts dig into emerging exploits, uncover hidden vulnerabilities, and develop resources that power our penetration testing engagements. By combining curiosity with technical precision, the team equips Raxis testers with cutting-edge intelligence to simulate real-world attacks and strengthen client defenses.

## About _The Exploit_

The Exploit is written by [Raxis penetration testers](https://raxis.com/blog/category/meet-our-team/). Every post is a technical writeup from someone who runs engagements for a living, with code, command output, and the reasoning behind each step. Topics include exploit research, vulnerability disclosure, tool development, and the offensive techniques showing up in current client work.

### Search The Exploit Blog

Search

### Raxis Discovered Vulnerabilities

[View the CVEs and bugs](https://raxis.com/blog/category/raxis-discovered-vulnerabilities/) that Raxis pentesters have uncovered and submitted.

### Work With the Pentesters Who Wrote This Blog

The engineers behind these posts run real engagements every week. Put them on your network, web apps, APIs, or cloud and see what an attacker would find first.

[Request A Quote](https://raxis.com/contact/) [Schedule Call](https://raxis.com/schedule/)

### Blog Categories

  * [AI](https://raxis.com/blog/category/ai/)
  * [Careers](https://raxis.com/blog/category/careers/)
  * [Choosing a Penetration Testing Company](https://raxis.com/blog/category/choosing-pentest-company/)
  * [Exploits](https://raxis.com/blog/category/exploits/)
  * [How To](https://raxis.com/blog/category/how-to/)
  * [In The News](https://raxis.com/blog/category/in-the-news/)
  * [Injection Attacks](https://raxis.com/blog/category/exploits/injection-attacks/)
  * [Just For Fun](https://raxis.com/blog/category/just-for-fun/)
  * [Meet Our Team](https://raxis.com/blog/category/meet-our-team/)
  * [Mobile Apps](https://raxis.com/blog/category/mobile-apps/)
  * [Networks](https://raxis.com/blog/category/networks/)
  * [Password Cracking](https://raxis.com/blog/category/exploits/passwords-cracking/)
  * [Patching](https://raxis.com/blog/category/patching/)
  * [Penetration Testing](https://raxis.com/blog/category/penetration-testing/)
  * [Phishing](https://raxis.com/blog/category/phishing/)
  * [PTaaS](https://raxis.com/blog/category/ptaas/)
  * [Raxis Discovered Vulnerabilities](https://raxis.com/blog/category/raxis-discovered-vulnerabilities/)
  * [Raxis In The Community](https://raxis.com/blog/category/raxis-in-the-community/)
  * [Red Team](https://raxis.com/blog/category/red-team/)
  * [Security Recommendations](https://raxis.com/blog/category/security-recommendations/)
  * [Social Engineering](https://raxis.com/blog/category/social-engineering/)
  * [Tips For Everyone](https://raxis.com/blog/category/tips-for-everyone/)
  * [Web Apps](https://raxis.com/blog/category/web-apps/)
  * [What People Are Saying](https://raxis.com/blog/category/what-people-are-saying/)
  * [Wireless](https://raxis.com/blog/category/wireless/)

### Join Our Newsletter

Name(Required)

First Last

Email(Required)

Newsletter(Required)

Do you wish to join our newsletter? We send out emails once a month that cover the latest in cybersecurity news. We do not sell your information to other parties. 

Yes! Please send me Popped Culture, the Raxis Newsletter.
