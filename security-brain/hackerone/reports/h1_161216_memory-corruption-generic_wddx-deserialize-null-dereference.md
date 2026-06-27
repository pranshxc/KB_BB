---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161216'
original_report_id: '161216'
title: wddx_deserialize null dereference
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-08-19T03:57:00.501Z'
disclosed_at: '2019-10-31T06:17:34.375Z'
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

# wddx_deserialize null dereference

## Metadata

- HackerOne Report ID: 161216
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-31T06:17:34.375Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Upstream Bug
---
https://bugs.php.net/bug.php?id=72750

Summary
--
When wddx deserialize tries to parse an invalid base64 binary value, php_base64_decode return NULL. The return value is not checked and used.
```
https://github.com/php/php-src/blob/master/ext/wddx/wddx.c#L896

                if (!strcmp((char *)name, EL_BINARY)) {
                        zend_string *new_str = php_base64_decode(
                                (unsigned char *)Z_STRVAL(ent1->data), Z_STRLEN(ent1->data));
                        zval_ptr_dtor(&ent1->data);
                        ZVAL_STR(&ent1->data, new_str);
                }
```

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=698a691724c0a949295991e5df091ce16f899e02
```

Fixed for PHP 5.6.25, PHP 7.0.10
--
http://php.net/ChangeLog-5.php
http://php.net/ChangeLog-7.php

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
