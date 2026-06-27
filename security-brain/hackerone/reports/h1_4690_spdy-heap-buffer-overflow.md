---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '4690'
original_report_id: '4690'
title: SPDY heap buffer overflow
team_handle: ibb
created_at: '2014-03-24T21:54:37.486Z'
disclosed_at: '2014-03-24T21:54:37.486Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: Nginx (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# SPDY heap buffer overflow

## Metadata

- HackerOne Report ID: 4690
- Weakness: 
- Program: ibb
- Disclosed At: 2014-03-24T21:54:37.486Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A bug in the experimental SPDY implementation in nginx was found, which might allow an attacker to cause a heap memory buffer overflow in a worker process by using a specially crafted request, potentially resulting in arbitrary code execution (CVE-2014-0133).

The problem affects nginx 1.3.15 - 1.5.11, compiled with the ngx_http_spdy_module module (which is not compiled by default) and without --with-debug configure option, if the "spdy" option of the "listen" directive is used in a configuration file.

The problem is fixed in nginx 1.5.12, 1.4.7.

Patch for the problem can be found here:

http://nginx.org/download/patch.2014.spdy2.txt

Thanks to Lucas Molas, researcher at Programa STIC, Fundación Dr. Manuel Sadosky, Buenos Aires, Argentina.

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
