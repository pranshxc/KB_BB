---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '903740'
original_report_id: '903740'
title: Denial of Service | twitter.com & mobile.twitter.com
weakness: Uncontrolled Resource Consumption
team_handle: x
created_at: '2020-06-20T11:31:57.245Z'
disclosed_at: '2020-09-02T19:18:29.905Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 86
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Denial of Service | twitter.com & mobile.twitter.com

## Metadata

- HackerOne Report ID: 903740
- Weakness: Uncontrolled Resource Consumption
- Program: x
- Disclosed At: 2020-09-02T19:18:29.905Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Detail:
I found a DoS that works on **twitter.com** and **mobile.twitter.com**, but it doesn't work on the mobile app. The user only needs to view the message or tweet in order to be exposed to this DoS. As far as I can remember, a report similar to this report has been sent to you before, but I think it's no longer public.

Note:
- If the user tries to view the DoS message or tweet from twitter.com, DoS will definitely work, but if it enters from Chrome and displays this DoS from **mobil.twitter.com**, this DoS will not work. This works without exception in Edge and Firefox.

- I think this is a browser-based DoS, so I think it won't work on Desktop Twitter. So I didn't test it.

- I did my tests on my own accounts. I haven't done a test for any tag. But I'm sure it will work.


PoC & Steps:
`http://twitter.com:627732462`



{F875527}

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
