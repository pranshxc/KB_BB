---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1401891'
original_report_id: '1401891'
title: broken authentication (password reset link not expire after use   in  https://network.tochka.com/sign-up)
weakness: Weak Password Recovery Mechanism for Forgotten Password
team_handle: qiwi
created_at: '2021-11-16T18:58:25.333Z'
disclosed_at: '2022-02-22T14:28:04.442Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: '*.tochka.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- weak-password-recovery-mechanism-for-forgotten-password
---

# broken authentication (password reset link not expire after use   in  https://network.tochka.com/sign-up)

## Metadata

- HackerOne Report ID: 1401891
- Weakness: Weak Password Recovery Mechanism for Forgotten Password
- Program: qiwi
- Disclosed At: 2022-02-22T14:28:04.442Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

target :-https://network.tochka.com/

bug:-- Broken Authentication (Password Reset Link Not Expired After Use)
severity:- medium(“Insufficient Security Configurability >Weak Reset Password Implementation > Token Not Invalidated After Use”)

Steps To Find This Bug:
1.Go to https://network.tochka.com/sign-up
2. Enter your email, and ask for a password reset link.
3. Now go to mail and open that link in two tabs.
4. Reset the password from one tab, reload the other tab , and if it let’s you reset password again then it is vulnerable to token not invalidated after use as we are resetting the password two times with same token.

POC :-
Attached

Impact/Exploit Scenario:
If victim’s email account is still logged into his/her Office Computers or any public Internet Café. Then any external attacker can use the used token to reset victims password.
Impact
If victim’s email account is still logged into his/her Office Computers or any public Internet Café. Then any external attacker can use the used token to reset victims password.

## Impact

If victim’s email account is still logged into his/her Office Computers or any public Internet Café. Then any external attacker can use the used token to reset victims password.
Impact
If victim’s email account is still logged into his/her Office Computers or any public Internet Café. Then any external attacker can use the used token to reset victims password.

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
