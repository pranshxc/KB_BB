---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1168191'
original_report_id: '1168191'
title: Insecure File Creation Mask
weakness: Insecure Temporary File
team_handle: versa-networks
created_at: '2018-05-12T00:00:00.000Z'
disclosed_at: '2021-05-05T20:19:51.008Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- insecure-temporary-file
---

# Insecure File Creation Mask

## Metadata

- HackerOne Report ID: 1168191
- Weakness: Insecure Temporary File
- Program: versa-networks
- Disclosed At: 2021-05-05T20:19:51.008Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In VOS and overly permissive "umask" may allow for authorized users of the server to gain unauthorized access through insecure file permissions that can result in an arbitrary read, write, or execution of newly created files and directories.
Insecure umask setting was present throughout the Versa servers.
Example shell excerpt
admin@na73versadir01:~$ umask
0022
admin@na73versadir01:~$ umask -S
u=rwx,g=rx,o=rx

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
