---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116352'
original_report_id: '116352'
title: nginx SPDY heap buffer overflow for https://grtp.co/
weakness: Memory Corruption - Generic
team_handle: gratipay
created_at: '2016-02-14T10:11:09.188Z'
disclosed_at: '2016-02-15T22:07:20.090Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- memory-corruption-generic
---

# nginx SPDY heap buffer overflow for https://grtp.co/

## Metadata

- HackerOne Report ID: 116352
- Weakness: Memory Corruption - Generic
- Program: gratipay
- Disclosed At: 2016-02-15T22:07:20.090Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

A heap-based buffer overflow in the SPDY implementation in nginx 1.3.15 before 1.4.7 and 1.5.x before 1.5.12 allows remote attackers to execute arbitrary code via a crafted request. The problem affects nginx compiled with the ngx_http_spdy_module module (which is not compiled by default) and without --with-debug configure option, if the "spdy" option of the "listen" directive is used in a configuration file.
This vulnerability affects Web Server. 

Current version is : nginx/1.4.6

The impact of this vulnerability:
An attacker can cause a heap memory buffer overflow in a worker process by using a specially crafted request, potentially resulting in arbitrary code execution.

How to fix this vulnerability:
Upgrade nginx to the latest version of apply the patch provided by the vendor.

Screenshots attached for the reference.

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
