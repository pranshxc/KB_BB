---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1405673'
original_report_id: '1405673'
title: Sidekiq dashboard exposed at notary.shopifycloud.com
weakness: Information Disclosure
team_handle: shopify
created_at: '2021-11-19T15:20:43.552Z'
disclosed_at: '2021-11-25T19:28:29.518Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: '*.shopifycloud.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- information-disclosure
---

# Sidekiq dashboard exposed at notary.shopifycloud.com

## Metadata

- HackerOne Report ID: 1405673
- Weakness: Information Disclosure
- Program: shopify
- Disclosed At: 2021-11-25T19:28:29.518Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi,

I found that the host https://notary.shopifycloud.com/ is exposing a sidekiq dashboard to the internet, for any unauthenticated user to use. I am not very familliar with Sidekiq, but from what I can tell its used for ruby background proccessing. 

I am fairly certain this dashboard is used to manage shopify instances, since browsing to `https://notary.shopifycloud.com/sidekiq/scheduled` reveals a list of jobs which domains as arguments. I checked a few of the domains and they all seem to be shopify hosts.

I have not tried stopping any of the proccesses in order to not cause any downtime or issues to shopify hosts.

██████████

## Impact

Stop workers & background processes for shopify hosts.

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
