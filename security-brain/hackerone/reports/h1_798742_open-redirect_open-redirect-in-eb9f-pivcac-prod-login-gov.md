---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '798742'
original_report_id: '798742'
title: open redirect in eb9f.pivcac.prod.login.gov
weakness: Open Redirect
team_handle: gsa_bbp
created_at: '2020-02-18T11:03:46.716Z'
disclosed_at: '2020-05-12T18:19:43.519Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.login.gov'
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# open redirect in eb9f.pivcac.prod.login.gov

## Metadata

- HackerOne Report ID: 798742
- Weakness: Open Redirect
- Program: gsa_bbp
- Disclosed At: 2020-05-12T18:19:43.519Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

poc:
```
https://eb9f.pivcac.prod.login.gov/?nonce=wI0UglN84A06Q4z4JnkZVc3i1V8%3D&redirect_uri=https%3A%2F%2Fgoogle.com%23%40secure.login.gov%2Flogin%2Fpiv_cac
```
visit this and will redirect to google.com

## Impact

phishing

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
