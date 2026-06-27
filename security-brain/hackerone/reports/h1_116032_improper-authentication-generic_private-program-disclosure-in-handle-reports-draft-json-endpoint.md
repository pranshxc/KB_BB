---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116032'
original_report_id: '116032'
title: Private Program Disclosure in /:handle/reports/draft.json endpoint
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2016-02-12T02:33:23.118Z'
disclosed_at: '2016-02-16T20:22:07.670Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# Private Program Disclosure in /:handle/reports/draft.json endpoint

## Metadata

- HackerOne Report ID: 116032
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2016-02-16T20:22:07.670Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

PoC revealed an issue in the HTTP codes returned for the /reports/draft.json endpoint:



private team: https://hackerone.com/[invite-only team handle]/reports/draft.json
Returned {"error":"You need to sign in or sign up before continuing."} with Status Code:401 OK

user: https://hackerone.com/[user handle]/reports/draft.json
Returned 404
thanks

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
