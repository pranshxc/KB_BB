---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1065041'
original_report_id: '1065041'
title: Google API key leaked to Public
weakness: Information Disclosure
team_handle: fetlife
created_at: '2020-12-23T09:47:26.736Z'
disclosed_at: '2021-01-23T00:38:30.188Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 209
asset_identifier: '*.fetlife.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Google API key leaked to Public

## Metadata

- HackerOne Report ID: 1065041
- Weakness: Information Disclosure
- Program: fetlife
- Disclosed At: 2021-01-23T00:38:30.188Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

I found a bunch of endpoints that is leaking you Google Api key.
I tested the key and found it is vulnerable to Geocode Api.

List of vulnerable endpoints
https://ass0.fetlife.com 
https://ass2.fetlife.com
https://app.fetlife.com
https://ass1.fetlife.com 
https://ass3.fetlife.com 
https://fetlife.com
https://ws.fetlife.com 


**POC key:**
`AI████████DM`



**Exploit POC:**
API key is  vulnerable  for Geocode API! Here is the PoC link which can be used directly via browser:
https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=AI████████DM

## Impact

costing companies extra money and in some cases DOS.

Identifies cost: $5 per 1000 request

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
