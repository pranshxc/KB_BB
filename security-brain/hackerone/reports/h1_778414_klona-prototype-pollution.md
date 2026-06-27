---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '778414'
original_report_id: '778414'
title: '[klona] Prototype pollution'
team_handle: nodejs-ecosystem
created_at: '2020-01-20T17:03:43.298Z'
disclosed_at: '2020-01-23T11:17:26.602Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# [klona] Prototype pollution

## Metadata

- HackerOne Report ID: 778414
- Weakness: 
- Program: nodejs-ecosystem
- Disclosed At: 2020-01-23T11:17:26.602Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report Prototype pollution in klona
It allows adding arbitrary property to Prototype while deep cloning an object

# Module

**module name:** klona
**version:** <1.1.1
**npm page:** `https://www.npmjs.com/package/klona`

## Module Description

A tiny (366B) and fast utility to "deep clone" Objects, Arrays, Dates, RegExps, and more!

## Module Stats

356 weekly downloads

# Vulnerability

## Vulnerability Description

See: https://snyk.io/vuln/SNYK-JS-LODASH-450202

## Steps To Reproduce:

Described here: https://github.com/lukeed/klona/pull/11/files

Note:
This vulnerability was reported directly to owner here https://github.com/lukeed/klona/pull/11 on 10/01/2020.
Fix published in v1.1.1 on 15/01/2020

# Wrap up

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository: Y

> Hunter's comments and funny memes goes here

{F690469}

## Impact

Denial of Service and possible Remote code execution by overriding object's property methods like `toString`

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
