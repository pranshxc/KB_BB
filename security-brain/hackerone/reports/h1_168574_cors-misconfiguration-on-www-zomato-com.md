---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '168574'
original_report_id: '168574'
title: CORS Misconfiguration on www.zomato.com
team_handle: zomato
created_at: '2016-09-15T11:24:28.321Z'
disclosed_at: '2017-06-30T04:52:12.475Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 28
tags:
- hackerone
---

# CORS Misconfiguration on www.zomato.com

## Metadata

- HackerOne Report ID: 168574
- Weakness: 
- Program: zomato
- Disclosed At: 2017-06-30T04:52:12.475Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The website at https://www.zomato.com tries to use Cross-Origin Resource Sharing (CORS) to allow cross-domain access from all subdomains of zomato.com. However, due to a flaw in the implementation, it actually allows cross-domain access from all domains ending in zomato.com including notzomato.com as shown in the attached screenshot.

This means anyone who could be bothered registering a domain ending in zomato.com can read arbitrary data from the accounts of other users. 

To resolve this issue, simply require that origins end in .zomato.com rather than zomato.com

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
