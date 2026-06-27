---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1536901'
original_report_id: '1536901'
title: Self XSS in attachments name
team_handle: acronis
created_at: '2022-04-10T22:01:58.810Z'
disclosed_at: '2022-05-31T09:10:35.148Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Self XSS in attachments name

## Metadata

- HackerOne Report ID: 1536901
- Weakness: 
- Program: acronis
- Disclosed At: 2022-05-31T09:10:35.148Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Gents,
> + While testing `account.acronis.com` I found that I could inject XSS payload in attachments name at  **"Support requests"** .

### Steps to Reproduce:
1. Please Login at `account.acronis.com`.
2. From support request, support a new case.
3. Expand Case ID,  Leave a comment for support professional, upload a file: `"><img src="x" onerror="alert(document.domain)">.png`.


### Proof of Concept:
{F1687467}

## Impact

XSS

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
