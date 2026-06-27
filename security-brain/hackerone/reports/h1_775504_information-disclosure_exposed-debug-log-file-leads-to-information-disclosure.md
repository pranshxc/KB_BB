---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '775504'
original_report_id: '775504'
title: Exposed debug.log file leads to information disclosure
weakness: Information Disclosure
team_handle: mariadb
created_at: '2020-01-15T12:44:07.843Z'
disclosed_at: '2020-01-15T22:53:37.716Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: mariadb.org
asset_type: URL
max_severity: medium
tags:
- hackerone
- information-disclosure
---

# Exposed debug.log file leads to information disclosure

## Metadata

- HackerOne Report ID: 775504
- Weakness: Information Disclosure
- Program: mariadb
- Disclosed At: 2020-01-15T22:53:37.716Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

At the following address i have found debug.log file disclose the application full path on the server. And there is database username too in debug.log

http://mariadb.org/wp-content/debug.log

## Impact

Information disclosure

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
