---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2101087'
original_report_id: '2101087'
title: Able to see Bonus amount given to a report  even if the bounty and Bonus is
  not visible to public or mentioned in {Report-Id}.json
weakness: Information Disclosure
team_handle: security
created_at: '2023-08-08T12:28:50.725Z'
disclosed_at: '2023-09-14T07:45:39.073Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 94
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Able to see Bonus amount given to a report  even if the bounty and Bonus is not visible to public or mentioned in {Report-Id}.json

## Metadata

- HackerOne Report ID: 2101087
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2023-09-14T07:45:39.073Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
Hey team,
while looking at your Disclosed reports I noticed that on report #2082680 you awarded the user with a Bonus and no bounty at all it was hidden as well because the Activity shows that "HackerOne rewarded someone with a bounty. " which also included the **Bonus**, upon checking the #2082680.json  I did not found the "bonus_amount" parameter at all or any number representing ████ which was the bonus given to the user thus it was supposed to be a Confidential but it's now exposed to the public.

As a PoC look at this report showing the Bonus amount in JSON 
A bonus of ███████ was given to the user of this report as well  https://hackerone.com/reports/1952124.json but upon checking the JSON format of this you can clearly see it's mentioned in the "bonus_amount"  parameter.

**Description:**

### Steps To Reproduce

1. Go to https://hackerone.com/reports/2082680 and see the right column of the screen and see the activity column's Bounty amount  
 ████

## Impact

Confidential  Information Disclosure

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
