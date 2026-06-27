---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '235216'
original_report_id: '235216'
title: Exposed FTP Credentials on ███████
weakness: Insufficiently Protected Credentials
team_handle: deptofdefense
created_at: '2017-06-01T02:53:56.499Z'
disclosed_at: '2019-12-02T18:59:13.550Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- insufficiently-protected-credentials
---

# Exposed FTP Credentials on ███████

## Metadata

- HackerOne Report ID: 235216
- Weakness: Insufficiently Protected Credentials
- Program: deptofdefense
- Disclosed At: 2019-12-02T18:59:13.550Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
An exposed configuration file leaks FTP credentials to a DoD server.
**Description:**
The config file hosted on`ftp://█████████/pub/misc/FTP_███████Sign.exe.config` exposes a username `█████████` and associated password `███████`. These are valid credentials for the FTP server operating on `██████████:21`. This was verified by establishing a connection to the server with the credentials - no file data was transferred.
## Impact
Read access to any file on the `████` FTP server.

## Step-by-step Reproduction Instructions

1. Navigate to `ftp://████/pub/misc/FTP_██████Sign.exe.config` (establishes an anonymous FTP session on modern browsers)
2. Verify credentials are in the `userSettings` XML section
3. Establish an FTP connection to `████████` using the credentials

## Suggested Mitigation/Remediation Actions
Anonymous FTP access should be disabled on `██████████` and the credentials exposed in the configuration file should be changed.

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
