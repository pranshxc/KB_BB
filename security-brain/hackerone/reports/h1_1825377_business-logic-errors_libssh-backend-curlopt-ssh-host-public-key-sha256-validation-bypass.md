---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1825377'
original_report_id: '1825377'
title: libssh backend CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 validation bypass
weakness: Business Logic Errors
team_handle: curl
created_at: '2023-01-07T01:05:51.501Z'
disclosed_at: '2023-01-07T21:04:06.121Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# libssh backend CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 validation bypass

## Metadata

- HackerOne Report ID: 1825377
- Weakness: Business Logic Errors
- Program: curl
- Disclosed At: 2023-01-07T21:04:06.121Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
If libcurl is built against libssh `CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256` is quietly ignored. As a result a SSH connection will be established even if the SHA256 key set doesn't match.

## Steps To Reproduce:

  1. configure libcurl with libssh and build it
  2. `curl --hostpubsha256 HOSTFINGERPRINTHERE sftp://example.tld/`

Instead of  failing due to mismatching fingerprint the connection quietly continues.

While the `CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256 ` documentation does mention that this option `Requires the libssh2 backend`, it is still wrong to quietly ignore the validation.

## Remediation

Change `lib/vssh/libssh.c` `myssh_is_known` to reject connection if `CURLOPT_SSH_HOST_PUBLIC_KEY_SHA256` is set, or implement sha256 fingerprint support for libssh.

## Impact

SSH host validation bypass.

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
