---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1256371'
original_report_id: '1256371'
title: PII data Leakage through hackerone reports
weakness: Information Disclosure
team_handle: security
created_at: '2021-07-09T20:24:59.928Z'
disclosed_at: '2021-08-09T20:03:00.042Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# PII data Leakage through hackerone reports

## Metadata

- HackerOne Report ID: 1256371
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2021-08-09T20:03:00.042Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Summary:

I found PII data leakage through the HackerOne report. I found a link in one of the disclosed report that allow me to get the address and phone numbers of security researchers. Here I got the address and phone number of ████ (███)


Vulnerability Name: PII data Leakage through

##Steps to reproduce:
—>Just visit ███
—>You will find a link swag link there.  (Refer: Screenshot 1)
—>Now visit the swag link ie. ██████████ and add a parameter there ██████████ 
—> link becomes : ████████
—>You will get the PII of researchers.  (Refer: Screenshot 2)

##Fix
1.)████████ should be informed that the data might have leaked. 
2.)Link should be redacted.
3.) When hackerone provides swag to researchers they should mention to keep the link strictly confidential , 
same information should also be provided to the programs on HackerOne , that offer swag.

## Impact

An attacker can get sensitive information about the other researchers like their addresses and phone number.

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
