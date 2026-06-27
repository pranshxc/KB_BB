---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1536936'
original_report_id: '1536936'
title: Unprotected Direct Object Reference
weakness: Insecure Direct Object Reference (IDOR)
team_handle: mtn_group
created_at: '2022-04-11T00:18:26.759Z'
disclosed_at: '2022-12-01T17:24:05.518Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: mtnonline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Unprotected Direct Object Reference

## Metadata

- HackerOne Report ID: 1536936
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: mtn_group
- Disclosed At: 2022-12-01T17:24:05.518Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello MTN Security Team,
During my hunting,
I discovered that there's an Insecure Direct Object Reference  on https://nin.mtnonline.com 
Vulnerable Path:  https://nin.mtnonline.com/nin/success?message=1

Steps To Reproduce:
You may not even require to submit any NIN before accessing this unprotected page,
Just visit https://nin.mtnonline.com/nin/success?message=1 

I discovered that, to  see other user's NIN, it only require 2 difference , example
https://nin.mtnonline.com/nin/success?message=3
https://nin.mtnonline.com/nin/success?message=5
https://nin.mtnonline.com/nin/success?message=7
https://nin.mtnonline.com/nin/success?message=9
https://nin.mtnonline.com/nin/success?message=11
https://nin.mtnonline.com/nin/success?message=1901
https://nin.mtnonline.com/nin/success?message=1903
https://nin.mtnonline.com/nin/success?message=8001

## Impact

This bug exposed all the submitted Nigerians National Identity Number (NIN) .which can be abused in other way else if found out by a malicious person

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
