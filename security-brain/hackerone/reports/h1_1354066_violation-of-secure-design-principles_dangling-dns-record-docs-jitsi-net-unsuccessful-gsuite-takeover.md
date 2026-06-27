---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1354066'
original_report_id: '1354066'
title: Dangling DNS Record docs.jitsi.net (unsuccessful GSuite takeover)
weakness: Violation of Secure Design Principles
team_handle: 8x8-bounty
created_at: '2021-09-28T19:06:58.550Z'
disclosed_at: '2023-04-03T00:36:41.823Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: '*.jitsi.net'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Dangling DNS Record docs.jitsi.net (unsuccessful GSuite takeover)

## Metadata

- HackerOne Report ID: 1354066
- Weakness: Violation of Secure Design Principles
- Program: 8x8-bounty
- Disclosed At: 2023-04-03T00:36:41.823Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

HI Team , it is possible for a Attacker to do Sub-domain takeover - http://docs.jitsi.net/

As we can see in the Screenshot it is 404 and belongs to ghs google

As I tried claiming the domain it was possible for me to claim it by using workspace .

Hence it is possible to do Sub-domain Takeover

## Impact

An attacker can claim this subdomain by requesting a process of registering this abandoned subdomain to his name.
And attacker can fully take over this subdomain and do whatever he wants. this can cause huge damage to the website's main domain as well as to the company.
I Recommend removing  the Cname and DNS connecting to it.

You can read about this sort of attacks here : https://www.siteground.com/tutorials/googleapps/google_calendar.htm

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
