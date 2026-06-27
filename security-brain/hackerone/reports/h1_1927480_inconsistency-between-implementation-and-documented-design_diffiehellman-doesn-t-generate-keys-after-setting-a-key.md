---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1927480'
original_report_id: '1927480'
title: DiffieHellman doesn't generate keys after setting a key
weakness: Inconsistency Between Implementation and Documented Design
team_handle: nodejs
created_at: '2023-03-31T13:33:05.838Z'
disclosed_at: '2023-07-20T20:59:27.162Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- inconsistency-between-implementation-and-documented-design
---

# DiffieHellman doesn't generate keys after setting a key

## Metadata

- HackerOne Report ID: 1927480
- Weakness: Inconsistency Between Implementation and Documented Design
- Program: nodejs
- Disclosed At: 2023-07-20T20:59:27.162Z
- Has Bounty: No
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

DiffieHellman may be used as the basis for application level security, implications are consequently broad. E.g., key reuse can cause major problems, cryptanalysis may break confidentiality, integrity, ...

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
