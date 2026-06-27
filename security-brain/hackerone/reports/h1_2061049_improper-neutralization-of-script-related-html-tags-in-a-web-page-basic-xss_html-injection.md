---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2061049'
original_report_id: '2061049'
title: Html injection
weakness: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic
  XSS)
team_handle: mars
created_at: '2023-07-10T13:29:48.812Z'
disclosed_at: '2023-08-30T15:46:22.508Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: '*.wikichat.fr'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-neutralization-of-script-related-html-tags-in-a-web-page-basic-xss
---

# Html injection

## Metadata

- HackerOne Report ID: 2061049
- Weakness: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)
- Program: mars
- Disclosed At: 2023-08-30T15:46:22.508Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Issue Description
Hypertext Markup Language (HTML) injection is a technique used to take advantage of non-validated input to modify a web page presented by a web application to its users. Attackers take advantage of the fact that the content of a web page is often related to a previous interaction with users. When applications fail to validate user data, an attacker can send HTML-fomatted text to modify site content that gets presented to other users. A specifically crafted query can lead to inclusion in the web page of attacker-controlled HTML elements which change the way the application content gets exposed to the web. 

## Issue Identified
The consultant identified that the `show` parameter can reflect into the html page, the outline below demonstrates the steps taken to exploit and reproduce.
## Risk Breakdown
- Risk: **Medium**
 
- Difficulty to Exploit: **Medium**
 
- CVSS:3.1 Score: **5.4** [(/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N)](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N)

## Affected URLs
 - https://www.wikichat.fr


## Exploit Link
 ```html
 https://www.wikichat.fr/trouver-lalimentation-adaptee-chat/?show=pedbaq%22%3E%3Ch1%3Especial%20offer%20%3Ca%20href=https://google.com%3Emalicious%20link%3C/a%3E%3C/h1%3E%3Cinput%20type=hidden%20id=%22
 ```

## Steps to Reproduce
The following steps indicate a proof of concept outlined in three(2) steps to reproduce and execute the issue.

**Step 1:**
Open the `Exploit Link` and you will see the `special offer` with `malicious link` as shown in the image below

![alt text](https://www.uplooder.net/img/image/87/76f9c0358f1f67069b0aeb89de2e0c68/Screenshot-from-2023-07-10-16-40-30.png "malicious page")



**Step 2:**
When the user clicks on the link, redirected to the attacker's site


## References
 - [1] [snyk](https://security.snyk.io/vuln/SNYK-JAVA-COMXUXUELI-3248764)
 - [2] [OWASP](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/03-Testing_for_HTML_Injection)

## Impact

Fraud and deceiving site users

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
