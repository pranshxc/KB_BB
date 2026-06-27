---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '412988'
original_report_id: '412988'
title: Hacker can request mediation for published reports
weakness: Improper Authorization
team_handle: security
created_at: '2018-09-23T07:24:41.910Z'
disclosed_at: '2018-11-27T17:31:27.655Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authorization
---

# Hacker can request mediation for published reports

## Metadata

- HackerOne Report ID: 412988
- Weakness: Improper Authorization
- Program: security
- Disclosed At: 2018-11-27T17:31:27.655Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team, @jobert

**Summary:**
After creating the publish report, we do not have a field to send the requested meditation from HackerOne Support

**Description:**

### Steps To Reproduce

1. Create publish report for any program
████████

2. Use query
`https://hackerone.com/reports/`***number_publish_report***`/hacker_help`

My
`https://hackerone.com/reports/███/hacker_help`
POST:
`message=123&mediation_type=unresponsive`


3. Next check report

███


I understand the degree of low, but this is a disagreement between the web and the end point.

Sorry i bad speak english
I hope you understand me
Thank you,haxta4ok00

## Impact

Creating a query `requested meditation from HackerOne Support`  without being able to do so

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
