---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '418145'
original_report_id: '418145'
title: No rate limiting in changing room subject.
team_handle: chaturbate
created_at: '2018-10-03T12:23:54.508Z'
disclosed_at: '2018-10-09T03:59:44.566Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# No rate limiting in changing room subject.

## Metadata

- HackerOne Report ID: 418145
- Weakness: 
- Program: chaturbate
- Disclosed At: 2018-10-09T03:59:44.566Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Before i shed more light on this: I noticed i can create over 200 apps but i don't really know how valid that was.
I want to report that there is no rate limiting  in changing room subject.
Attacker scenrio:
1. Navigate to https://chaturbate.com/b/your username
2. Try to create a room subject and capture the request.
3. Send to intruder and repeater it numerous times.
4. I tried this 144 times and it was succesful
Thanks
Below is a video as a poc

## Impact

bruteforcing.

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
