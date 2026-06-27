---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '439174'
original_report_id: '439174'
title: Verbose PHP error messages exposed on a blog article
weakness: Information Exposure Through an Error Message
team_handle: security
created_at: '2018-11-11T18:46:14.814Z'
disclosed_at: '2019-04-10T21:33:50.552Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-exposure-through-an-error-message
---

# Verbose PHP error messages exposed on a blog article

## Metadata

- HackerOne Report ID: 439174
- Weakness: Information Exposure Through an Error Message
- Program: security
- Disclosed At: 2019-04-10T21:33:50.552Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey guys!

For what its worth, warning messages aren't suppressed on the /blog/ endpoint, giving verbose PHP
error messages when visiting a blog article such as https://www.hackerone.com/blog/H1-702-2018-makes-history-over-500K-bounties-paid.

{F374066}

## Impact

Not much impact, just disclosures of paths and technologies used (Drupal, Symphony)

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
