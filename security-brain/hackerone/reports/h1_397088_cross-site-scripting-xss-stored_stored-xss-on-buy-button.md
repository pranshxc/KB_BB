---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '397088'
original_report_id: '397088'
title: Stored XSS on buy button
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2018-08-19T18:20:45.555Z'
disclosed_at: '2018-09-29T17:31:26.349Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on buy button

## Metadata

- HackerOne Report ID: 397088
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2018-09-29T17:31:26.349Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I found an XSS vulnerability on buy button.
**Steps to reproduce**
Go to Settings > General > Store currency > Change formatting and add on "HTML with currency" the payload `€{{amount}} "><img src=x onerror=prompt(document.domain)>`
After that go to buy button and you will see that the payload triggers there.

## Impact

A staff member can takeover another account.

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
