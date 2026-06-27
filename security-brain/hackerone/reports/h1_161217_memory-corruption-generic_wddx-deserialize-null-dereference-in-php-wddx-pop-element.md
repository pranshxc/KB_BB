---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161217'
original_report_id: '161217'
title: wddx_deserialize null dereference in php_wddx_pop_element
weakness: Memory Corruption - Generic
team_handle: ibb
created_at: '2016-08-19T04:03:10.173Z'
disclosed_at: '2019-10-13T18:25:48.192Z'
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

# wddx_deserialize null dereference in php_wddx_pop_element

## Metadata

- HackerOne Report ID: 161217
- Weakness: Memory Corruption - Generic
- Program: ibb
- Disclosed At: 2019-10-13T18:25:48.192Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Upstream Bug
---
https://bugs.php.net/bug.php?id=72799

Summary
--
If we add an element to boolean leaf of XML struct, a null pointer dereference will happen when the element is popped. 

```
Source code:
https://github.com/php/php-src/blob/PHP-5.6.24/ext/wddx/wddx.c#L985

static void php_wddx_pop_element(void *user_data, const XML_Char *name)
{
...
  if (Z_TYPE_P(ent2->data) == IS_ARRAY || Z_TYPE_P(ent2->data) == IS_OBJECT) {
    target_hash = HASH_OF(ent2->data);
...

```

Patch
--
```
http://git.php.net/?p=php-src.git;a=commit;h=1f6078e4a5c67733bfdbd20bb2706501ac56a344
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
