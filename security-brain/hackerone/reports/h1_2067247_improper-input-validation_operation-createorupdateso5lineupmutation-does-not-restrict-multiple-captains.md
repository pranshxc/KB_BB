---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2067247'
original_report_id: '2067247'
title: Operation CreateOrUpdateSo5LineupMutation does not restrict multiple captains
weakness: Improper Input Validation
team_handle: sorare
created_at: '2023-07-12T17:33:40.847Z'
disclosed_at: '2023-08-01T15:41:17.293Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: api.sorare.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-input-validation
---

# Operation CreateOrUpdateSo5LineupMutation does not restrict multiple captains

## Metadata

- HackerOne Report ID: 2067247
- Weakness: Improper Input Validation
- Program: sorare
- Disclosed At: 2023-08-01T15:41:17.293Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
By tampering with the POST request to the endpoint CreateOrUpdateSo5LineupMutation while editing a team you can change all football players to have the captain attribute to 'true'.  This goes against the UI enforced logic of having only one captain per team, as this attribute gives the football player a 50% score bonus disrupting game logic. 

## Steps To Reproduce:
  1. Go to https://sorare.com/football
  2. Edit a team you own.
  3. Press "Confirm" button.
  4. Intercept the request made to /federation/graphql with the "operationName":"CreateOrUpdateSo5LineupMutation"
{F2493465}
  5. Change all the players attribute "captain":true

## Result:
Confirmed team of all captains:
{F2493464}

## Impact

An attacker could get an unfair advantage vs other users that are following the expected game logic, since the API does not check for multiple captains.

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
