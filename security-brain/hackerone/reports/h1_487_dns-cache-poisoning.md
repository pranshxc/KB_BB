---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '487'
original_report_id: '487'
title: DNS Cache Poisoning
team_handle: security
created_at: '2013-12-01T00:58:34.856Z'
disclosed_at: '2014-01-09T14:36:41.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
tags:
- hackerone
---

# DNS Cache Poisoning

## Metadata

- HackerOne Report ID: 487
- Weakness: 
- Program: security
- Disclosed At: 2014-01-09T14:36:41.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I noticed if I made a request to your website, intercepted the request, and added the header...
X-Forwarded-Host: evil.com
it would redirect me to evil.com. Well, after that, I tried going to hackerone.com and I was instantly redirected to evil.com. This is a result of DNS cache poisoning.

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
