---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '96908'
original_report_id: '96908'
title: An administrator without the 'Settings' permission is able to see payment gateways
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-10-30T23:46:24.189Z'
disclosed_at: '2015-11-18T20:58:31.135Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# An administrator without the 'Settings' permission is able to see payment gateways

## Metadata

- HackerOne Report ID: 96908
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-11-18T20:58:31.135Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
====
An administrator who lacks the 'Settings' permission is not able to see the shops payment gateways through the UI.  But the endpoint `shop.myshopify.com/admin/payment_gateways.json` does disclose payment gateways to the unprivileged user.

Mitigation
====
Restrict the endpoint in question to be only accessible with the correct permission set.

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
