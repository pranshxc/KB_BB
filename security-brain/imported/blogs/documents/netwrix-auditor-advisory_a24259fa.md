---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-13_netwrix-auditor-advisory.md
original_filename: 2022-07-13_netwrix-auditor-advisory.md
title: Netwrix Auditor Advisory
category: documents
detected_topics:
- command-injection
- information-disclosure
- mobile-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- mobile-security
language: en
raw_sha256: a24259fa3484ceab2ed7d71cefeada2d8e16df8461e73573cdf9f73f2e5e4ed4
text_sha256: 8506ababe1098fef9159020b339749e45ccc47f648e58c3dea0878bda6724d37
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Netwrix Auditor Advisory

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-13_netwrix-auditor-advisory.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `a24259fa3484ceab2ed7d71cefeada2d8e16df8461e73573cdf9f73f2e5e4ed4`
- Text SHA256: `8506ababe1098fef9159020b339749e45ccc47f648e58c3dea0878bda6724d37`


## Content

---
title: "Netwrix Auditor Advisory"
page_title: "Netwrix Auditor Application Critical Vulnerability… | Bishop Fox"
url: "https://bishopfox.com/blog/netwrix-auditor-advisory"
final_url: "https://bishopfox.com/blog/netwrix-auditor-advisory"
authors: ["Jordan Parkin"]
programs: ["Netwrix"]
bugs: ["Insecure deserialization"]
publication_date: "2022-07-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2461
---

Share

[ ](https://www.facebook.com/share.php?u=https://bishopfox.com/blog/netwrix-auditor-advisory&amp;utm_medium=social&amp;utm_source=facebook) [ ](https://twitter.com/intent/tweet?url=https://bishopfox.com/blog/netwrix-auditor-advisory&utm_medium=social&utm_source=twitter&source=tweetbutton&text=) [ ](http://www.linkedin.com/shareArticle?mini=true&url=https://bishopfox.com/blog/netwrix-auditor-advisory&utm_medium=social&utm_source=linkedin) [ ](/feeds/advisories.rss)

## NETWRIX AUDITOR ADVISORY SUMMARY

The following document describes identified vulnerabilities in the Netwrix Auditor application in supported versions prior to 10.5.

### Product Vendor

Netwrix

### Product Description

Auditor is IT auditing software used to track assets within an organization. The product’s official website is <https://www.netwrix.com/auditor.html>. The latest version of the application is 10.5, released on June 6, 2022.

### Vulnerabilities List

1 vulnerability was identified within the Netwrix Auditor application:

  * Insecure Object Deserialization

These vulnerabilities are described in the following sections.

### Affected Version

All supported versions prior to 10.5

### Summary of Findings

The Netwrix Auditor application is affected by an insecure object deserialization issue that allows an attacker to execute arbitrary code with the privileges of the affected service. This issue is caused by an unsecured .NET remoting port accessible on TCP port 9004.

### Impact

An attacker can use this issue to achieve arbitrary code execution on servers running Netwrix Auditor. Since this service is typically executed with extensive privileges in an Active Directory environment, the attacker would likely be able to compromise the Active Directory domain.

### Solution

Update to version 10.5

### 

## Insecure Object Deserialization

Netwrix Auditor is vulnerable to an insecure object deserialization issue that is caused by an unsecured .NET remoting service. An attacker can submit arbitrary objects to the application through this service to achieve remote code execution on Netwrix Auditor servers.

### Vulnerability Details

CVE ID:  __CVE-2022-31199

Vulnerability Type: Insecure Object Deserialization

Access Vector: ☒ Remote, ☐ Local, ☐ Physical, ☐ Context dependent, ☐ Other (if other, please specify)

Impact: ☒ Code execution, ☐ Denial of service, ☒ Escalation of privileges, ☐ Information disclosure, ☐ Other (if other, please specify)

Security Risk: ☒ Critical, ☐ High, ☐ Medium, ☐ Low

Vulnerability: CWE-502

The Netwrix Auditor application is affected by an insecure object deserialization issue that allows an attacker to execute arbitrary code with the privileges of the affected service. In a typical real-world scenario, Netwrix Auditor services would be running with a highly privileged account, which could lead to full compromise of the Active Directory environment.

This issue was discovered by performing a TCP port scan of a Netwrix Auditor server using the tool nmap. As the following output demonstrates, the Netwrix server had a .NET remoting service available on TCP port 9004:

![Screenshot of the TCP port scan of a Netwrix Auditor Server](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Netrix-9.96.PNG)

**FIGURE 1** -Scanning for services on Netwrix server

The `netstat` and `tasklist` commands were used on the Netwrix server to find out which process was exposing the .NET remoting service:

![Screenshot of code showing the identification of the .NET remoting service.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Netrix-9.96-Image-2.PNG)

**FIGURE 2** – Identifying the .NET remoting service

Analyzing the .NET remoting service revealed that it could be accessed with the `UAVRServer` endpoint. The `ysoserial.net` tool was used to generate a serialized object designed to execute the command `whoami` on the server under the context of `UAVRServer.exe`:

![screenshot of code showing how The ysoserial.net tool was used to generate a serialized object designed to execute the command whoami](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Netrix-9.96-Image-3.PNG)

**FIGURE 3** – Generating a serialized object

The `ExploitRemotingService` tool was then used to send the serialized object to the `UAVRServer` service over .NET remoting. The resulting exception was an indicator that the payload was executed successfully:

![Screenshot of code showing the result and how an exception was an indicator that the payload was executed successfully.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Netrix-Image-4.PNG)

**FIGURE 4** – Sending the malicious object to the `UAVRServer` service

Logging onto the server and inspecting the contents of C:\temp\out.txt showed that the command was executed successfully:

![Screenshot showing how the code was executed through the .NET remoting service.](https://assets.bishopfox.com/prod-1437/Images/channels/blog/Content/Netrix-Image-5.PNG)

**FIGURE 5** – Code executed through the .NET remoting service

Since the command was executed with `NT AUTHORITY\`system privileges, exploiting this issue would allow an attacker to fully compromise the Netwrix server.

  

* * *

![Default fox headshot purple](https://assets.bishopfox.com/prod-1437/Images/headshots/BanksyFox_exploder2.png)

By Jordan Parkin 

Senior Security Consultant

Jordan Parkin (OSCP, OSWP) is a Senior Security Consultant for Bishop Fox, where he focuses on web and mobile application assessments, network penetration testing, and embedded systems security. Jordan has worked for Fortune 500 companies across a wide range of industries, including finance, healthcare, technology, and manufacturing. Jordan is responsible for discovering [CVE-2022-31199](https://bishopfox.com/blog/netwrix-auditor-advisory), a critical severity vulnerability in the Netwrix Auditor application in supported versions prior to 10.5.

[ More by Jordan Parkin  ](https://bishopfox.com/authors/jordan-parkin)

[ ](https://www.linkedin.com/in/jordan-parkin-02950825/)

![](/static/assets/images/backgrounds/lander-header-bg-black-lines.svg)

Subscribe to our blog

Be first to learn about latest tools, advisories, and findings.

Thank You! You have been subscribed.
