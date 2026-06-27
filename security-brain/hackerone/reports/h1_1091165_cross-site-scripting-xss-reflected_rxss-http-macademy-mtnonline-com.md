---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1091165'
original_report_id: '1091165'
title: RXSS - http://macademy.mtnonline.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: mtn_group
created_at: '2021-01-31T11:18:15.229Z'
disclosed_at: '2021-12-11T15:31:49.881Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
asset_identifier: mtnonline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# RXSS - http://macademy.mtnonline.com

## Metadata

- HackerOne Report ID: 1091165
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: mtn_group
- Disclosed At: 2021-12-11T15:31:49.881Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The page located at http://macademy.mtnonline.com
suffers from a Cross-site Scripting (XSS) vulnerability. XSS is a vulnerability that occurs when user input is unsafely encorporated into the HTML markup inside of a webpage. When not properly escaped an attacker can inject malicious JavaScript that, once evaluated, can be used to hijack authenticated sessions and rewrite the vulnerable page's layout and functionality. The following report contains information on an XSS payload that has fired on http://macademy.mtnonline.com, it can be used to reproduce and remediate the vulnerability.

Steps To Reproduce
Go to Those Links.
http://macademy.mtnonline.com/learner/ContactUs.aspx/(A('onerror='alert%60xElkomy%60'xelkomy))/Signin.aspx

Browsers
I test them on Firefox and Google Chrome.

Fix:-
Filter input on arrival
Encode data on output
Use appropriate response headers
Content Security Policy.

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
