---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146368'
original_report_id: '146368'
title: BRUTE FORCE ATTACK
team_handle: mailru
created_at: '2016-06-22T03:46:36.474Z'
disclosed_at: '2016-06-27T09:20:58.275Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
tags:
- hackerone
---

# BRUTE FORCE ATTACK

## Metadata

- HackerOne Report ID: 146368
- Weakness: 
- Program: mailru
- Disclosed At: 2016-06-27T09:20:58.275Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi I've found that the user is allowed to perform brute force in 
https://m.my.mail.ru/cgi-bin/login
https://babel.mail.ru/login/ ,
 I've tried to input wrong password 30 times , then input my correct password in my 31st attempt and it is successfully login, a malicious minded user can always continue guessing an account password.

Steps to reproduce

Go to https://m.my.mail.ru/cgi-bin/login  &  https://babel.mail.ru/login/  then click login button and you can now perform brute force attack.

Regards
WHITE DRAGON

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
