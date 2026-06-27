---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '405342'
original_report_id: '405342'
title: Clickjacking at ylands.com
weakness: UI Redressing (Clickjacking)
team_handle: bohemia
created_at: '2018-09-04T17:34:03.262Z'
disclosed_at: '2019-03-21T15:28:35.098Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: Domain listed in the policy scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking at ylands.com

## Metadata

- HackerOne Report ID: 405342
- Weakness: UI Redressing (Clickjacking)
- Program: bohemia
- Disclosed At: 2019-03-21T15:28:35.098Z
- Has Bounty: Yes
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

        Steps to Reproduce / POC

Vulnerable Urls:
        https://ylands.com/
	https://workshop.ylands.com/
	https://dayz.com/
	http://armamobileops.com/
	https://minidayz.com/


 Put every above url one by one in the code of iframe, which is given below
---------------------------------------------------

<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>I Frame</title>
</head>
<body>
<h3>clickjacking vulnerability</h3>
<iframe src="https://vigorgame.com/" height="550px" width="700px"></iframe>
</body>
</html>

By Tahir Javed
tahirjavedbhutta@gmail.com

------------------------------------------------------

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
