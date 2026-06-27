---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '831353'
original_report_id: '831353'
title: tcpdump before 4.9.3 has a heap-based buffer over-read related to aoe_print
  in print-aoe.c and lookup_emem in addrtoname.c
weakness: Buffer Over-read
team_handle: ibb
created_at: '2020-03-25T15:43:57.976Z'
disclosed_at: '2021-07-23T05:14:50.320Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- buffer-over-read
---

# tcpdump before 4.9.3 has a heap-based buffer over-read related to aoe_print in print-aoe.c and lookup_emem in addrtoname.c

## Metadata

- HackerOne Report ID: 831353
- Weakness: Buffer Over-read
- Program: ibb
- Disclosed At: 2021-07-23T05:14:50.320Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There seems to be a heap-based buffer overread while running tcpdump on a crafted pcap file. A similar behavior is seen when tcpdump is listening on an interface and the contents of this file is relayed over the network.

Please find the detailed report on github
https://github.com/the-tcpdump-group/tcpdump/issues/645

CVE: https://nvd.nist.gov/vuln/detail/CVE-2017-16808

## Impact

Heap Over Read

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
