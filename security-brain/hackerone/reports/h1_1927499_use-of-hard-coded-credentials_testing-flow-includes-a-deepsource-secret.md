---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1927499'
original_report_id: '1927499'
title: Testing flow includes a DeepSource secret
weakness: Use of Hard-coded Credentials
team_handle: weblate
created_at: '2023-03-31T14:07:19.687Z'
disclosed_at: '2023-04-11T10:40:02.683Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: https://github.com/WeblateOrg/wlc
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- use-of-hard-coded-credentials
---

# Testing flow includes a DeepSource secret

## Metadata

- HackerOne Report ID: 1927499
- Weakness: Use of Hard-coded Credentials
- Program: weblate
- Disclosed At: 2023-04-11T10:40:02.683Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The testing workflow (https://github.com/WeblateOrg/wlc/blob/main/.github/workflows/test.yml) has a DeepSource secret included which would allow a malicious actor to use the DeepSource cli and access parts of the repo (https://deepsource.io/docs/cli/usage).

Recommended usage would be to create a GitHub action environment secret and call this at runtime.
https://deepsource.io/docs/analyzer/test-coverage#with-github-actions

## Impact

Access to the DeepSource environment is gained through the token with the malicious actor able to report artifacts to DeepSource.

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
