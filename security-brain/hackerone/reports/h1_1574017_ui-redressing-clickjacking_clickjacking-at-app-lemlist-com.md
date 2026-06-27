---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1574017'
original_report_id: '1574017'
title: Clickjacking at  app.lemlist.com
weakness: UI Redressing (Clickjacking)
team_handle: lemlist
created_at: '2022-05-18T01:43:11.747Z'
disclosed_at: '2022-05-20T15:04:22.692Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: app.lemlist.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking at  app.lemlist.com

## Metadata

- HackerOne Report ID: 1574017
- Weakness: UI Redressing (Clickjacking)
- Program: lemlist
- Disclosed At: 2022-05-20T15:04:22.692Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

While performing security testing of your website i have found the vulnerability called Clickjacking.
Many URLS are in scope and vulnerable to Clickjacking.

What is Clickjacking ?

Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
This vulnerability affects Web Server.


Vulnerable Urls:
=============

https://app.lemlist.com

Put every above url one by one in the code of iframe, which is given below
```javascript
<html lang="tr-TR">
<kafa>
<meta karakter kümesi="UTF-8">
<title>Çerçeve Yapıyorum</title>
</head>
<body>
<h3>clickjacking güvenlik açığı</h3>
<iframe src="https://app.lemlist.com/teams/tea_sgYr5dZr478x4FQ9K/settings/user/usr_Z3GZ4DDHLLyLyZHj5/users" height="550px" width="700px"></iframe>
</body>
</html>
```

## Impact

Using a similar technique, keystrokes can also be hijacked. With a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email or bank account, but are instead typing into an invisible frame controlled by the attacker.

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
