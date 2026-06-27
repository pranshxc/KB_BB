---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '149572'
original_report_id: '149572'
title: 'Clickjacking: X-Frame-Options header missing'
weakness: UI Redressing (Clickjacking)
team_handle: legalrobot
created_at: '2016-08-26T19:59:55.903Z'
disclosed_at: '2016-08-29T07:41:34.649Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 4
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking: X-Frame-Options header missing

## Metadata

- HackerOne Report ID: 149572
- Weakness: UI Redressing (Clickjacking)
- Program: legalrobot
- Disclosed At: 2016-08-29T07:41:34.649Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.

This vulnerability affects Web Server.

POC

Here are th steps to reproduce the vulnerability

1.open notepad and paste the following code

<html>
   <head>
     <title>Clickjack test page</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="https://www.legalrobot.com/swag/" width="500" height="500"></iframe>
   </body>
</html>
2.save it as <anyname>.html eg cj.html
3.and just simply open that in browser

As far as i know this data is enough to prove that your site is vulberable to Clickjacking..
according to OWASP its more than enough..
https://www.owasp.org/index.php/Testing_for_Clickjacking_(OWASP-CS-004)

Solution

https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet
check this out..here is the solution for that...

Please also find the attached screenshots (one of response & one of  attack being exploited in browser )

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
