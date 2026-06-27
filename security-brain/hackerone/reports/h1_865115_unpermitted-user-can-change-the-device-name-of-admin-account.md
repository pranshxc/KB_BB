---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '865115'
original_report_id: '865115'
title: unpermitted user can change the device name of admin account
team_handle: helium
created_at: '2020-05-03T06:50:04.504Z'
disclosed_at: '2020-06-16T14:41:17.183Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: https://helium-console-dev.herokuapp.com/
asset_type: URL
max_severity: high
tags:
- hackerone
---

# unpermitted user can change the device name of admin account

## Metadata

- HackerOne Report ID: 865115
- Weakness: 
- Program: helium
- Disclosed At: 2020-06-16T14:41:17.183Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Invited user with only the read-only permission can change the device name in admin account

1.create two account 'A 'and 'B ' in  console.helium
2.Invited the account 'B' with 'A' by giving the read-only permission
3.In account 'B' trying to delete the organization created by admin account 'A' and intercept the request then you got the organization id in request
4.Then in account 'B' add the device name and click on it and update the name which you want to display in the admin account(victim account)
5.And intercept the request while clicking the update button
6.In the request add the organization id which you got in step 3
7.then forward the request then the device name in admin account will be changed

## Impact

attacker with only the read-only permission can change the device name in the admin account

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
