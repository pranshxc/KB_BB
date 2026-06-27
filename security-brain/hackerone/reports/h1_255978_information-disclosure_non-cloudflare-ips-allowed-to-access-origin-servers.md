---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '255978'
original_report_id: '255978'
title: Non-Cloudflare IPs allowed to access origin servers
weakness: Information Disclosure
team_handle: unikrn
created_at: '2017-08-03T01:59:21.038Z'
disclosed_at: '2018-02-07T21:43:45.233Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: unikrn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Non-Cloudflare IPs allowed to access origin servers

## Metadata

- HackerOne Report ID: 255978
- Weakness: Information Disclosure
- Program: unikrn
- Disclosed At: 2018-02-07T21:43:45.233Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** Non-Cloudflare IPs allowed to access origin servers

**Description:** Your origin servers are not blocking access from non-Cloudflare servers. This way crawlers can find your origin servers' IPs by checking random IPs until they found your origin server(s).

What makes this especially easy are tools like censys.io (which can find your origin servers).

One of the origin server IPs I found is ███████ but there were quite a few others, too.

This attack vector can be extremely bad because with the IP found out an attacker could attack the servers by DDoS or other attacks without being stopped by CloudFlare.]

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
