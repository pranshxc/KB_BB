---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-24_atlassian-jira-align-version-101074-advisory.md
original_filename: 2022-10-24_atlassian-jira-align-version-101074-advisory.md
title: Atlassian Jira Align, Version 10.107.4 Advisory
category: documents
detected_topics:
- access-control
- ssrf
- xss
- cloud-security
- command-injection
- automation-abuse
tags:
- imported
- documents
- access-control
- ssrf
- xss
- cloud-security
- command-injection
- automation-abuse
language: en
raw_sha256: 28c4ab521edf6f4317f8373a7dd5c088aa0b8284a7d64975aa99b07dd93cf244
text_sha256: 6292817ee484787434527cae8ccad49cdbbb866a87a4ceca3e06a3645de244ca
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Atlassian Jira Align, Version 10.107.4 Advisory

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-24_atlassian-jira-align-version-101074-advisory.md
- Source Type: markdown
- Detected Topics: access-control, ssrf, xss, cloud-security, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `28c4ab521edf6f4317f8373a7dd5c088aa0b8284a7d64975aa99b07dd93cf244`
- Text SHA256: `6292817ee484787434527cae8ccad49cdbbb866a87a4ceca3e06a3645de244ca`


## Content

---
title: "Atlassian Jira Align, Version 10.107.4 Advisory"
page_title: "Advisory: Atlassian Jira Align Application, Version… | Bishop Fox"
url: "https://bishopfox.com/blog/jira-align-advisory"
final_url: "https://bishopfox.com/blog/jira-align-advisory"
authors: ["Jacob Shafer (@fibbot)"]
programs: ["Atlassian"]
bugs: ["SSRF", "Broken Access Control", "Privilege escalation"]
publication_date: "2022-10-24"
added_date: "2022-10-25"
source: "pentester.land/writeups.json"
original_index: 2002
---

Share

[ ](https://www.facebook.com/share.php?u=https://bishopfox.com/blog/jira-align-advisory&amp;utm_medium=social&amp;utm_source=facebook) [ ](https://twitter.com/intent/tweet?url=https://bishopfox.com/blog/jira-align-advisory&utm_medium=social&utm_source=twitter&source=tweetbutton&text=) [ ](http://www.linkedin.com/shareArticle?mini=true&url=https://bishopfox.com/blog/jira-align-advisory&utm_medium=social&utm_source=linkedin) [ ](/feeds/advisories.rss)

## Atlassian Jira Align — VERSION 10.107.4 — ADVISORY SUMMARY

The following document describes identified vulnerabilities in the Jira Align application Version 10.107.4.

### Product Vendor

Atlassian

### Product Description

Jira Align is an Atlassian software as a service (SaaS) program that allows users to have a scalable Jira solution in the cloud. The project’s official website is <https://www.atlassian.com/software/jira/align>. The latest version of the application is 10.109.3 and was released on July 22, 2022.

### Vulnerabilities List

2 vulnerabilities were identified within the Jira Align application:

  * Server-side Request Forgery (SSRF) 
  * Insufficient Authorization Controls

These vulnerabilities are described in the following sections.

### Affected Version

Version 10.107.4

### Summary of Findings

The first vulnerability is a SSRF in the "Connectors" settings that allows a user to retrieve the AWS credentials of the Atlassian service account that provisioned the Jira Align instance. Additionally, there was a case of Insufficient Authorization Controls in the "People" permission that allows any user with this permission to modify their own role to that of Super Admin. 

### Impact

For the SSRF, an attacker could exploit this issue to retrieve the AWS credentials of the Atlassian service account that provisioned access to the Jira Align instance. In the case of Insufficient Authorization Controls, a user who exploits this issue could elevate their role to Super Admin, the highest role provisioned in Jira Align for an end user. With access to Super Admin permissions, a malicious user could gain access to all data in Jira Align, modify user or account settings, and modify any security control for the Jira Align instance. 

### Solution

Update to version 10.109.3 or newer.

## Vulnerabilities

### Server-Side Request Forgery (SSRF)

The Jira Align application was affected by a Server-side Request Forgery vulnerability that could allow an attacker to retrieve the AWS credentials of the service account that deployed the instance of Jira Align. Due to each instance of Jira Align being provisioned by Atlassian, this attack could potentially be used to gain access to the Atlassian cloud infrastructure by a consumer of Jira Align.

### Vulnerability Details

CVE ID: CVE-2022-36802

Vulnerability Type: Other (SSRF)

Access Vector: ☒ Remote, ☐ Local, ☐ Physical, ☐ Context dependent, ☐ Other (if other, please specify)

Impact: ☐ Code execution, ☐ Denial of service, ☐ Escalation of privileges, ☒ Information disclosure, ☐ Other (if other, please specify)

Security Risk: ☐ Critical, ☒ High, ☐ Medium, ☐ Low

Vulnerability: CWE-918

The Jira Align `ManageJiraConnectors` API that manages external Jira connections to the application is vulnerable to SSRF. An attacker can exploit this issue to return the AWS credentials of the service account that deployed the instance of Jira Align.

The identified endpoint required a user-supplied parameter called `txtAPIURL`, which was a URL value that pointed to the desired Jira API location. Jira Align automatically appended the standard `API /rest/api/2/` to the URL server side but could be bypassed by adding a single # symbol to the end of the URL, which would allow an attacker to specify any URL for the Jira connector.

To exploit this, an attacker could specify the AWS metadata endpoint in the `txtAPIURL` parameter, as shown below:**  
**

**Request:**
  
  
  POST /ManageJiraConnectors HTTP/1.1
  Host: amertrial317.jiraalign.com
  …omitted for brevity…
  cmbJiraConnectorID=1&txtURL1=https%3A%2F%2Fone-atlas-demo-
  1.atlassian.net%2Fbrowse%2F%7Bexternal%7D&txtConnectorName1=Partner+Connector&txtConnectorAdmin1=1190&
  txtAPIURL1=http%3A%2F%2F169.254.169.254%2Flatest%2Fmeta-data%2Fiam%2Fsecurity-
  credentials%2FLP-USE2-MULTI-2-CON-B6-AZ2-InstanceRole-1QX59D6VM44H6%23&ddlAuthType1=0&txtAPIEMAN1=&txtAPIDROWSSAP1=&txtOACK1=&txtOAPuK1=&btnUpdateConnectors=Save&__STATE=W5DLrMbpCpgsEfqmIeYAizIRcWv1khjXXchwHRr6%2Fww%3D
  

**Response:**
  
  
  HTTP/1.1 302 Found
  Date: Thu, 26 May 2022 21:34:34 GMT
  Content-Type: text/html; Charset=utf-8
  Connection: close
  Location: ManageJiraConnectors?i=1
  …omitted for brevity…
  Server: cloudflare
  Content-Length: 145
  <head><title>Object moved</title></head>
  <body><h1>Object Moved</h1>
  </a>.</body>

After activating the connector, Jira Align reached out to the Jira API URL and returned the full body of the response to the URL in the Jira Change Log:  
  

![AWS credentials of user LP-USE2-MULTI-2-CON-B6-AZ2-InstanceRole-1QX59D6VM44H6 returned in Jira Change Log](https://s3.us-east-2.amazonaws.com/s3.bishopfox.com/prod-1437/Images/channels/blog/Content/Bishop-Fox-Image-Jira-Align.png?1665444914187?1665445016882#asset:324181)

**FIGURE 1** \- AWS credentials of user LP-USE2-MULTI-2-CON-B6-AZ2-InstanceRole-1QX59D6VM44H6 returned in Jira Change Log

The impact to Atlassian's AWS infrastructure with the `LP-USE2-MULTI-2-CON-B6-AZ2-InstanceRole-1QX59D6VM44H6` user could not be determined due to restrictions in the agreement between Atlassian and Bishop Fox's client. It was also not possible to establish whether further access could be gained to the Atlassian infrastructure through privilege escalation or lateral movement with the account.

## Insufficient Authorization Controls

The Jira Align application was affected by an insufficient authorization control vulnerability that allowed users provisioned with the `People` role permission to elevate any user’s role, including their own, to `Super Admin`. Due to Jira Align being tailored to the end user’s needs, the exact role this permission is applied to varies. In the sandbox environment that was provisioned for testing purposes, this permission was added to the `Program Manager` role, but could be exploited by any role with the `People` permission. With `Super Admin` access to the application, a user has control over any settings in the Jira Align tenant, including modifying Jira connections, resetting user accounts, or modifying any security settings.

### Vulnerability Details

CVE ID: CVE-2022-36803

Vulnerability Type: Incorrect Access Control

Access Vector: ☒ Remote, ☐ Local, ☐ Physical, ☐ Context dependent, ☐ Other (if other, please specify)

Impact: ☐ Code execution, ☐ Denial of service, ☒ Escalation of privileges, ☐ Information disclosure, ☐ Other (if other, please specify)

Security Risk: ☐ Critical, ☒ High, ☐ Medium, ☐ Low

Vulnerability: CWE-284, CWE-285

An authenticated attacker with the `People` role permission can use the `MasterUserEdit` API to modify any user’s role, including their own, to `Super Admin`. In the sandbox environment that was designed for testing, the `People` permission was added to the `Program Manager` role. However, any role provisioned to Jira Align with only the `People` role permission can exploit this vulnerability.

In the example below, the user was given the `Program Manager` role. However, testing was performed with a customized role with only the `People` role permission enabled and the issue was successfully exploited. If a user can modify other user roles via the front-end GUI of Jira Align, the option to change the user to the `Super Admin` role will not be available. Nonetheless, intercepting the role change request directly to the API and modifying the `cmbRoleID` parameter to 9 will allow the request to be completed. Additionally, without the ability to modify roles using the front-end GUI of Jira Align, if the user is given the `People` permission, they can successfully perform the API call with a `POST` request containing their session cookies:

**Request:**
  
  
  POST /MasterUserEdit HTTP/1.1
  Host: amertrial317.jiraalign.com
  …omitted for brevity…
  btnSubmit=Save&txtStatus=Active&txtStartDate=5%2F25%2F2022&txtEndDate=&rbIsInternal=0&
  txtUID=1209&txtExternalID=&txtFirst=Johnny&txtLast=TesterChangeMe&txtEmail=jashafer%2B
  rolechange%40ebay.com&txtTitle=Mr.+Changeme&cmbRoleID=9&cmbDivision=16&cmbRegion=1&cmb
  City=14&cmbCostCenter=3&cmbTimeZoneID=Turks+And+Caicos+Standard+Time&cmbPublicER=0&txt
  Notes=%60%60%0D%0A'%0D%0A%22%0D%0A%7B%7D%0D%0A%7B%7B2*2%7D%7D%0D%0A%7B3*3%7D%0D%0A%22%
  3Ch1%3Eabc%3C%2Fh1%3E&rbTimeType=1&UNIQ=1209
  

**Response:  
**
  
  
  HTTP/1.1 302 Found
  Date: Thu, 26 May 2022 14:48:18 GMT
  Content-Type: text/html; Charset=utf-8
  Connection: close
  Location: MasterUserEdit?Uniq=1209
  …omitted for brevity…
  Content-Length: 145
  <head><title>Object moved</title></head>
  <body><h1>Object Moved</h1>
  </a>.</body>

After sending the request, the targeted user would be forced to log out of the application. After logging in again, the user would then have the `Super Admin` role, allowing them to modify any aspect of the Jira Align tenant such as modifying Jira connections, resetting user accounts, or modifying security settings.**  
**  

## CREDITS

  * Jacob Shafer, Security Consultant, Bishop Fox ([[email protected]](/cdn-cgi/l/email-protection#9bf1e8f3fafdfee9dbf9f2e8f3f4ebfdf4e3b5f8f4f6))

## TIMELINE

  * 05/31/2022: Initial discovery
  * 06/06/2022: Contact with vendor
  * 06/08/2022: Vendor acknowledged vulnerabilities
  * 06/28/2022: Vendor released patched hotfix version 10.108.3.5 (SSRF)
  * 07/22/2022: Vendor released patched version 10.109.3
  * 10/14/2022: Vulnerabilities publicly disclosed

* * *

![Jake Shaffer Headshot](https://assets.bishopfox.com/prod-1437/Images/author-photos/Jake-Shaffer-Headshot.png)

By Jake Shafer 

Senior Security Consultant III

Jake Shafer is a Senior Security Consultant III at Bishop Fox. He currently focuses on [Application Penetration Testing](https://bishopfox.com/services/penetration-testing-services/application-penetration-testing) and [Hybrid Application Assessments](https://bishopfox.com/services/penetration-testing-services/hybrid-application-assessment); however, he has previous offensive security experience in external and internal penetration testing. Jake is known for his expertise in web application security, source code review, server-side request forgery (SSRF), cross-site scripting (XSS), and web application authorization controls.

Jake earned a B.S. in Information Technology from the University of North Texas ([UNT](https://www.unt.edu/)). He enjoys helping others break into the offensive security world and has presented on this topic at the [UNT Cybersecurity Club](https://untcsc.github.io/).

[ More by Jake Shafer  ](https://bishopfox.com/authors/jacob-shafer)

[ ](https://twitter.com/fibbot) [ ](https://www.linkedin.com/in/jacob-shafer/)

![](/static/assets/images/backgrounds/lander-header-bg-black-lines.svg)

Subscribe to our blog

Be first to learn about latest tools, advisories, and findings.

Thank You! You have been subscribed.
