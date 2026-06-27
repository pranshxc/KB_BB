---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '781614'
original_report_id: '781614'
title: subdomain takeover at status-stage0.stripo.email
weakness: Privilege Escalation
team_handle: stripo
created_at: '2020-01-23T15:40:37.720Z'
disclosed_at: '2020-01-30T10:14:21.187Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: stripo.email
asset_type: URL
max_severity: medium
tags:
- hackerone
- privilege-escalation
---

# subdomain takeover at status-stage0.stripo.email

## Metadata

- HackerOne Report ID: 781614
- Weakness: Privilege Escalation
- Program: stripo
- Disclosed At: 2020-01-30T10:14:21.187Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The subdomain status-stage0.stripo.email was pointed at uptimerobot.com
whereas it was not being used , but having Cname record as stats.uptimerobot.com .
Hence anyone can takeover it.

I have parked it with an account on uptimerobot.com
note : 
this issue is similar to [report](https://hackerone.com/reports/737695)
but with another subdomain

## Impact

Subdomain takeover can be abused to do several things like :

Malware distribution
Phishing / Spear phishing
XSS
Authentication bypass
Legitimate mail sending and receiving on behalf of ford subdomain
...
List goes on and on

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
