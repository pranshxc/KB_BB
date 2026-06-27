---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1763817'
original_report_id: '1763817'
title: Take over subdomain undici.nodejs.org.cdn.cloudflare.net
weakness: Array Index Underflow
team_handle: nodejs
created_at: '2022-11-06T23:57:13.909Z'
disclosed_at: '2023-01-11T04:07:10.952Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- array-index-underflow
---

# Take over subdomain undici.nodejs.org.cdn.cloudflare.net

## Metadata

- HackerOne Report ID: 1763817
- Weakness: Array Index Underflow
- Program: nodejs
- Disclosed At: 2023-01-11T04:07:10.952Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

this is a pretty serious security issue in some contexts, so please act as soon as possible

Summary:

I just went to undici.nodejs.org, and I've also checked the IP of the main domain it goes to cdn.cloudflare.net which means if it's not added it can be added to any github account your subdomain should be added to your account so shows the URL you selected. This vulnerability is called subdomain takeover

•Remove CNAME records from DNS zone completely

Poc
http://undici.nodejs.org.cdn.cloudflare.net/

## Impact

Subdomain takeovers are abused for several purposes:

Malware distribution
•Phishing / Spear phishing
•XSS
•Bypass authentication
•...


The list goes on and on. Since some certificate authorities (Let's Encrypt) only require domain verification, SSL certificates can be generated easily.

Regards Algisec1337

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
