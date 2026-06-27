---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '9522'
original_report_id: '9522'
title: https://polldaddy.com storage.swf XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: automattic
created_at: '2014-04-24T10:34:45.449Z'
disclosed_at: '2014-07-08T10:00:26.819Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# https://polldaddy.com storage.swf XSS

## Metadata

- HackerOne Report ID: 9522
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: automattic
- Disclosed At: 2014-07-08T10:00:26.819Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found a flash based XSS located here :
`https://polldaddy.com/swf/storage.swf?onload=alert(1)`

It happends in the `ExternalInterface.Call` Function, when a parameter is inserted unfiltered it will allow XSS, you can patch it by only allowing :
A-Z a-z 0-9

Best regards,

Olivier Beg

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
