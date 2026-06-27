---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1221942'
original_report_id: '1221942'
title: Shop - Reflected  XSS  With  Clickjacking Leads to Steal User's Cookie  In
  Two Domain
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: meredith
created_at: '2021-06-09T19:18:55.244Z'
disclosed_at: '2022-09-14T16:12:57.122Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: https://marthastewart.com/shop
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Shop - Reflected  XSS  With  Clickjacking Leads to Steal User's Cookie  In Two Domain

## Metadata

- HackerOne Report ID: 1221942
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: meredith
- Disclosed At: 2022-09-14T16:12:57.122Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hii  Security Team ,

I am S Rahul MCEH(Metaxone Certified Ethical Hacker) and a Security Researcher I just checked your website and found Reflected XSS to Good XSS Clickjacking In Two Domain

Description:- As the search parameter is vulnerable to XSS and but the plus point is there is  no X-Frame-Header or Click-jacking Protection.So by combing this two methods the Attack Easier And Converted it to Well Working XSS on Other User’s . 

Vulnerable Urls:- https://marthastewart.com/shop/all.html?s=
                            https://bhg.com/shop/all.html?s=
		
Steps to reproduce :-
1. Navigate to  Vulnerable URLS and As we know that ?s= parameter is vulnerable to XSS 

2.As Reflected XSS Occurs on :-
	Example1 :-  https://bhg.com/shop/all.html?s=%E2%80%98);%3C/script%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E
	Example2 :-  https://marthastewart.com/shop/all.html?s=%E2%80%98);%3C/script%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E

3.The attacker can use different Payloads like document.domain etc 

4.Now as we know there is no X-Frame-Header or Click-jacking Protection that can leads to successful attack

5.Now we will create POC.html to send the victim and steal the cookies of the other users { POC.html is attached below }

6.Now as the victim opens the POC.html the attacker will get the cookies of the users or victim

Refernces:-
https://arbazhussain.medium.com/self-xss-to-good-xss-clickjacking-6db43b44777e
https://hackerone.com/reports/470206
https://hackerone.com/reports/892289

## Impact

Impact
By exploiting this Vulnerability
1.An attacker can force the customer to execute XSS and Steal user's cookie.
2.Launch advanced phishing attacks by rendering arbitrary HTML forms.
3.Force users to download malware/viruses.
4.Execute browser-based attacks etc.

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
