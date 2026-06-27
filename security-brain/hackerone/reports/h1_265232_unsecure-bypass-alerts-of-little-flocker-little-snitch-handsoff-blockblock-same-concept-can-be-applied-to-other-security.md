---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '265232'
original_report_id: '265232'
title: 'Unsecure: Bypass alerts of Little Flocker / Little Snitch / HandsOff! / BlockBlock
  (same concept can be applied to other security tools)'
team_handle: ibb
created_at: '2017-09-01T14:39:42.126Z'
disclosed_at: '2017-12-12T18:55:55.172Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# Unsecure: Bypass alerts of Little Flocker / Little Snitch / HandsOff! / BlockBlock (same concept can be applied to other security tools)

## Metadata

- HackerOne Report ID: 265232
- Weakness: 
- Program: ibb
- Disclosed At: 2017-12-12T18:55:55.172Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

This PoC is using a simple yet powerful trick to detect when Little Flocker, Little Snitch, HandsOff! or BlockBlock window appear then automatically click on the "Allow" button by calculating the distance (so it works pretty well on every resolution). The window only appear for a fraction of second.

More details about this and PoC at https://github.com/pwnsdx/Unsecure

I am submitting this as HandsOff! finally fixed the issue.

Regards,
Sabri.

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
