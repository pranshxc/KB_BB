---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '131409'
original_report_id: '131409'
title: Certificate signed using SHA-1
team_handle: gratipay
created_at: '2016-12-10T00:44:05.860Z'
disclosed_at: '2016-12-29T21:17:35.070Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 3
tags:
- hackerone
---

# Certificate signed using SHA-1

## Metadata

- HackerOne Report ID: 131409
- Weakness: 
- Program: gratipay
- Disclosed At: 2016-12-29T21:17:35.070Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hello,
I detected a certificate signed using SHA-1. SHA-1 is a hash algorithm used in digital signatures. It is currently considered deprecated due to the increasing feasibility in breaking it. 

Impact:
Certificates can be forged by capable adversaries. 
Forged certificates can be used in MITM attacks against connecting clients. 

Solution:
Renew certificates with SHA-256 signatures. 
This should be done before 2016.

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
