---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '152232'
original_report_id: '152232'
title: NULL Pointer Dereference in exif_process_user_comment
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-07-19T07:55:52.244Z'
disclosed_at: '2016-08-30T18:58:10.546Z'
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

# NULL Pointer Dereference in exif_process_user_comment

## Metadata

- HackerOne Report ID: 152232
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2016-08-30T18:58:10.546Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is a bug occur in exif_process_user_comment when trying to encode JIS string.
```
else if (!memcmp(szValuePtr, "JIS\0\0\0\0\0", 8)) {
			/* JIS should be tanslated to MB or we leave it to the user - leave it to the user */
			*pszEncoding = estrdup((const char*)szValuePtr);
			szValuePtr = szValuePtr+8;
			ByteCount -= 8;
			/* XXX this will fail again if encoding_converter returns on error something different than SIZE_MAX   */
			if (zend_multibyte_encoding_converter(
					(unsigned char**)pszInfoPtr,
					&len,
					(unsigned char*)szValuePtr,
					ByteCount,
					zend_multibyte_fetch_encoding(ImageInfo->encode_jis),
					zend_multibyte_fetch_encoding(ImageInfo->motorola_intel ? ImageInfo->decode_jis_be : ImageInfo->decode_jis_le)
					) == (size_t)-1) {
				len = exif_process_string_raw(pszInfoPtr, szValuePtr, ByteCount);
			}
			return len;
```
As you can see at function call zend_multibyte_fetch_encoding(ImageInfo->encode_jis). At PHP_INI_BEGIN encode_jis was set at empty string so that the result of this call above return NULL and then pass to zend_multibyte_encoding_converter. If this php version is compiled with *mbstring*, this NULL pointer is passed to mbfl_buffer_converter_new2 through *to* pointer.
```
mbfl_buffer_converter_new2(
	const mbfl_encoding *from,
	const mbfl_encoding *to,
    int buf_initsz)
{
    ******SNIP********
	/* initialize */
	convd->from = from;
	convd->to = to;
	/* create convert filter */
	convd->filter1 = NULL;
	convd->filter2 = NULL;
	if (mbfl_convert_filter_get_vtbl(convd->from->no_encoding, convd->to->no_encoding) != NULL) {
    ******SNIP********
```

Because of none checking 2 pointers *from* and *to* so NULL pointer is passed directly to convd->to and result is the crash when calling mbfl_convert_filter_get_vtbl.

Here crash jpeg file : https://drive.google.com/file/d/0B0D1DYQpkA9URnRROVdLdG5jdFE/view?usp=sharing

This bug also works on Mac OS X and Windows.

Test script:
---------------
```
<?php
	$exif = exif_read_data('null.jpg');
	var_dump($exif);
?>
```
The bug here : https://bugs.php.net/bug.php?id=72618

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
