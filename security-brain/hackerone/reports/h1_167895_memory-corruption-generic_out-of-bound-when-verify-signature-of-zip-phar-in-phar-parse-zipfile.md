---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '167895'
original_report_id: '167895'
title: Out of bound when verify signature of zip phar in phar_parse_zipfile
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-09-13T04:08:14.362Z'
disclosed_at: '2019-11-12T09:31:59.768Z'
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

# Out of bound when verify signature of zip phar in phar_parse_zipfile

## Metadata

- HackerOne Report ID: 167895
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-11-12T09:31:59.768Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=72928

There was a security code in phar_parse_zipfile
```
sig = (char *) emalloc(entry.uncompressed_filesize);
read = php_stream_read(fp, sig, entry.uncompressed_filesize);
if (read != entry.uncompressed_filesize) {
	php_stream_close(sigfile);
	efree(sig);
	PHAR_ZIP_FAIL("signature cannot be read");
}
mydata->sig_flags = PHAR_GET_32(sig);
if (FAILURE == phar_verify_signature(sigfile,
	php_stream_tell(sigfile),
	mydata->sig_flags,
	sig + 8,
	entry.uncompressed_filesize - 8,
	fname,
	&mydata->signature,
	&mydata->sig_len,
	error)
	) {
```
There are no checking *entry.uncompressed_filesize* attacker can create a signature.bin with size less than 8 and then this value is passed to *phar_verify_signature* as sig_len as you can see `entry.uncompressed_filesize - 8` as result sig_len is overflow.
And the third param is sig buffer as you can see `sig + 8`, because *entry.uncompressed_filesize* is less than 8 by default emalloc will return 16 bytes this result may lead to heap out of bound.

phar zip file : https://drive.google.com/file/d/0B0D1DYQpkA9Ud3I2OFlfeFRqbEU/view?usp=sharing

Test script:
---------------
```
<?php
	$phar = new PharData('phars/signature.zip');
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
