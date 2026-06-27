---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '129436'
original_report_id: '129436'
title: xss in DM group name in twitter
weakness: Cross-site Scripting (XSS) - Generic
team_handle: x
created_at: '2016-04-09T07:22:40.389Z'
disclosed_at: '2016-04-22T18:08:10.933Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss in DM group name in twitter

## Metadata

- HackerOne Report ID: 129436
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: x
- Disclosed At: 2016-04-22T18:08:10.933Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

hi,

found a xss on twitter

Steps

1. Create a DM group with payload `<script>alert(1);//`

2. Whenever anybody shares a tweet via DM, XSS will popup

POC https://youtu.be/P2Ram2FBAS4

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
