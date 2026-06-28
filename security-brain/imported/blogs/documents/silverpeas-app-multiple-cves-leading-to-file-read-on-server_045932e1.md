---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-12_silverpeas-app-multiple-cves-leading-to-file-read-on-server.md
original_filename: 2023-12-12_silverpeas-app-multiple-cves-leading-to-file-read-on-server.md
title: 'Silverpeas App: Multiple CVEs leading to File Read on Server'
category: documents
detected_topics:
- access-control
- xss
- sqli
- command-injection
- otp
- csrf
tags:
- imported
- documents
- access-control
- xss
- sqli
- command-injection
- otp
- csrf
language: en
raw_sha256: 045932e1dbf4b0f15dfa088503d0e5b6774ae5acab423ac06ea21bfd34228d62
text_sha256: de3074e3ba5836b6fcacb0dcc89f17fdab01f62eadf39771067c81f3682f00cb
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# Silverpeas App: Multiple CVEs leading to File Read on Server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-12_silverpeas-app-multiple-cves-leading-to-file-read-on-server.md
- Source Type: markdown
- Detected Topics: access-control, xss, sqli, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `045932e1dbf4b0f15dfa088503d0e5b6774ae5acab423ac06ea21bfd34228d62`
- Text SHA256: `de3074e3ba5836b6fcacb0dcc89f17fdab01f62eadf39771067c81f3682f00cb`


## Content

---
title: "Silverpeas App: Multiple CVEs leading to File Read on Server"
page_title: "Silverpeas App: Multiple CVEs leading to File Read on Server - Rhino Security Labs"
url: "https://rhinosecuritylabs.com/research/silverpeas-file-read-cves/"
final_url: "https://rhinosecuritylabs.com/research/silverpeas-file-read-cves/"
authors: ["Tyler Ramsbey (@Tyler_Ramsbey)"]
programs: ["Silverpeas"]
bugs: ["Stored XSS", "Arbitrary file read"]
publication_date: "2023-12-12"
added_date: "2024-01-02"
source: "pentester.land/writeups.json"
original_index: 636
---

[ Technical Blog ](https://rhinosecuritylabs.com/blog-technical)

____

[Research](https://rhinosecuritylabs.com/research/)

![](https://rhinosecuritylabs.com/wp-content/uploads/2018/10/Pasted_image_at_2018-10-28__5_37_PM-1140x400.png)

# Silverpeas App: Multiple CVEs leading to File Read on Server

Tyler Ramsbey

## Silverpeas Vulnerability Overview

## Affected Product Summary

During research on the Silverpeas Core application, the Rhino research team identified 8 new CVEs over the course of 2 weeks. The most severe of these is CVE-2023-47324, a Stored Cross-Site Scripting (XSS) vulnerability affecting the messaging application. This can be used for privilege escalation, providing an adversary with full administrative access. The adversary can then use the Silverpeas Crawler application to perform a full file read on the backend server. 

The public disclosure details for each CVE can be found below. 

  1. [CVE-2023-47320: Broken Access Control Leading to Denial-of-Service ](https://github.com/RhinoSecurityLabs/CVEs/tree/master/CVE-2023-47320)
  2. [CVE-2023-47321: Broken Access Control Allows Attacker to Access Portlet Deployer](https://github.com/RhinoSecurityLabs/CVEs/tree/master/CVE-2023-47321)
  3. [CVE-2023-47322: CSRF Leading to Privilege Escalation](https://github.com/RhinoSecurityLabs/CVEs/tree/master/CVE-2023-47322)
  4. [CVE-2023-47323: Broken Access Control Allows Attacker to Read All Messages ](https://github.com/RhinoSecurityLabs/CVEs/tree/master/CVE-2023-47323)
  5. [CVE-2023-47324: Stored XSS in Messaging Feature](https://github.com/RhinoSecurityLabs/CVEs/tree/master/CVE-2023-47324)
  6. [CVE-2023-47325: Broken Access Control on “Bin” Allows Modification by Attacker](https://github.com/RhinoSecurityLabs/CVEs/tree/master/CVE-2023-47325)
  7. [CVE-2023-47326: CSRF Leading to Domain Creation](https://github.com/RhinoSecurityLabs/CVEs/tree/master/CVE-2023-47326)
  8. [CVE-2023-47327: Broken Access Control Allows Attacker to Create Spaces](https://github.com/RhinoSecurityLabs/CVEs/tree/master/CVE-2023-47327)

Vendor: Silverpeas 

Product: Silverpeas Core 

Confirmed Vulnerable Version: 6.3.1 

Fixed Version: 6.3.2 

Product Link: [https://www.silverpeas.org/](https://www.silverpeas.org/)

Confirmed Vulnerable Platforms: Linux 

## What is Silverpeas Core? 

Silverpeas Core is an open-source digital workplace platform designed to facilitate collaboration and communication within organizations. Silverpeas Core includes the essential features and functionalities that serve as the backbone for the application – including user management, authentication, access control, content management, and messaging functionality. It can be installed on either Windows or Linux, but our research was exclusively on the Linux application. 

The official docker image has over one million downloads and is actively used by [government, industrial, and community organizations](https://www.silverpeas.com/clients/).

## CVE-2023-47324: Stored XSS in Messaging Feature 

A primary focus of Silverpeas is enabling collaboration between internal and external teams. To facilitate this, a messaging feature is included in the application. Silverpeas makes it convenient for any user to send a message to the administrators by including a “Write to administrators” option on the user’s personal workspace after logging into the application. 

While testing this functionality, we discovered Silverpeas checks for Cross-Site Scripting by filtering out <script> tags in messages. This check can be bypassed by performing XSS without using <script> tags. We first confirmed this by sending a basic “alert” when the message was view by the administrator: 

When this message was viewed by the administrator, the Javascript was successfully executed in their browser. 

## Weaponizing XSS: Granting Attacker Additional Privileges 

Although generating an alert demonstrates XSS, we wanted to weaponize the vulnerability to show how it could be used by an adversary. By analyzing the administrative request to elevate permissions, we discovered the following payload will successfully execute Javascript that elevates the adversary’s permissions: 
  
  
  <html><body onload="document.forms[0].submit();"><form action="http://localhost:8080/silverpeas/RjobDomainPeas/jsp/userModify" method="GET"><input type="hidden" name="Iduser" value="[userID]" /><input type="hidden" name="userLastName" value="[userLastName]" /><input type="hidden" name="userAccessLevel" value="ADMINISTRATOR" /><input type="hidden" name="X-STKN" value="[userSTKNToken]" /></form></body></html>

There are three pieces of information related to our _own_ user we need for a viable attack: 

  1. The ID of our user. 
  2. The last name of our user. 
  3. The X-STKN of our user (the X-STKN is the Silverpeas Core CSRF token). 

We would already know the last name of our user and the other information can be retrieved by sending a message to ourselves and intercepting the POST request with Burp Suite: 

With this information and the previous payload, an adversary can send a message to the administrators with the Javascript in the “content” field of the request. As soon as the malicious message is viewed by an administrator, the adversary will gain full administrative rights to the application. 

## File Read Through New Administrative Access

Now that we have administrative access to the application, we can abuse a feature called “Silvercrawler.” Silvercrawl allows administrators to host files for other users to access. The Silvercrawler runs as the “root” user on the backend Linux server, so it can view sensitive files such as /etc/shadow.

Once Silvercrawler is enabled, we can specify the Root directory. To perform a full file read and enumerate the entire system, we can set the root directory as “/”. After this is configured, we can click the “Ok” button to save the application. 

By navigating to the new path we created, we now have full access to the underlying file system. From here an adversary can search for credentials, read environmental variables, or access configuration files. 

## Conclusion: Showcasing XSS Impact

## Disclosure Timeline 

Cross-Site Scripting is often downplayed in security discussions because the impact is often misunderstood, and PoCs usually consist of a simple alert payload. In this attack walkthrough, we show how an XSS payload – directed at an app administrator – allows an attacker to gain additional privileges, including File Read on the underlying server.

This walkthrough is an example of one of the eight CVEs we found during our research. You can find the details for the other CVEs in our Github: [https://github.com/RhinoSecurityLabs/CVEs](https://github.com/RhinoSecurityLabs/CVEs)

We want to say thank you to the Silverpeas team for working with us and getting these patched. They were quick to respond to our reports and immediately began working on remediating each of the CVEs we discovered in the platform. 

As always, feel free to follow us on Twitter and join our Discord server for more releases and blog posts.  
  
Twitter: [https://twitter.com/rhinosecurity](https://twitter.com/rhinosecurity)

Discord: [https://discord.gg/TUuH26G5](https://discord.gg/TUuH26G5)

YouTube: [https://youtube.com/@TylerRamsbey](https://youtube.com/@TylerRamsbey)

10/20/2023 | Issues reported to Silverpeas  
---|---  
10/23/2023 | Report acknowledged by Silverpeas  
11/24/2023 | Silverpeas release 6.3.2, fixing the issues  
12/12/2023 | CVEs are disclosed publicly  
  
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
