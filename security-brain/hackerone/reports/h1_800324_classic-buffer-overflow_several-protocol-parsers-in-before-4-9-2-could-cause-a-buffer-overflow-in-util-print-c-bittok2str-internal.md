---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '800324'
original_report_id: '800324'
title: Several protocol parsers in before 4.9.2 could cause a buffer overflow in util-print.c:bittok2str_internal()
weakness: Classic Buffer Overflow
team_handle: ibb
created_at: '2020-02-20T06:27:05.183Z'
disclosed_at: '2021-08-22T03:50:13.318Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- classic-buffer-overflow
---

# Several protocol parsers in before 4.9.2 could cause a buffer overflow in util-print.c:bittok2str_internal()

## Metadata

- HackerOne Report ID: 800324
- Weakness: Classic Buffer Overflow
- Program: ibb
- Disclosed At: 2021-08-22T03:50:13.318Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Length of a local buffer used to parse network packets was not validated against actual payload size leading to a classic buffer overflow.

P.S. I was not aware of this bounty program at the time of reporting. Is this report in scope? I have a few more reports that were originally sent to the tcpdump security mailing list, I could file a report for each of them here if that qualifies. I may have also helped fix some issues in 4.9.3 as well.

## Impact

I believe remote DoS is possible. Remote code execution remains a possibility but I have not checked this myself.

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
