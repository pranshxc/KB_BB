---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '345152'
original_report_id: '345152'
title: Publicly Accessible Datadog link
weakness: Information Disclosure
team_handle: shopify
created_at: '2018-04-30T19:04:04.428Z'
disclosed_at: '2018-06-15T17:37:55.437Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: '*.shopify.io'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- information-disclosure
---

# Publicly Accessible Datadog link

## Metadata

- HackerOne Report ID: 345152
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2018-06-15T17:37:55.437Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

During my daily scanning of shopify and shopify's internal domain (Shopify.io), I landed on a personal bookmark of an employee: █████████ who works at `Guru at Shopify`. 

The link for personal bookmark is here: ███

There is a personal bookmark called `██████████`. When going to the link: ████████ it loaded some stats about chat and talks: 

{F292195}

## Impact

Leak of statistics regarding how many calls are waiting in support, how many are handled, average wait time etc.

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
