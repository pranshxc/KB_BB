---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1187001'
original_report_id: '1187001'
title: Email spoofing
weakness: Improper Authentication - Generic
team_handle: sifchain
created_at: '2021-05-07T06:14:37.485Z'
disclosed_at: '2021-05-13T10:20:43.792Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Email spoofing

## Metadata

- HackerOne Report ID: 1187001
- Weakness: Improper Authentication - Generic
- Program: sifchain
- Disclosed At: 2021-05-13T10:20:43.792Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Email spoofing is possible
To verify:
visit :https://www.kitterman.com/spf/validate.html? and type your domain name to check SPF record 
you can see the results as: NO valid SPF record found
POC:
1.visit http://emkei.cz//
2.fill the from email as admin@sifchain.finance
3.to email as victim email address, enter subject, data and click send
4.you will receive the mail in your inbox

## Impact

email spoofing

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
