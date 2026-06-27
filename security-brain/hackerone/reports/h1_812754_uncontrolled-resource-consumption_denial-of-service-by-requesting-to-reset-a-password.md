---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '812754'
original_report_id: '812754'
title: Denial of Service by requesting to reset a password
weakness: Uncontrolled Resource Consumption
team_handle: nextcloud
created_at: '2020-03-07T13:51:40.910Z'
disclosed_at: '2021-01-25T20:12:19.503Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Denial of Service by requesting to reset a password

## Metadata

- HackerOne Report ID: 812754
- Weakness: Uncontrolled Resource Consumption
- Program: nextcloud
- Disclosed At: 2021-01-25T20:12:19.503Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description:
I believe that this is posible due to the brute force protection that makes all request last for 30 seconds which in this case is using all the PHP workers avalible in the pool, so the only way to defend yourself is setting up a limit or having a lot of resources.

### How to reproduce:
* In the Nextcloud login screen click the "Forgot password?" button and then type something in the textbox (can be anything)
* Then open the developers tools and go to the network tab
* Hold the "enter" key after pressing the reset password button and in the network tab you will see a lot of request being made
* With just 1000 request I managed to make the demo server "https://demo2.nextcloud.com/" not respond for 1 hour

## Impact

The attacker could make an entire nextcloud installation or even the entire server where it is hosted not respond for a very long time
Also, this attack can be made by almost anyone

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
