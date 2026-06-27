---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1459338'
original_report_id: '1459338'
title: Same the Url
team_handle: shopify
created_at: '2022-01-24T18:03:54.572Z'
disclosed_at: '2022-04-21T18:54:25.218Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# Same the Url

## Metadata

- HackerOne Report ID: 1459338
- Weakness: 
- Program: shopify
- Disclosed At: 2022-04-21T18:54:25.218Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
i found the /graphql path and /performance_report with the post method. when i will create page with name /graphql i am not allowed on the grounds it is reserved but i can create page with name performance_report.
although both use the same method but only /graphql cannot be created.

## Shops Used to Test:
https://linkpop.com/performance_report

## Steps To Reproduce:
1. login to https://linkpop.com
2. create page and use performance_report to profile page url.
3. and it will be created successfully

Best Regards,
@4bel

## Impact

It is clear that /performance_report should not be used like /graphql.

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
