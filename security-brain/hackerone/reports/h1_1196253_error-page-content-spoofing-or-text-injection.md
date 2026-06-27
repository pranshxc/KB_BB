---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1196253'
original_report_id: '1196253'
title: Error Page Content Spoofing or Text Injection
team_handle: sifchain
created_at: '2021-05-13T19:03:40.474Z'
disclosed_at: '2021-06-15T23:51:36.681Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
tags:
- hackerone
---

# Error Page Content Spoofing or Text Injection

## Metadata

- HackerOne Report ID: 1196253
- Weakness: 
- Program: sifchain
- Disclosed At: 2021-06-15T23:51:36.681Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

i want to report a context spoofing or text injection at   api-cryptoeconomics.sifchain.finance and   market-data.sifchain.finance

steps to reproduce:
1: Just browse this target on any browser
2: Target:  https://api-cryptoeconomics.sifchain.finance/ 
3: Then add any text or content after the "/" , i added this content
4: For example: !!!ATENTION!This_server_is_on_Maintenance_please_go_to_WWW.EVIL.COM
5: Now browser reflect the content or text which you add in url.

Repeat the same process for https://market-data.sifchain.finance/

You can see also image which i had attached
F1300496
F1300495

## Impact

Fix & Mitigation:
Fix 404 error page to a new who not allow text content injection

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
