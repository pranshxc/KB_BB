---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '500686'
original_report_id: '500686'
title: url that twitter mobile site can not load
weakness: Uncontrolled Resource Consumption
team_handle: x
created_at: '2019-02-25T09:22:42.338Z'
disclosed_at: '2019-03-19T21:44:36.317Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 139
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# url that twitter mobile site can not load

## Metadata

- HackerOne Report ID: 500686
- Weakness: Uncontrolled Resource Consumption
- Program: x
- Disclosed At: 2019-03-19T21:44:36.317Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
A url that twitter mobile site can not load, crushes any page containing this url

**Description:** 
Invalid hex characters crushes twitter mobile site as example go to ```https://mobile.twitter.com/?%xx``` 
twitter won't load.

1) Sending such url on a direct message, twitter will no longer be able to load the conversation,
F429765
2) Tweet such url, anyone following you won't be able to load any tweets
F429766

I think Twitter on the client side trying to find a value for %xx which is not possible so it raises an error

## Steps To Reproduce:

  1. Go to https://mobile.twitter.com/
  2. Send or tweet this url ```https://mobile.twitter.com/?%xx```
  3. You and your followers won't be able to see any tweets on the mobile site

## Impact

This issue works only on https://mobile.twitter.com/
(not working on IOS, Android and https://twitter.com/ )
however, all twitter mobile users with no twitter app should be affected

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
