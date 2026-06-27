---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1808596'
original_report_id: '1808596'
title: Multiple OpenSSL error handling issues in nodejs crypto library
weakness: Cryptographic Issues - Generic
team_handle: nodejs
created_at: '2022-12-16T21:14:34.485Z'
disclosed_at: '2023-02-17T18:04:53.656Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cryptographic-issues-generic
---

# Multiple OpenSSL error handling issues in nodejs crypto library

## Metadata

- HackerOne Report ID: 1808596
- Weakness: Cryptographic Issues - Generic
- Program: nodejs
- Disclosed At: 2023-02-17T18:04:53.656Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** NodeJS up to 19.2.0 does not clear the OpenSSL error stack after operations that may set it

**Description:** NodeJS up to 19.2.0 does not clear the OpenSSL error stack after operations that may set it. This may lead to false positive errors during subsequent cryptographic operations that happen to be on the same thread.

## Steps To Reproduce:

The following issues have reproduction cases:

https://github.com/nodejs/node/pull/45495
https://github.com/nodejs/node/pull/45377

Upon reviewing the code in crypto_x509.cc, at least one other function lacks use of ClearErrorOnReturn - X509Certificate::CheckPrivateKey.

https://github.com/nodejs/node/blob/main/src/crypto/crypto_x509.cc#L432

## Impact:

On our application, JWTs failed to sign after a certificate fails to verify on the same thread.

## Impact

If the server verifies certificates using Node's X509Certificate API, it may fail to sign other users' auth tokens: if a certificate fails to verify, the error from the previous failing call is applied to the next call that should succeed. It is worth auditing all OpenSSL entry points to see if they can cause errors to be raised.

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
