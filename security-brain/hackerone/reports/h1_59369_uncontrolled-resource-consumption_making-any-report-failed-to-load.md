---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '59369'
original_report_id: '59369'
title: Making any Report Failed to load
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2015-05-03T01:16:24.683Z'
disclosed_at: '2015-05-09T14:06:12.170Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Making any Report Failed to load

## Metadata

- HackerOne Report ID: 59369
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2015-05-09T14:06:12.170Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I found a way to make any report failed to load using this code with Hex Character:
```_www.%40ebаy.com_ ```

I was testing for Homographic Issue using Hex Characters and I listed all of hex character and tried to bypass. 

Then, when I paste the list and comment it in a report I experienced report failed to load then I paste each code with hex character one by one. I figured out that ```%40``` causes the report failed to load.

To reproduce this issue:
- Create a sample report then add a comment using the code above.
- Then, Refresh and you will receive a message ```Report Failed to load```

Regards,
@atom

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
