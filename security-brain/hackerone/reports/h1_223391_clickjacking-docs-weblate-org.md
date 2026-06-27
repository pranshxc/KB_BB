---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223391'
original_report_id: '223391'
title: Clickjacking docs.weblate.org
team_handle: weblate
created_at: '2017-04-24T11:22:11.904Z'
disclosed_at: '2017-06-05T12:45:32.666Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# Clickjacking docs.weblate.org

## Metadata

- HackerOne Report ID: 223391
- Weakness: 
- Program: weblate
- Disclosed At: 2017-06-05T12:45:32.666Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.

This vulnerability affects Web Server.

POC

Here are th steps to reproduce the vulnerability

1.save the below file as anything.html and run it u can see its vulnerable to clickjacking

<html>
   <head>
     <title>Clickjack test page</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="http://docs.weblate.org" width="500" height="500"></iframe>
   </body>
</html>

As far as i know this data is enough to prove that your site is vulberable to Clickjacking..
according to OWASP its more than enough..
https://www.owasp.org/index.php/Testing_for_Clickjacking_(OWASP-CS-004)

Solution

https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet

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
