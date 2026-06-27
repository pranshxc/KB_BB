---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '36594'
original_report_id: '36594'
title: New Device Confirmation, token is valid until not used.
weakness: Cryptographic Issues - Generic
team_handle: coinbase
created_at: '2014-11-18T14:53:31.691Z'
disclosed_at: '2015-05-24T21:14:41.227Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# New Device Confirmation, token is valid until not used.

## Metadata

- HackerOne Report ID: 36594
- Weakness: Cryptographic Issues - Generic
- Program: coinbase
- Disclosed At: 2015-05-24T21:14:41.227Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

New Device Confirmation token sends to the logged in user from unconfirmed device. Now If Click on Account or Settings or Profile email of new token will send to that person and same if user click multiple times, more and more confirmation emails user received. On each reload each confirmation token send to the user's email. Now All Tokens are Valid.

User will use any one of them, but others are still valid. So It should expire after sometime.

I have checked by reloading multiple times and all tokens are valid.

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
