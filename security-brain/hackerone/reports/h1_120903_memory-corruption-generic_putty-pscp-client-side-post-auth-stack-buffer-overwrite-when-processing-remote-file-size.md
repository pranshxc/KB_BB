---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '120903'
original_report_id: '120903'
title: putty pscp client-side post-auth stack buffer overwrite when processing remote
  file size
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-03-06T10:10:58.684Z'
disclosed_at: '2019-11-12T23:54:51.809Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# putty pscp client-side post-auth stack buffer overwrite when processing remote file size

## Metadata

- HackerOne Report ID: 120903
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-11-12T23:54:51.809Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Not sure if this will qualify but it may impact a pretty broad audience given the fact that putty code is part of many other apps (filezilla, ...) and it is the defacto standalone ssh client for windows administrators (besides openssh cygwin)

putty <= 0.66; affects putty versions dating back ~9 years.

Vulnerability Note: https://github.com/tintinweb/pub/tree/master/pocs/cve-2016-2563
Vendor Security Notification: http://www.chiark.greenend.org.uk/~sgtatham/putty/wishlist/vuln-pscp-sink-sscanf.html

provided patch and PoC to vendor. was resolved within one week (which is very impressive!).

patch/poc will be released later today on this github account.

in total reported:
* mem-corruption/remote code execution via stack buffer overwrite in putty pscp (connect vulnerable putty to poc.py to trigger an EIP=0x41414141 (AAAA) bad instruction.
* DoS condition in the parsing of SSH-Strings (core packet handling) that lead to a nullptr read. (connect putty to poc.py and type x11exploit to trigger one occurrence of a crash)
* DoS condition in the handling of unrequested forwarded-tcpip channels open requests that lead to a nullptr read. (connect putty to poc.py and type forwardedtcpipcrash to trigger crash)

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
