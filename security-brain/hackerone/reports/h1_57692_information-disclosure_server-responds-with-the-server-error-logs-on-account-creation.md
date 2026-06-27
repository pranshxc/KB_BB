---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '57692'
original_report_id: '57692'
title: Server responds with the server error logs on account creation
weakness: Information Disclosure
team_handle: enter
created_at: '2015-04-21T23:51:02.249Z'
disclosed_at: '2015-11-26T20:49:08.409Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# Server responds with the server error logs on account creation

## Metadata

- HackerOne Report ID: 57692
- Weakness: Information Disclosure
- Program: enter
- Disclosed At: 2015-11-26T20:49:08.409Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Impact**
Poorly protected response can provide a gold mine of information to an attacker, disclosing a host of sensitive information such as function and file names. This information may enable the attacker
to immediately or later compromise the entire application.

**PoC**

1. Create a new wallet.

2. Intercept the request using a proxy tool.

3. Edit the `bankAccountType` to anything other than CHECKING

The server responds with error log of the server in the header of the response, see attached picture.

Thanks
crab

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
