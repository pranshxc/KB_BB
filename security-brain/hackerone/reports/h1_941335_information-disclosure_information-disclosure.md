---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '941335'
original_report_id: '941335'
title: Information Disclosure
weakness: Information Disclosure
team_handle: mailru
created_at: '2020-07-24T14:03:45.397Z'
disclosed_at: '2020-11-25T09:39:26.478Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
asset_identifier: Foodplex
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Information Disclosure

## Metadata

- HackerOne Report ID: 941335
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2020-11-25T09:39:26.478Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application

www7.promo.plazius.ru

Steps to reproduce

1. By nmap port scanning we know port 9049 is open

2. After that dirsearch Metrics are shown result open in browser.

3.Now open http://www7.promo.plazius.ru:9049/Metrics Here you will get internal metrics of system

## Impact

This is quite difficult to know exactly what could be achieved as the infrastructure is complex. However, I would say that it could first enable an attacker to understand better your infrastructure and identify weaknesses. The other point is that if the attacker is able to perform some actions, this could lead to DoS of this service in some cases and, of course, unexpected behaviour (modfying env properties ...)

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
