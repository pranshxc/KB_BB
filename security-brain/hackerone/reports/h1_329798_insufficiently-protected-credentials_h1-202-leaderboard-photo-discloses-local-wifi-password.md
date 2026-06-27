---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '329798'
original_report_id: '329798'
title: h1-202 leaderboard photo discloses local wifi password
weakness: Insufficiently Protected Credentials
team_handle: security
created_at: '2018-03-25T20:30:00.778Z'
disclosed_at: '2018-03-25T21:33:50.355Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 143
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insufficiently-protected-credentials
---

# h1-202 leaderboard photo discloses local wifi password

## Metadata

- HackerOne Report ID: 329798
- Weakness: Insufficiently Protected Credentials
- Program: security
- Disclosed At: 2018-03-25T21:33:50.355Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

the h1-202 event took several photos for the event that rotate on the *public* leaderboard. One of these photos disclosed the local wifi SSID and Password.

**Description:**
SSID: HackerOne
Password: █████████

### Steps To Reproduce

1. Look at the photo attached


### Remediation

Have your staff photographer revie the background for photos to not disclose passwords.

## Impact

Local attackers could connect to the wifi and sniff any unencypted traffic, as well as DoS the network (potentially).

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
