---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '923864'
original_report_id: '923864'
title: RXSS - ████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-07-14T21:44:16.240Z'
disclosed_at: '2021-10-18T19:25:06.349Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# RXSS - ████

## Metadata

- HackerOne Report ID: 923864
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-10-18T19:25:06.349Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello, friends today when I was checking some sites I found this bug on your own website.


##Detalis XSS
Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.
[OWASP](https://owasp.org/www-community/attacks/xss/)



##Steps To Reproduce
Go to Those Links.
`https://███/(A(%22onerror='alert%601%60'testabcd))/Login.aspx?ReturnUrl=%2f`

##Browsers
I test them on Firefox and Google Chrome.

##Fix:-
Filter input on arrival
Encode data on output
Use appropriate response headers
Content Security Policy.
These all are standards concepts for fix the XSS vulnerabilities.

Regards, 
xElkomy

## Impact

View any information that the user is able to view. Modify any information that the user is able to modify. Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user. || And I can used this for
1-Ad-Jacking
2-Session Hijacking
3-Bypassing CSRF protection
4-Crypto Mining ::::)))

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
