---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1113663'
original_report_id: '1113663'
title: Inadequate Cryptographic Key Size and Insecure Cryptographic Mode.  File Name
  :- curl_ntlm_core.c
weakness: Use of a Broken or Risky Cryptographic Algorithm
team_handle: curl
created_at: '2021-03-01T09:37:07.051Z'
disclosed_at: '2021-03-08T08:24:10.065Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 1
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- use-of-a-broken-or-risky-cryptographic-algorithm
---

# Inadequate Cryptographic Key Size and Insecure Cryptographic Mode.  File Name :- curl_ntlm_core.c

## Metadata

- HackerOne Report ID: 1113663
- Weakness: Use of a Broken or Risky Cryptographic Algorithm
- Program: curl
- Disclosed At: 2021-03-08T08:24:10.065Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

The application is generating cryptographic keys or key pairs using a short and inadequate length.
This application is using the ECB (Electronic Codebook) mode of operation to perform encryption, which is considered semantically insecure.

Vulnerable File name :- curl_ntlm_core.c
Vulnerable line no. 274 :- err = CCCrypt(kCCEncrypt, kCCAlgorithmDES, kCCOptionECBMode, key,

## Impact

If a message with identical blocks is encrypted, an attacker get a certain advantage to have information on plaintext, by only observing CipherText.

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
