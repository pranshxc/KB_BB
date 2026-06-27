---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '703972'
original_report_id: '703972'
title: Reset any password
weakness: Weak Password Recovery Mechanism for Forgotten Password
team_handle: pixiv
created_at: '2019-09-29T21:45:27.602Z'
disclosed_at: '2021-03-31T01:58:17.733Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 298
asset_identifier: www.pixiv.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- weak-password-recovery-mechanism-for-forgotten-password
---

# Reset any password

## Metadata

- HackerOne Report ID: 703972
- Weakness: Weak Password Recovery Mechanism for Forgotten Password
- Program: pixiv
- Disclosed At: 2021-03-31T01:58:17.733Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

When I try to reset the password, the verification code of the mailbox is 6 digits, and there is no limit on the number of submissions, so I can reset the password of any user.

## Steps To Reproduce:
1.input the email  [reset password url](https://www.pixiv.net/reminder.php).
{F595146}
click  the "submit" button
{F595147}
input the email verification code and try to guess the verification code, but I won’t be able to continue using it after I try it a few times.

{F595148}

2.After trying, I found that there was no such submission restriction when the password was reset in the third step.

Repeat the above steps, the only difference is that you need to enter the correct verification code.

{F595160}
It can be seen that when we reset the password in the last step, the verification code will still be sent, that is, the verification code will be sent to the server for validity verification in the last step, and the verification code of the last step is not limited by the number of submissions. In other words, we can guess the verification code.

I wrote a python script to verify the vulnerability, you only need to enter the following parameters to verify the vulnerability.

parameter：tt code_id code phpsession

python: {F595166}
video: {F595172}

## Supporting Material/References:
none

  * [attachment / reference]

## Impact

Reset any user's password

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
