---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '961997'
original_report_id: '961997'
title: Denial of Service when entring an Array in email at seetings
team_handle: nextcloud
created_at: '2020-08-19T02:36:42.970Z'
disclosed_at: '2020-08-19T11:02:28.855Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Denial of Service when entring an Array in email at seetings

## Metadata

- HackerOne Report ID: 961997
- Weakness: 
- Program: nextcloud
- Disclosed At: 2020-08-19T11:02:28.855Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

in settings `https://demo2.nextcloud.com/index.php/settings/users/TweLbFT93aqRnEfF/settings`
when you submit the request with email value Array the server return `500 Internal Server Error`
Poc video:
F954435

## Impact

denial a service attack on the server. This may lead to the website becoming slow or unresponsive.

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
