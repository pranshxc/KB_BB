---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1787644'
original_report_id: '1787644'
title: Any organization's assets pending review can be downloaded
weakness: Information Disclosure
team_handle: security
created_at: '2022-11-29T02:20:24.108Z'
disclosed_at: '2022-11-29T18:36:13.305Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 71
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Any organization's assets pending review can be downloaded

## Metadata

- HackerOne Report ID: 1787644
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2022-11-29T18:36:13.305Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Steps to reproduce
- sign in as any user
- visit https://hackerone.com/organizations/:handle/assets/download_pending_reviews.csv, where `:handle` is the organization you want to download the assets for

## Impact

This may leak sensitive data about an organization's attack surface.

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
