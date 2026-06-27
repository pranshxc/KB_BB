---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '282518'
original_report_id: '282518'
title: Memory Corruption via Large Pixels
weakness: Classic Buffer Overflow
team_handle: infogram
created_at: '2017-10-24T15:04:24.266Z'
disclosed_at: '2024-02-01T15:41:38.853Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- classic-buffer-overflow
---

# Memory Corruption via Large Pixels

## Metadata

- HackerOne Report ID: 282518
- Weakness: Classic Buffer Overflow
- Program: infogram
- Disclosed At: 2024-02-01T15:41:38.853Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a memory corruption issue.

#PoC:
The exploit is really simple. I have an image of 5kb, 260x260 pixels. In the image itself I exchange the 260x260 values with 0xfafa x 0xfafa (so 64250x64250 pixels). Now from what I remember your service tries to convert the image once uploaded. By loading the 'whole image' into memory, it tries to allocate 4128062500 pixels into memory. which may cause some backend processing memory corruption issues.

Please have a look on attached video.

#Fix:
Proper resolution checks on image uploads.

Regards,
Mr.R3boot.

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
