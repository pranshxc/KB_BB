---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '182420'
original_report_id: '182420'
title: Illegal write/read access caused by gdImageAALine overflow
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-11-16T02:24:22.263Z'
disclosed_at: '2019-10-31T06:16:01.317Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# Illegal write/read access caused by gdImageAALine overflow

## Metadata

- HackerOne Report ID: 182420
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-31T06:16:01.317Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Upstream Bug
---
https://bugs.php.net/bug.php?id=72482

Summary
---
Ilegal write/read access at gdImageSetAAPixelColor caused by gdImageAALine overflow.
gdImageAALine tries to clip the limit values and fails because an integer overflow occurs while calculating the new line limits.

PHP 5 is affected, but my debugging is done on PHP 7.

One of the integer overflows happens here:

1314   x2 -= ((im->sy - y2) * (x1 - x2)) / (y2 - y1);
gdb-peda$ p ((im->sy - y2) * (x1 - x2)) / (y2 - y1)   ## (a * b) / c  fails
$8 = 0x0
gdb-peda$ p (im->sy - y2) * ((x1 - x2) / (y2 - y1))   ## a * (b / c)   works
$9 = 0x40000c10

The illegal write access happens while trying to set this pixels to draw the line in gdImageSetAAPixelColor:

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=b25009fc2c97c6b5a93b3fc5f6a5b221b62f1273
https://gist.github.com/anonymous/873314feb4f89bd8336711333299f748
```

Fixed for PHP 5.6.28, PHP 7.0.13
--
http://php.net/ChangeLog-5.php#5.6.28
http://php.net/ChangeLog-7.php#7.0.13

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
