---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1234746'
original_report_id: '1234746'
title: Private program disclosure through notifications
weakness: Improper Access Control - Generic
team_handle: security
created_at: '2021-06-15T15:13:41.573Z'
disclosed_at: '2021-08-05T18:42:15.562Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Private program disclosure through notifications

## Metadata

- HackerOne Report ID: 1234746
- Weakness: Improper Access Control - Generic
- Program: security
- Disclosed At: 2021-08-05T18:42:15.562Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

**Summary:**

I recently came across hackerone report: https://hackerone.com/reports/1179241 . I though this was fixed but today I have have faced similar experience. I have received a Scope and policy update from the program "██████" which I am not part of. 

████████


When I was clicking on the notifications, scope update notification is taking me to hacktivity page and policy update notification is taking me to "Page not found page", I think the previous fix to #1179241 is not complete  . As a proof, I have attached a video poc and screenshots.

### Steps To Reproduce

1. Login to Hackerone account
2. Checked my notifications

## POC

██████████

## Impact

I was able to received notification updates of a private program to which I am not part of. This discloses the private program handle to which i am not part of.

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
