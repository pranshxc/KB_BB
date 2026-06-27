---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '921286'
original_report_id: '921286'
title: Denial of Service  [Chrome]
weakness: Uncontrolled Resource Consumption
team_handle: x
created_at: '2020-07-11T21:51:46.289Z'
disclosed_at: '2020-07-24T20:00:58.923Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 66
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Denial of Service  [Chrome]

## Metadata

- HackerOne Report ID: 921286
- Weakness: Uncontrolled Resource Consumption
- Program: x
- Disclosed At: 2020-07-24T20:00:58.923Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

**Summary:**
I encountered such an error while creating a new account:
{F903872}
But I don't remember where I found this last point. I remember only when I was a new member.
I created a url using the load **%xx** as in #500686 reports as follows.
`https://twitter.com/i/flow/%00`

I got a result like the #903740 report I just sent you:
{F903873}

But this time only Chrome works. I haven't figured out why this DoS was triggered yet.
 I will keep you updated when I find new findings.

Thanks!
@cyanpiny

## Impact

An attacker could apply this DoS to any Twitter account or popular tag. It prevents a large audience or target user from accessing Twitter from the browser.

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
