---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1007988'
original_report_id: '1007988'
title: Able to comment/view in others support ticket at https://en.instagram-brand.com/requests/dashboard
weakness: Information Disclosure
team_handle: automattic
created_at: '2020-10-14T02:33:28.392Z'
disclosed_at: '2020-12-05T13:21:03.579Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 51
asset_identifier: www.tumblr.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Able to comment/view in others support ticket at https://en.instagram-brand.com/requests/dashboard

## Metadata

- HackerOne Report ID: 1007988
- Weakness: Information Disclosure
- Program: automattic
- Disclosed At: 2020-12-05T13:21:03.579Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I reported the vulnerability to Facebook, and they have said to report it here for the bounty. 

## Platform(s) Affected:
 https://en.instagram-brand.com/requests/dashboard
## Steps To Reproduce:
1. Create two account User A, User B at https://en.instagram-brand.com/
2. Apply for Instagram brand from https://en.instagram-brand.com/requests/dashboard by User A
3. Login to user B and intercept the request

4.Send a post request with cookie and other header got by intercepting user B in the below endpoint and replace comment 44799 with User A support ticket id 
POST /wp-json/brc/v1/approval-requests/44799/comments HTTP/1.1
text=sure thanks&files=1597287925578-44741-%3Etest.jpg&sizes=4249

## Supporting Material/References:

video POC - https://drive.google.com/file/d/1My6MQuQTmYwCWQw_7uw1veGFkn13WkDP/view?usp=sharing
screenshot of viewing other's messages - https://drive.google.com/file/d/1WnDGPDHGA6pP9RIPBQpEAIXxPTaFJZVX/view?usp=sharing&fbclid=IwAR3k4cEfCcUcfBKhlffQgjDcy4ASRf7V3fsS7FmZcHyyd_HZZfFk1OlDpf8

## Impact

1) can comment in other's support ticket
2) can view other's support ticket comments (Both Instagram as well as user's)

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
