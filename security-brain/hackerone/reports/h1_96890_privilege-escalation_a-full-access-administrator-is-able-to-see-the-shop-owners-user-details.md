---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '96890'
original_report_id: '96890'
title: A 'Full access' administrator is able to see the shop owners user details
weakness: Privilege Escalation
team_handle: shopify
created_at: '2015-10-30T23:05:30.461Z'
disclosed_at: '2015-11-10T23:17:24.278Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# A 'Full access' administrator is able to see the shop owners user details

## Metadata

- HackerOne Report ID: 96890
- Weakness: Privilege Escalation
- Program: shopify
- Disclosed At: 2015-11-10T23:17:24.278Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
====

A 'Full access' administrator is usually forbidden to see the shop owners user profile. But the endpoint `shop.myshopify.com/admin/users.json` does disclose the shop owners profile. As the user listing includes all fields of users this does leak the user details of the shop owner.

A direct query to `shop.myshopify.com/admin/users/{USERID}.json` does however honer the fact that this shouldn't be allowed by returning `{ "error": "Forbidden from viewing user" }`.

Mitigation
====
Filter out the shop owner from the user listing provided by the `/admin/users.json` endpoint for 'Full access' administrators.

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
