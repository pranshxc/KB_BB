---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '446271'
original_report_id: '446271'
title: CRLF injection
team_handle: x
created_at: '2018-11-17T07:30:34.955Z'
disclosed_at: '2019-12-25T16:08:10.950Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 429
asset_identifier: '*.twitter.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# CRLF injection

## Metadata

- HackerOne Report ID: 446271
- Weakness: 
- Program: x
- Disclosed At: 2019-12-25T16:08:10.950Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello twiiter security team,


on the domain ads.twitter.com http response splitting is vulnerability.


PoC:
https://ads.twitter.com/subscriptions/mobile/landing?ref=gl-tw-tw-promote-mode?t=%0d%0atest:tested

## Impact

an attacker can set new header

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
