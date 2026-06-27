---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '153095'
original_report_id: '153095'
title: Text Only Content Spoofing on ubermovement.com Community Page
weakness: Violation of Secure Design Principles
team_handle: uber
created_at: '2016-07-22T07:20:53.698Z'
disclosed_at: '2016-07-26T00:26:27.432Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Text Only Content Spoofing on ubermovement.com Community Page

## Metadata

- HackerOne Report ID: 153095
- Weakness: Violation of Secure Design Principles
- Program: uber
- Disclosed At: 2016-07-26T00:26:27.432Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Text Only Content Spoofing on ubermovement.com Community Page

Vulnerable URL:
http://ubermovement.com/community?tag=%20Stories%20have%20false%20information.%20Visit%20http://attacker.com%20for%20real%20stories.

Content Spoofing is an attack technique that allows an attacker to inject a malicious payload that is later misrepresented as legitimate content of a web application. This approach is common on error pages, or sites providing story or news entries. The content specified in this parameter is later reflected into the page to provide the content for the page. If an attacker where to replace this content with something more sinister they might be able to falsify statements on the destination website. Upon visiting this link the user would believe the content being displayed as legitimate
.
This attack exploits the trust relationship established between the user and the web site. 

The community page says about the stories from driver-partner. An attacker can specify misleading/falsified information about the stories through ‘tag’ parameter and trick the user into clicking the URL via email. This falsified information is reflected back on to the browser by the application and user consider it as a legitimate content, thereby follow the information provided by the attacker.
In this example the falsified content is directly reflected back on the same page. Please refer the attachment.
 
Valid Page: http://ubermovement.com/community?tag=Washington
Modified Page: http://ubermovement.com/community?tag=%20Stories%20have%20false%20information.%20Visit%20http://attacker.com%20for%20real%20stories.

It is recommended to allow the user to supply only trusted input using white-listing technique in order to maintain the trust between the user and web site.

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
