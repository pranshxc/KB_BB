---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '473064'
original_report_id: '473064'
title: Open Redirect On Your Login Panel
weakness: Open Redirect
team_handle: zomato
created_at: '2018-12-29T09:02:59.819Z'
disclosed_at: '2019-02-14T17:14:26.360Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 10
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open Redirect On Your Login Panel

## Metadata

- HackerOne Report ID: 473064
- Weakness: Open Redirect
- Program: zomato
- Disclosed At: 2019-02-14T17:14:26.360Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Summery**
Hey There are a open Redirect on your login panel

**Platform(s) Affected:** Website

## Browsers Verified In [If Applicable]:

  * Chrome For Android
  * Firefox For Android

## Steps To Reproduce:

  1. Go To This Url :- https://www.zomato.com/login?redirect_url=https://askdcodes.org
  2. Then login there
  3. boom you got Redirected to askdcodes.org

## Supporting Materials ##
Attaching A Video Poc

## Impact

Any Attacker can Redirect your users to malicious website

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
