---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '321702'
original_report_id: '321702'
title: '`put` allocates uninitialized Buffers when non-round numbers are passed in
  input'
weakness: Out-of-bounds Read
team_handle: nodejs-ecosystem
created_at: '2018-03-04T01:05:37.886Z'
disclosed_at: '2018-06-14T19:48:12.220Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- out-of-bounds-read
---

# `put` allocates uninitialized Buffers when non-round numbers are passed in input

## Metadata

- HackerOne Report ID: 321702
- Weakness: Out-of-bounds Read
- Program: nodejs-ecosystem
- Disclosed At: 2018-06-14T19:48:12.220Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report an uninitialized Buffer allocation issue in `put`.
It allows to extract sensitive data from uninitialized memory by passing in non-round numbers, in setups where typed user input can be passed (e.g. from JSON).

# Module

**module name:** `put`
**version:** 0.0.6
**npm page:** `https://www.npmjs.com/package/put`

## Module Description

> Pack multibyte binary values into buffers with specific endiannesses.

## Module Stats

402 downloads in the last day
3 889 downloads in the last week
17 107 downloads in the last month

# Vulnerability

## Vulnerability Description

`put` incorrectly calculates the total length of the allocated Buffer and does not trim it to the total bytes written, see https://github.com/substack/node-put/blob/master/index.js#L51

The problem arises when non-round numbers are passed in to the `pad` function.
The API should not propagate the already-bad Buffer issue further.

On Node.js 6.x and below, this exposes uninitialized memory, which could contain sensitive data.

## Steps To Reproduce:

```js
var Put = require('put');
var buf = Put().pad(0.99).pad(0.99).pad(0.99).pad(0.99).pad(0.99).buffer();
console.log(buf);
```

```js
var Put = require('put');
var buf = Put();
for (var i = 0; i < 10000; i++) buf.pad(0.99);
console.log(buf.buffer().toString('ascii'));
```

Run on Node.js 6.x or below.

## Supporting Material/References:

- OS: Arch Linux current
- Node.js 6.13.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Sensitive uninitialized memory exposure on Node.js 6.x or lower

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
