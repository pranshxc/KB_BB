---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '909757'
original_report_id: '909757'
title: '[is-my-json-valid] ReDoS via ''style'' format'
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2020-06-27T15:07:22.309Z'
disclosed_at: '2020-07-31T17:13:38.920Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: is-my-json-valid
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# [is-my-json-valid] ReDoS via 'style' format

## Metadata

- HackerOne Report ID: 909757
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2020-07-31T17:13:38.920Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a ReDoS in `is-my-json-valid`
It allows cause a denial of service if schema uses the built-in `style` format.

# Module

**module name:** `is-my-json-valid`
**version:** 2.20.1
**npm page:** `https://www.npmjs.com/package/is-my-json-valid`

## Module Description

> A JSONSchema validator that uses code generation to be extremely fast.

## Module Stats

1 250 253 weekly downloads

# Vulnerability

## Vulnerability Description

Classic ReDoS, polynomial time.

Note that https://www.npmjs.com/package/safe-regex is not free from false positives/negatives (as noted in its Readme) and does not catch this and other polynomial regexps (e.g. `/a*a*b/`).

## Steps To Reproduce:

```js
const imjv = require('is-my-json-valid')
const validate = imjv({ maxLength: 100, format: 'style' })
console.log(validate(' '.repeat(1e4)))
```

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

DoS if schema uses the `style` format.

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
