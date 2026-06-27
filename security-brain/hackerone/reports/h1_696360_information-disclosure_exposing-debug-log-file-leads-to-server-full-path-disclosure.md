---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '696360'
original_report_id: '696360'
title: Exposing debug.log file leads to server full path disclosure
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2019-09-17T10:37:40.752Z'
disclosed_at: '2019-10-17T12:50:54.472Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Exposing debug.log file leads to server full path disclosure

## Metadata

- HackerOne Report ID: 696360
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2019-10-17T12:50:54.472Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

At the following address i have found debug.log file disclose the application full path on the server.
https://nextcloud.com/wp-content/debug.log

## Impact

The server should not expose this log file as it could help an attacker to understand the environment that may lead to further attacks.

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
