---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '221989'
original_report_id: '221989'
title: Sensitive information disclosure via response headers on jenkins.brew.sh
weakness: Information Exposure Through an Error Message
team_handle: homebrew
created_at: '2017-04-19T04:42:43.263Z'
disclosed_at: '2017-04-25T16:46:47.777Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
- information-exposure-through-an-error-message
---

# Sensitive information disclosure via response headers on jenkins.brew.sh

## Metadata

- HackerOne Report ID: 221989
- Weakness: Information Exposure Through an Error Message
- Program: homebrew
- Disclosed At: 2017-04-25T16:46:47.777Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

While logging into jenkins.brew.sh site, the vulnerable nginx version is disclosed via response headers.
There is a chance with known vulnerabilities this could be compromised. so better to avoid banner disclosure with "Server Tokens Prod off" modification in conf file.

Please let me know if any further information is required.

Regards,
Mr_R3boot.

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
