---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '911857'
original_report_id: '911857'
title: increased privileges on staff account
team_handle: shopify
created_at: '2020-06-30T13:23:00.957Z'
disclosed_at: '2020-08-24T16:05:40.795Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: partners.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# increased privileges on staff account

## Metadata

- HackerOne Report ID: 911857
- Weakness: 
- Program: shopify
- Disclosed At: 2020-08-24T16:05:40.795Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

staff on partners without a store management permit can have access to the collaboration shop

## steps for reproduction
1. Invite staff to partners without store management permission
2. accept the invitation and the staff has become a member of the partner
3. On the staff account, try to access the collaboration store that has been active with partners
4. staff can enter and have permissions according to those owned by the partner account

## Impact

gives staff unauthorized access to see anything in the collaboration shop

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
