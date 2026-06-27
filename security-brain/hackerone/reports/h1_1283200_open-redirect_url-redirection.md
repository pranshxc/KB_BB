---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1283200'
original_report_id: '1283200'
title: url redirection
weakness: Open Redirect
team_handle: upchieve
created_at: '2021-07-29T14:12:20.642Z'
disclosed_at: '2021-07-30T14:33:20.075Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
asset_identifier: argocd.upchieve.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# url redirection

## Metadata

- HackerOne Report ID: 1283200
- Weakness: Open Redirect
- Program: upchieve
- Disclosed At: 2021-07-30T14:33:20.075Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
[the following url is vulnerable to redirect]

https://app.upchieve.org

## Steps To Reproduce:
when you add @evil.com the user will be directed to evil.com
https://app.upchieve.org@evil.com

## Impact

Users could get redirected to malicious domain

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
