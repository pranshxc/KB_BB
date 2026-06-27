---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2070810'
original_report_id: '2070810'
title: Potential NULL dereference in libssh's sftp server
weakness: NULL Pointer Dereference
team_handle: ibb
created_at: '2023-07-16T02:48:18.989Z'
disclosed_at: '2023-09-14T16:33:24.916Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: https://git.libssh.org/
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- null-pointer-dereference
---

# Potential NULL dereference in libssh's sftp server

## Metadata

- HackerOne Report ID: 2070810
- Weakness: NULL Pointer Dereference
- Program: ibb
- Disclosed At: 2023-09-14T16:33:24.916Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Missing allocation check in sftp server processing read requests may
cause NULL dereference on low-memory conditions. The malicious client
can request up to 4GB SFTP reads, causing allocation of up to 4GB buffers,
which is being unchecked for failure.

## Impact

This will likely crash the authenticated user sftp server's connection
(if implemented as forking as we recommend). For thread-based
servers, this might cause DoS also for legitimate users.

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
