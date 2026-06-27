---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1066189'
original_report_id: '1066189'
title: Account takeover just through csrf in https://booking.qiwi.kz/profile
weakness: Improper Access Control - Generic
team_handle: qiwi
created_at: '2020-12-25T08:53:52.575Z'
disclosed_at: '2021-05-20T13:53:14.881Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 30
asset_identifier: Subdomains
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Account takeover just through csrf in https://booking.qiwi.kz/profile

## Metadata

- HackerOne Report ID: 1066189
- Weakness: Improper Access Control - Generic
- Program: qiwi
- Disclosed At: 2021-05-20T13:53:14.881Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team:

after register by any account, we can found that we can change email in profile to another one, by just using a GET request https://booking.qiwi.kz/ajax__confirm_contact?type=email_confirmed&contact=email@email.com&iframePopupMode=1 but without verification, attacker can steal account without verification.

POC:
-----------

1 - after register open https://booking.qiwi.kz/profile
2 - now just use this url https://booking.qiwi.kz/ajax__confirm_contact?type=email_confirmed&contact=alwardaniahmed2@gmail.com&iframePopupMode=1
3 - now i can take your account by go to reset password and reset your password by using victim email , and i will recieve the reset password token in my email

POC Video:
--------------

1 - {F1129450}

## Impact

attacker can takeover victim account.

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
