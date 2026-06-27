---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '774872'
original_report_id: '774872'
title: Configuartion [Sensitive] Information Disclosure
weakness: Information Disclosure
team_handle: kubernetes
created_at: '2020-01-14T17:28:02.990Z'
disclosed_at: '2020-10-22T18:11:12.362Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: prow.k8s.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Configuartion [Sensitive] Information Disclosure

## Metadata

- HackerOne Report ID: 774872
- Weakness: Information Disclosure
- Program: kubernetes
- Disclosed At: 2020-10-22T18:11:12.362Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Report Submission Form

Hello Team,

The Configuration Details are being leaked by the following url:  https://prow.k8s.io/config

## Steps to Reproduce

Click on the Below link to reproduce the issue - 
https://prow.k8s.io/config

## Impact

The Sensitive Information is being leaked. This information can be used to launch further attacks.

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
