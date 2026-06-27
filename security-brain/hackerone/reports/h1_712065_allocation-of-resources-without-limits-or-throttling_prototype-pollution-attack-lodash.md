---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '712065'
original_report_id: '712065'
title: Prototype pollution attack (lodash)
weakness: Allocation of Resources Without Limits or Throttling
team_handle: nodejs-ecosystem
created_at: '2019-10-11T12:06:20.745Z'
disclosed_at: '2020-04-27T22:14:18.244Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: lodash
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- allocation-of-resources-without-limits-or-throttling
---

# Prototype pollution attack (lodash)

## Metadata

- HackerOne Report ID: 712065
- Weakness: Allocation of Resources Without Limits or Throttling
- Program: nodejs-ecosystem
- Disclosed At: 2020-04-27T22:14:18.244Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a prototype pollution vulnerability in lodash.
It allows an attacker to inject properties on Object.prototype

Module
module name: lodash
version: 4.17.15
npm page: https://www.npmjs.com/package/lodash

Module Description
The Lodash library exported as Node.js modules.

Module Stats
25,228,177 downloads in the last week

Vulnerability
Vulnerability Description
This is a similar with this vulnerability: https://hackerone.com/reports/380873

The functions merge, mergeWith, and defaultsDeep can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.

Steps To Reproduce:
Craft an object by "zipObjectDeep" function of lodash

const _ = require('lodash');
_.zipObjectDeep(['__proto__.z'],[123])
console.log(z) // 123

## Impact

Variable. Server crash or the server becoming unable to respond to all request is garanteed, but more significant impact like remote code execution can be achieved in some cases.

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
