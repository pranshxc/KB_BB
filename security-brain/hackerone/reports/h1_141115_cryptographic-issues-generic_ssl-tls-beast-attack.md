---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '141115'
original_report_id: '141115'
title: SSL/TLS BEAST ATTACK
weakness: Cryptographic Issues - Generic
team_handle: drchrono
created_at: '2016-05-26T05:34:55.665Z'
disclosed_at: '2018-04-09T20:41:04.937Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- cryptographic-issues-generic
---

# SSL/TLS BEAST ATTACK

## Metadata

- HackerOne Report ID: 141115
- Weakness: Cryptographic Issues - Generic
- Program: drchrono
- Disclosed At: 2018-04-09T20:41:04.937Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Supported versions:
 TLSv1.0 TLSv1.1 TLSv1.2
Deflate compression: no
Supported cipher suites (ORDER IS NOT SIGNIFICANT):
  TLSv1.0
     RSA_WITH_3DES_EDE_CBC_SHA
     RSA_WITH_AES_128_CBC_SHA
     RSA_WITH_AES_256_CBC_SHA
     TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA
     TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
     TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
  (TLSv1.1: idem)
  TLSv1.2
     RSA_WITH_3DES_EDE_CBC_SHA
     RSA_WITH_AES_128_CBC_SHA
     RSA_WITH_AES_256_CBC_SHA
     RSA_WITH_AES_128_CBC_SHA256
     RSA_WITH_AES_256_CBC_SHA256
     TLS_RSA_WITH_AES_128_GCM_SHA256
     TLS_RSA_WITH_AES_256_GCM_SHA384
     TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA
     TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
     TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
     TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
     TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
     TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
     TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
----------------------
Server certificate(s):
  4784741821c06e5af52b053fd6362db38c222df3: CN=*.drchrono.com, O=Drchrono Inc., L=Mountain View, S=California, C=US
----------------------
Minimal encryption strength:     strong encryption (96-bit or more)
Achievable encryption strength:  strong encryption (96-bit or more)
BEAST status: vulnerable <<<<<<<<<<<<<<<<<<<< patch it
CRIME status: protected

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
