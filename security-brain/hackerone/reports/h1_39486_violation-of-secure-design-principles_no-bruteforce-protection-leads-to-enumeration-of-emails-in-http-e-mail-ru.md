---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '39486'
original_report_id: '39486'
title: No bruteforce protection leads to enumeration of emails in http://e.mail.ru/
weakness: Violation of Secure Design Principles
team_handle: mailru
created_at: '2014-12-16T10:39:32.909Z'
disclosed_at: '2015-06-28T14:41:06.705Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# No bruteforce protection leads to enumeration of emails in http://e.mail.ru/

## Metadata

- HackerOne Report ID: 39486
- Weakness: Violation of Secure Design Principles
- Program: mailru
- Disclosed At: 2015-06-28T14:41:06.705Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is no bruteforce protection here  http://e.mail.ru/cgi-bin/passrestore?email=[email here]
Also the actual thing is when I put a non-existing email in the above url's "email" parameter I get an error.
But if i put my email there it gives the option to recover my password which means the email exists. As this do not have any bruteforce protection an attacker may get all the emails of the mail.ru
Thanks
Niyaax

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
