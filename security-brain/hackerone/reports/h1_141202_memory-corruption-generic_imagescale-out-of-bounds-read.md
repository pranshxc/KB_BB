---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '141202'
original_report_id: '141202'
title: imagescale out-of-bounds read
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-05-26T14:35:56.958Z'
disclosed_at: '2019-10-31T06:15:50.017Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# imagescale out-of-bounds read

## Metadata

- HackerOne Report ID: 141202
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-31T06:15:50.017Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=72227

Invalid memory access while applying bicubic scaling on images.

```
Reading symbols from /home/user/php-7.0/sapi/cli/php...done.
(gdb) b gd_interpolation.c:890
Breakpoint 1 at 0x81925a9: file /home/user/php-7.0/ext/gd/libgd/gd_interpolation.c, line 890.
(gdb) b gd_interpolation.c:982 if i == 12
Breakpoint 2 at 0x81929fc: file /home/user/php-7.0/ext/gd/libgd/gd_interpolation.c, line 982.
(gdb) r
Starting program: /home/user/php-7.0/sapi/cli/php -n phuzz4.php

Breakpoint 1, _gdContributionsAlloc (line_length=13, windows_size=9) at /home/user/php-7.0/ext/gd/libgd/gd_interpolation.c:890
890         res->ContribRow = (ContributionType *) gdMalloc(line_length * sizeof(ContributionType));

# windows_size is 9 

(gdb) c
Continuing.

Breakpoint 2, _gdScaleRow (pSrc=0x8c71c38, src_width=100, dst=0x8c7f5f0, dst_width=13, row=0, contrib=0x8c5c2d8)
    at /home/user/php-7.0/ext/gd/libgd/gd_interpolation.c:982
982                 r += (unsigned char)(contrib->ContribRow[x].Weights[left_channel] * (double)(gdTrueColorGetRed(p_src_row[i])));
(gdb) p left_channel
$1 = 9

contrib->ContribRow[x].Weights[left_channel] tries to access 10th element but the size is 9.

```

This affected PHP version 5.5, 5.6 and 7.0, patch released today:

http://php.net/ChangeLog-5.php#5.5.36

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
