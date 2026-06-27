---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '504761'
original_report_id: '504761'
title: phar_tar_writeheaders_int() buffer overflow
weakness: Classic Buffer Overflow
team_handle: ibb
created_at: '2019-03-04T12:21:44.897Z'
disclosed_at: '2020-11-09T01:46:01.959Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- classic-buffer-overflow
---

# phar_tar_writeheaders_int() buffer overflow

## Metadata

- HackerOne Report ID: 504761
- Weakness: Classic Buffer Overflow
- Program: ibb
- Disclosed At: 2020-11-09T01:46:01.959Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

A buffer overflow has been found in the phar_tar_writeheaders_int() function.

it does a strncpy to header->linkname from entry->link with the size of entry->link.

As you can see in https://github.com/php/php-src/blob/master/ext/phar/tar.h#L66 , header->linkname is a char of the size 100. Once entry->link contains a value that's bigger than 100 it will overflow the _tar_header structure.

This can be fixed by setting the size argument of strncpy to sizeof(header->linkname) for example:

strncpy(header.linkname, entry->link, strlen(header->linkname);

This has been fixed in the following references:

https://github.com/php/php-src/commit/071e18c6971c4cf64297378b30b945a1b85d682a
http://git.php.net/?p=php-src.git;a=commit;h=e0f5d62bd6690169998474b62f92a8c5ddf0e699
https://bugs.php.net/bug.php?id=77586&edit=2

Kind Regards,

Jordy Zomer

## Impact

An attacker could overflow the buffer resulting in either a crash (DoS), EOP or RCE.

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
