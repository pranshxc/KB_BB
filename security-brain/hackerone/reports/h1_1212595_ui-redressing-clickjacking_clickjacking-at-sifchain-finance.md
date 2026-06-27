---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1212595'
original_report_id: '1212595'
title: Clickjacking at sifchain.finance
weakness: UI Redressing (Clickjacking)
team_handle: sifchain
created_at: '2021-05-29T14:44:16.982Z'
disclosed_at: '2021-12-09T17:49:16.209Z'
has_bounty: false
visibility: full
substate: spam
vote_count: 1
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking at sifchain.finance

## Metadata

- HackerOne Report ID: 1212595
- Weakness: UI Redressing (Clickjacking)
- Program: sifchain
- Disclosed At: 2021-12-09T17:49:16.209Z
- Has Bounty: No
- Visibility: full
- Substate: spam

## Original Report

Hi team,

While performing security testing of your website i have found the vulnerability called Clickjacking.

Many URLS are in scope and vulnerable to Clickjacking.

What is Clickjacking ?

Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
This vulnerability affects Web Server.

Steps to Reproduce / POC

Vulnerable Urls:

https://sifchain.finance/

Put every above url one by one in the code of iframe, which is given below

<!DOCTYPE HTML>

<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>I Frame</title>
</head>
<body>
<h3>clickjacking vulnerability</h3>
<iframe src="https://sifchain.finance/" height="550px" width="700px"></iframe>
</body>
</html>

Notice that site is visible in the Iframe

POC is in the attachments. Thanks, waiting for your response.

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
