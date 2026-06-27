---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '167896'
original_report_id: '167896'
title: Out of bound when verify signature of tar phar in phar_parse_tarfile
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-09-13T04:09:12.354Z'
disclosed_at: '2019-11-12T09:31:40.823Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- memory-corruption-generic
---

# Out of bound when verify signature of tar phar in phar_parse_tarfile

## Metadata

- HackerOne Report ID: 167896
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-11-12T09:31:40.823Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=73035
There was a security code in phar_parse_tarfile
```
if (FAILURE == phar_verify_signature(fp, php_stream_tell(fp) - size - 512, myphar->sig_flags, buf + 8, size - 8, fname, &myphar->signature, &myphar->sig_len, error)) {
	if (error) {
		char *save = *error;
		spprintf(error, 4096, "phar error: tar-based phar \"%s\" signature cannot be verified: %s", fname, save);
		efree(save);
		}
	goto bail;
}
```
There are no checking *entry.uncompressed_filesize* attacker can create a signature.bin with size less than 8 and then this value is passed to *phar_verify_signature* as sig_len as you can see `entry.uncompressed_filesize - 8` as result sig_len is overflow.
And the third param is sig buffer as you can see `sig + 8`, because *entry.uncompressed_filesize* is less than 8 by default emalloc will return 16 bytes this result may lead to heap out of bound.

tarfile : https://drive.google.com/open?id=0B0D1DYQpkA9UVkV1Q0tTeGpVYk0

Test script:
---------------
```
<?php
	$phar = new PharData('phars/signature.tar');
	var_dump($phar);
?>
```

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
