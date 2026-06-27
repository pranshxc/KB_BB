---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '361976'
original_report_id: '361976'
title: DNS Misconfiguration
team_handle: mailru
created_at: '2018-06-05T05:29:00.800Z'
disclosed_at: '2018-08-16T17:11:18.678Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# DNS Misconfiguration

## Metadata

- HackerOne Report ID: 361976
- Weakness: 
- Program: mailru
- Disclosed At: 2018-08-16T17:11:18.678Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Your localhost.mail.ru has address 127.0.0.1 and this may lead to "Same- Site" Scripting.

Here is detailed description of this minor security issue (by Tavis Ormandy): http://www.securityfocus.com/archive/1/486606/30/0/threaded


I can also ping the localhost network from mail.ru, as in the image attachment "PING TO LOCALHOST MAIL RU.png"


Reference:
https://www.cybrary.it/0p3n/same-site-scripting-the-lesser-known-vulnerability/
https://hackerone.com/reports/1509

## Impact

Can ping to localhost network from mail.ru

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
