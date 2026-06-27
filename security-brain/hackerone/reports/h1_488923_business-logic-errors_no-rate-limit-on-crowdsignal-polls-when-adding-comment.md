---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '488923'
original_report_id: '488923'
title: No Rate Limit on CrowdSignal Polls when Adding Comment
weakness: Business Logic Errors
team_handle: automattic
created_at: '2019-01-31T00:22:11.258Z'
disclosed_at: '2019-04-13T21:40:58.729Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- business-logic-errors
---

# No Rate Limit on CrowdSignal Polls when Adding Comment

## Metadata

- HackerOne Report ID: 488923
- Weakness: Business Logic Errors
- Program: automattic
- Disclosed At: 2019-04-13T21:40:58.729Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team!

I hope this isn't duplicate :/ 

I created a poll on CrowdSignal.com (https://poll.fm/10226924)
When adding a comment, there is no rate limit. You can see my comments on my poll. 

1. Go to any poll.
2. Turn on Intercept and Add a Comment.
3. Send request to Intruder.
4. Set your payloads and start attack.

There is no rate-limit.

## Impact

No rate-limit on comments.

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
