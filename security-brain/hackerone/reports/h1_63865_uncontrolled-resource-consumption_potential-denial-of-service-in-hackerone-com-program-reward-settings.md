---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '63865'
original_report_id: '63865'
title: Potential denial of service in hackerone.com/<program>/reward_settings
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2015-05-27T04:30:15.478Z'
disclosed_at: '2015-06-10T04:13:53.662Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Potential denial of service in hackerone.com/<program>/reward_settings

## Metadata

- HackerOne Report ID: 63865
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2015-06-10T04:13:53.662Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

While setting the bounty for the program, if I set the bounty to a large value (over 1,000,000 digits) and send the request the website hangs for about a minute and a half, then pops up an error page saying there is an error on Hackerone's Host end.

Time taken to repsond : 76856 Millisecond = 76.856 Seconds
Error Code: `Error 522`
URL: https://hackerone.com/<program>/reward_settings

The Request and response is attached in this Report.

Vulneurabe paramater `base_bounty`

Request parameters format:

    {"handle":"<program>","errors":{},"offers_bounties":true,"advertise_bounties":true,"base_bounty":"1111....till 1,000,000 digits","hide_bounty_amounts":false,"team_state":"sandboxed","allowed_to_disable_bounties?":true}

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
