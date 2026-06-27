---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '109373'
original_report_id: '109373'
title: Multiple vulnerabilities in mail.ru subdomains
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2016-01-08T15:57:36.732Z'
disclosed_at: '2016-01-27T09:31:21.473Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Multiple vulnerabilities in mail.ru subdomains

## Metadata

- HackerOne Report ID: 109373
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2016-01-27T09:31:21.473Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi. I found multiple vulnerabilities in mail.ru subdomains, affecting many mail.ru users and putting them at risk. Here are the details:

AFFECTED DOMAINS:

http://torg.mail.ru/---------------UI Redress (Clickjacking)
https://pogoda.mail.ru/---------------UI Redress (Clickjacking)
https://auto.mail.ru/ ------------XSS
http://s1.amigo.mail.ru/---------------UI Redress (Clickjacking)
https://top.mail.ru/---------------UI Redress (Clickjacking)

POC 1: (Clickjacking)

<html>
<head>
<title>Clickjacking POC</title>
</head>
<body>
<p>vulnerable to clickjacking</p>
<iframe src="https://pogoda.mail.ru/" width="500" height="500"></iframe>
</body>
</html>

*Just change the subdomains (those vulnerable to clickjacking) to see the effect

POC 2: (XSS)

1. Go to https://auto.mail.ru/ 
2. In the searchbar, enter the XSS payload: <img src=x onerror=alert(document.domain)>
3. Click Enter
4. XSS pop up

Impact: An attacker can host this domain in other evil site by using iframe and if a user fill the given filed it can directly redirect as logs to attacker and after its redirect to your web server.. its lead to steal user information too and use that host site as phishing of your site its CSRF and Clickjacking. Can lead to CSRF too...Impact: An attacker can host this domain in other evil site by using iframe and if a user fill the given filed it can directly redirect as logs to attacker and after its redirect to your web server.. its lead to steal user information too and use that host site as phishing of your site its CSRF and Clickjacking. Can lead to CSRF too...

Possible fix: Recommended fix is to add the HTTP header X FRAME OPTIONS and set it to DENY

I hope you consider my report, POC attached for XSS...

Thanks

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
