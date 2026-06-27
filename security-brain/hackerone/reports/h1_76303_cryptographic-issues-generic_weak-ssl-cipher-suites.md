---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '76303'
original_report_id: '76303'
title: weak ssl cipher suites
weakness: Cryptographic Issues - Generic
team_handle: gratipay
created_at: '2015-07-17T19:00:50.857Z'
disclosed_at: '2015-09-13T16:41:44.657Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cryptographic-issues-generic
---

# weak ssl cipher suites

## Metadata

- HackerOne Report ID: 76303
- Weakness: Cryptographic Issues - Generic
- Program: gratipay
- Disclosed At: 2015-09-13T16:41:44.657Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

> i found that some of the cipher suites are weak on you domain.
>
Here are those ( WEAK ):
DH 1024 bits (p: 128, g: 128, Ys: 128)   FS   WEAK
POC: https://www.ssllabs.com/ssltest/analyze.html?d=gratipay.com&s=23.23.184.160&latest

([original on Freshdesk](https://gratipay.freshdesk.com/helpdesk/tickets/2449))

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
