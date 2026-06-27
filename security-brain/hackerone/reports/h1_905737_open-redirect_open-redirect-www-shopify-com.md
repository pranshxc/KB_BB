---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '905737'
original_report_id: '905737'
title: Open Redirect - www.shopify.com
weakness: Open Redirect
team_handle: shopify
created_at: '2020-06-22T23:26:02.859Z'
disclosed_at: '2020-07-14T21:15:20.708Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- open-redirect
---

# Open Redirect - www.shopify.com

## Metadata

- HackerOne Report ID: 905737
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2020-07-14T21:15:20.708Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Shopify team,

I found an open redirect in www.shopify.com

Link:

- `https://www.shopify.com/plus/get-cdn-asset?asset=http://evil.com/?`

**Vulnerable parameter:** `asset`

## Impact

- Open redirect that can lead to phishing and other type of attacks.

Have a good day, zonduu.

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
