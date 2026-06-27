---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1815463'
original_report_id: '1815463'
title: oauth misconfigration lead to account takeover
weakness: Incorrect Authorization
team_handle: reddit
created_at: '2022-12-22T17:58:40.172Z'
disclosed_at: '2023-05-18T13:53:13.828Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: accounts.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- incorrect-authorization
---

# oauth misconfigration lead to account takeover

## Metadata

- HackerOne Report ID: 1815463
- Weakness: Incorrect Authorization
- Program: reddit
- Disclosed At: 2023-05-18T13:53:13.828Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
misconfigration in aouth 2.0 login with google account in "accounts.reddit.com"

## Impact:
misconfigration leads to account takeover

## Steps To Reproduce:

 1.  go to "https://accounts.reddit.com/".
 2. and login with your google account.
 3. after login, logout from your account.
 4. after logout go to "https://accounts.reddit.com/account/register/" and register with email you signed in before in google account oauth.
 5. as like you see it's created a new account 


  * [attachment / reference]

## Impact

attacker can login with any user's email thats lead to account takeover

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
