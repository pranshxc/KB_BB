---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1087489'
original_report_id: '1087489'
title: Github access token exposure
team_handle: shopify
created_at: '2021-01-26T13:03:40.870Z'
disclosed_at: '2021-07-26T19:50:02.320Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1151
asset_identifier: accounts.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Github access token exposure

## Metadata

- HackerOne Report ID: 1087489
- Weakness: 
- Program: shopify
- Disclosed At: 2021-07-26T19:50:02.320Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

While dissecting an application made by one of your employees I found his GitHub Personal Access Token (PAT), he's a member of the org with pull and push access to all of your repositories. 
As a proof I can tell you that on the repo github.com/Shopify/shopify at commit hash `cea9c273391d` the sha512 of the README.md is `69750574bec56c1f1052db3471252b1daacdc9dda9f6d5332a3400a847fa413ec1caf19ef0b5501f18a5a76c232e7210d5f3b91c24c9439f4e0f64c02d6db824`.

## Impact

Read and write access to all your private github repositories.

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
