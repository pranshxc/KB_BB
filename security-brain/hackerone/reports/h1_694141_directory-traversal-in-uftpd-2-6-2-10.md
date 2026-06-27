---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '694141'
original_report_id: '694141'
title: Directory Traversal in uftpd 2.6-2.10
team_handle: redact
created_at: '2019-08-31T23:42:54.000Z'
disclosed_at: '2020-03-03T16:05:12.716Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 136
tags:
- hackerone
---

# Directory Traversal in uftpd 2.6-2.10

## Metadata

- HackerOne Report ID: 694141
- Weakness: 
- Program: redact
- Disclosed At: 2020-03-03T16:05:12.716Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Description

It is possible for an unauthenticated user to perform a directory traversal attack using multiple different FTP commands and read and write to arbitrary locations on the filesystem due to improper path sanitization in the chroot jail implementation in `common.c`'s `compose_abspath`.

# Impact

An attacker could abuse these vulnerabilities to potentially:
* read and write to arbitrary locations on the filesystem
* leak memory through /proc/self
* obtain remote code execution

# Reproduction Steps
## Manual Verification

To reproduce this vulnerability, connect via `netcat <ip> <port>` and write the following to the FTP server socket:

```
MKD ../../../../../tmp/itworked
```

Then, `ls /tmp/itworked` from terminal to verify that the folder was created. `MKD` is one of the many vulnerable FTP commands.

## Automated PoC Exploit

I wrote a script in Python to automate the process of obtaining remote code execution through this vulnerability. It is available here: https://github.com/Arinerron/uftp_dirtrav/blob/master/uftpd_dirtrav.py

# Mitigation

Properly sanitize paths to prevent users from being able to escape the chroot jail.

An analysis of the root cause is available at https://arinerron.com/blog/posts/6

# References

* Blog post: https://arinerron.com/blog/posts/6
* Commit that fixes the directory traversal regression: https://github.com/troglobit/uftpd/commit/455b47d3756aed162d2d0ef7f40b549f3b5b30fe

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
