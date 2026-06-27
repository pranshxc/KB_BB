---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145278'
original_report_id: '145278'
title: xss in https://www.uber.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-06-17T01:13:29.847Z'
disclosed_at: '2016-07-25T17:43:50.528Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 64
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss in https://www.uber.com

## Metadata

- HackerOne Report ID: 145278
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-07-25T17:43:50.528Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,

this vulnerability is essentially the same as bug 145276, i'm reporting it again just in case.

there's a cross site scripting vulnerability in https://www.uber.com/.

steps to reproduce:

1.visit https://www.uber.com/?kxsrc=https%3A//beacon.krxd.net/optout_check%3Fcallback%3Dalert%28/XSSED/.source%29
2. wait until the page finishes loading
3.see the xss alert.

wonder it would be eligible for a bounty?

Cheers,
Mario

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
