---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '97535'
original_report_id: '97535'
title: List of devices is accessible regardless of the account limitations
weakness: Information Disclosure
team_handle: shopify
created_at: '2015-11-04T00:29:53.767Z'
disclosed_at: '2015-11-10T22:44:06.488Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# List of devices is accessible regardless of the account limitations

## Metadata

- HackerOne Report ID: 97535
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2015-11-10T22:44:06.488Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

List of devices is accessible regardless of the account limitations.

**PoC**

. Create a limited account A with no rights.
. Log some devices with a different account B.
. From account A, GET /admin/mobile_devices.json.
. List of devices.

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
