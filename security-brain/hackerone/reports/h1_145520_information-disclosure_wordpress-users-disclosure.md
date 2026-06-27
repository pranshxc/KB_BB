---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145520'
original_report_id: '145520'
title: Wordpress Users Disclosure
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2019-06-22T00:04:42.696Z'
disclosed_at: '2019-07-01T09:32:11.233Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 8
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Wordpress Users Disclosure

## Metadata

- HackerOne Report ID: 145520
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2019-07-01T09:32:11.233Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

**Information**
Using REST API, we can see all the WordPress users/author with some of their information.

**Step to Reproduce**
You can get user info by entering below url in your browser: 
https://nextcloud.com/wp-json/wp/v2/users

Reference: [#356047](https://hackerone.com/reports/356047)

## Impact

Authors : LTR , LTREditor can be created scenario of doing bruteforce attacks to this users.

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
