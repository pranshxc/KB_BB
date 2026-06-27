---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2038484'
original_report_id: '2038484'
title: DiffieHellman doesn't generate keys after setting a key
weakness: Cryptographic Issues - Generic
team_handle: ibb
created_at: '2023-06-26T10:18:46.123Z'
disclosed_at: '2023-06-30T14:05:28.179Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cryptographic-issues-generic
---

# DiffieHellman doesn't generate keys after setting a key

## Metadata

- HackerOne Report ID: 2038484
- Weakness: Cryptographic Issues - Generic
- Program: ibb
- Disclosed At: 2023-06-30T14:05:28.179Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

DiffieHellman doesn't generate keys after setting a key

## Steps To Reproduce:

  1. Instantiate: `const dh = crypto.createDiffieHellman(1024);`
  2. Set private key: 
```
//set private key to 2
dh.setPrivateKey(Buffer.from("02", 'hex'));        
//outputs 02 (as expected)
console.log(dh.getPrivateKey().toString('hex'));  
```
  3. Generate random private key:
```
//generate random private key
dh.generateKeys();                                 
//outputs 02: zero day.
console.log(dh.getPrivateKey().toString('hex'));   
```

## Underlying issue:

OpenSSL (https://github.com/majek/openssl/blob/master/crypto/dh/dh_key.c) doesn't generate keys when they're already instantiated: 

```
if (dh->priv_key == NULL)
  {
  priv_key=BN_new();
  if (priv_key == NULL) goto err;
  generate_new_key=1;
  }
else
  priv_key=dh->priv_key;

if (dh->pub_key == NULL)
  {
  pub_key=BN_new();
  if (pub_key == NULL) goto err;
  }
else
  pub_key=dh->pub_key;
```

node:crypto should use OpenSSL correctly. Method `generateKeys()` should re-instantiate OpenSSL before requesting a key, thereby avoiding the above.

## Impact

A nonce must be used just once; using a nonce more than once is a security vulnerability. As concrete examples: Forward secrecy of TLS and IND-CPA of ElGamal would be trivially lost if Node.js's DH were used as a building block. 

This vulnerability is devastating to any developers that have used nodejs in accordance with documentation. Developers have chosen to fix documentation rather than code, unfortunately, nodejs is potentially introducing gaping security holes to anyone using code as original directed.

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
