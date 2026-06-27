---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '211149'
original_report_id: '211149'
title: Inadequate/dangerous jQuery behavior
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2017-03-06T17:29:32.745Z'
disclosed_at: '2017-04-05T19:54:51.888Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- violation-of-secure-design-principles
---

# Inadequate/dangerous jQuery behavior

## Metadata

- HackerOne Report ID: 211149
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-04-05T19:54:51.888Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Every text/javascript response gets executed. JQuery 1.10.2 is vulnerable and executes response received.
https://assets.gratipay.com/jquery.min.js?etag=YoBy5yEtsejNrLIrIXUs2g~~

https://github.com/jquery/jquery/issues/2432

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
