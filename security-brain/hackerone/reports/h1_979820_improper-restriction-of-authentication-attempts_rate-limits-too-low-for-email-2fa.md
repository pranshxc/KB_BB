---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '979820'
original_report_id: '979820'
title: Rate limits too low for email 2FA
weakness: Improper Restriction of Authentication Attempts
team_handle: bitwarden
created_at: '2020-09-11T14:34:10.398Z'
disclosed_at: '2020-10-14T18:18:31.415Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: vault.bitwarden.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Rate limits too low for email 2FA

## Metadata

- HackerOne Report ID: 979820
- Weakness: Improper Restriction of Authentication Attempts
- Program: bitwarden
- Disclosed At: 2020-10-14T18:18:31.415Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

NO RATE LIMIT ON 2FA CAN LEAD TO ACCOUNT COMPROMISE!

1. Create account on vault.bitwarden.com  if you don't have.
2.Setup 2FA via email 
3.Logout and log in again. This time along with password you have to fill the 2fa code which is sent to the email.
4.Type Any Random number, intercept request with burp  then send to intruder, mark the code position and start bruteforcing

Results:

>>Invalid Code Response = 400 
>>Valid Code Response = 200

## Impact

2FA acts as extra security. Even if the attacker has user credentials 2FA always protects them from accessing the user data and compromise their whole account.
If the 2FA can be bruteforced it can lead to account compromise assuming that attacker already knows email and password!

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
