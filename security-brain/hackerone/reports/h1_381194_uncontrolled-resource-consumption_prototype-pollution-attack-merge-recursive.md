---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '381194'
original_report_id: '381194'
title: Prototype pollution attack (merge.recursive)
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2018-07-13T10:26:55.413Z'
disclosed_at: '2018-09-28T10:13:25.154Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: merge
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Prototype pollution attack (merge.recursive)

## Metadata

- HackerOne Report ID: 381194
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2018-09-28T10:13:25.154Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report prototype pollution in merge.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** merge
**version:** 1.2.0
**npm page:** `https://www.npmjs.com/package/merge`

## Module Description

Merge multiple objects into one, optionally creating a new cloned object. Similar to the jQuery.extend but more flexible. Works in Node.js and the browser.

## Module Stats

1,822,662 downloads in the last week

# Vulnerability

## Vulnerability Description

This is a variant of this vulnerability:
https://hackerone.com/reports/310443

The `merge.recursive` function can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:

Craft an object of form `{__proto__: {...}}` and send it to `merge.recursive`.

```javascript
let merge = require('merge');
let payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
merge.recursive({}, payload);
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
