---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1485788'
original_report_id: '1485788'
title: Improper Authentication via previous backup code login
weakness: Improper Authentication - Generic
team_handle: basecamp
created_at: '2022-02-19T10:40:58.147Z'
disclosed_at: '2022-03-24T02:45:41.414Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: launchpad.37signals.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Improper Authentication via previous backup code login

## Metadata

- HackerOne Report ID: 1485788
- Weakness: Improper Authentication - Generic
- Program: basecamp
- Disclosed At: 2022-03-24T02:45:41.414Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HI Basecamp,

I would like to report Improper Authentication in basecamp. Attacker is able to login at victim account once victim update his password.


attacker knows with victims email `█████████` password `uhn)(*123HH`
victim updates his password          `uhn)(*123HHjcc`

Step To Reproduce

==Attacker==

- Step1 attacker know victim password and logs in

- Step2 attacker enables 2fa in victims account.

- Step3 attacker logs out and login back in victim account, 2fa will be prompter, attacker gaves 2fa backup code and send request to repeater and captures the response.
██████

- Step4 attacker now removes 2fa from victim account and logout.


==Victim==

- Step5 victim logs in and `changes password.` from `uhn)(*123HH`to  `uhn)(*123HHjcc`

==Attacker==

- Step6 attacker logins in `victim account` with ==previous known password== and changes ==Step6 response with  Step3 response.==

- Attacker logged in victims account even he dose not know new password of victim.



Video POC attached for your reference.
████


Thanks,
@fuzzsqlb0f

## Impact

Improper Authentication.

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
