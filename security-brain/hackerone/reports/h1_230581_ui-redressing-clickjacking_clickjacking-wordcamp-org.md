---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '230581'
original_report_id: '230581'
title: Clickjacking wordcamp.org
weakness: UI Redressing (Clickjacking)
team_handle: wordpress
created_at: '2017-05-22T05:52:59.310Z'
disclosed_at: '2017-06-24T18:24:56.135Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking wordcamp.org

## Metadata

- HackerOne Report ID: 230581
- Weakness: UI Redressing (Clickjacking)
- Program: wordpress
- Disclosed At: 2017-06-24T18:24:56.135Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Security,
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.
The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
This vulnerability affects Web Server.
IMPACT:
An attacker can host this domain in other evil site by using iframe and if a user fill the given filed it can directly redirect as logs to attacker and after its redirect to your web server.. its lead to steal user information too and use that host site as phishing of your site its CSRF and Clickjacking
POC:
1.Open URL :https://www.blockchain.com/
2.put the url in the below code of iframe
<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>i Frame</title>
</head>
<body>
<h3>This is clickjacking vulnerable</h3>
<iframe src="https://www.blockchain.com/" frameborder="2 px" height="500px" width="500px"></iframe>
</body>
</html>

3.Observe that site is getting displayed in Iframe

Impact:
By using Clickjacking technique, an attacker hijack's click's
meant for one page and route them to another page, most likely
for another application, domain, or both.

Remediation:
Frame busting technique is the better framing protection
technique.
Sending the proper X-Frame-Options HTTP response headers
that instruct the browser to not allow framing from other
domains

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
