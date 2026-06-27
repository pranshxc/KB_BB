---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '194832'
original_report_id: '194832'
title: Authentication Bypass on monitoring server
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2016-12-30T15:18:38.917Z'
disclosed_at: '2017-01-11T17:42:10.851Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- improper-authentication-generic
---

# Authentication Bypass on monitoring server

## Metadata

- HackerOne Report ID: 194832
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2017-01-11T17:42:10.851Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

This issue has the same impact as this one: #143482. But the fix is not complete, there is a shopify subdomain (VPN server) where you still can connect your google account. This should be hide and protected.

So you guys need to change this so that only shopify.com Google accounts are accepted.

POC screen: ███████

Let me know about it and happy new year!!


Jamesclyde90

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
