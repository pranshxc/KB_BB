---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '78685'
original_report_id: '78685'
title: Email spoofing configuration missing
weakness: Violation of Secure Design Principles
team_handle: flox
created_at: '2015-07-25T11:29:39.246Z'
disclosed_at: '2015-07-27T02:05:19.831Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Email spoofing configuration missing

## Metadata

- HackerOne Report ID: 78685
- Weakness: Violation of Secure Design Principles
- Program: flox
- Disclosed At: 2015-07-27T02:05:19.831Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Email spoofing in 
flox.io
buddypress.org
bbpress.org


There are few email spoofing tool is available free.one them is

http://emkei.cz/

when I tried to send a email from admin@flox.io  or admin@buddypress.org  or  admin@bbpress.org   to my email ,it was successful but when i tried to send the another from admin@facebook.com or any other , i did not receive any email.Hence, there might be some configuration missing in your mail servers (i would love to know how this is happening).

This can be dangerous ,as attacker can send some fake email about free offer .., free money or password reset etc.. , and victims may claim on  flox.io
buddypress.org
bbpress.org
( which can lead to reputation loss :)

any it can be missued in many ways

note:- check spam if you cannot find the mail in inbox
EXTRA INFO
it is Issues with the SPF, DKIM or DMARC records on flox.io
buddypress.org
bbpress.org
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
