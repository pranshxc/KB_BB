---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '592885'
original_report_id: '592885'
title: multiple vulnerabilities on your mautic server
team_handle: unikrn
created_at: '2019-05-30T20:58:58.986Z'
disclosed_at: '2019-07-10T14:24:33.699Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: crm.unikrn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# multiple vulnerabilities on your mautic server

## Metadata

- HackerOne Report ID: 592885
- Weakness: 
- Program: unikrn
- Disclosed At: 2019-07-10T14:24:33.699Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi @unikrn!
I found some vulnerabilities in you crm server:

1. By pass Cloudflare access:

You Use Cloudflare Access on https://crm.unikrn.com . 
BUt this link bypassed  Cloudflare Access:  ████████/login

This vulnerability generates the disclosure of important data:

PHP info page:
██████████phpinfo  -  an attacker can find out the server configuration and also find out the server path

Symfony request log:

█████empty/search/results?limit=10 list of all requests, IP addresses and so on.

Symfony debug log:
██████████6099a6?panel=logger

Symfony config:
█████6099a6?panel=config

## Impact

crm.unicrn.com  multiple vulnerabilities on your mautic server

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
