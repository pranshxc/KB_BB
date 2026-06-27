---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1482057'
original_report_id: '1482057'
title: HTML injection through Invite Teammate email
team_handle: securityscorecard
created_at: '2022-02-16T03:23:20.015Z'
disclosed_at: '2022-04-09T17:25:32.536Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
asset_identifier: '*.securityscorecard.io'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# HTML injection through Invite Teammate email

## Metadata

- HackerOne Report ID: 1482057
- Weakness: 
- Program: securityscorecard
- Disclosed At: 2022-04-09T17:25:32.536Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I found HTML injection on domain https://platform.securityscorecard.io/ when we send invite teammate email. In this case "message" parameter is vulnerable.

## Steps To Reproduce:

 1. Go to page ( https://platform.securityscorecard.io/ ) and login.
 2. Now go to page https://platform.securityscorecard.io/#/scorecard/wearehackerone.com/factors . Click on "Invite Teammate".
 3. Fill the details first-last name, email and put below payload in "message" parameter
"><h1>HTML INJECTION</h1><a href="evil.com">Click me</a>
 4. Now when invited teammate see email , he will see executed html in email .

Video is attached as poc.

## Impact

1)  Attacker could redirect users and control them easily .
2)  Could steal the credentials .

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
