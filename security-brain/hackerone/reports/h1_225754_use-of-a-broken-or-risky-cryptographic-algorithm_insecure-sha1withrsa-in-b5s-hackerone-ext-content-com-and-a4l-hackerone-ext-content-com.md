---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '225754'
original_report_id: '225754'
title: Insecure SHA1withRSA in b5s.hackerone-ext-content.com and a4l.hackerone-ext-content.com
weakness: Use of a Broken or Risky Cryptographic Algorithm
team_handle: security
created_at: '2017-05-03T05:34:43.326Z'
disclosed_at: '2017-06-21T23:52:04.313Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- use-of-a-broken-or-risky-cryptographic-algorithm
---

# Insecure SHA1withRSA in b5s.hackerone-ext-content.com and a4l.hackerone-ext-content.com

## Metadata

- HackerOne Report ID: 225754
- Weakness: Use of a Broken or Risky Cryptographic Algorithm
- Program: security
- Disclosed At: 2017-06-21T23:52:04.313Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello, 

I just found some minor issue with RSA 2048 bits (SHA1withRSA) in b5s.hackerone-ext-content.com and a4l.hackerone-ext-content.com thru Qualys SSL Labs and wanted to report it.

Proof of Concept

https://www.ssllabs.com/ssltest/analyze.html?d=b5s.hackerone-ext-content.com
Result: SHA1withRSA   INSECURE
https://www.ssllabs.com/ssltest/analyze.html?d=a4l.hackerone-ext-content.com
Result: SHA1withRSA   INSECURE

I hope you will fix this issue.

Cheers,
Evan

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
