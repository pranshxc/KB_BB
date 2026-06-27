---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '321686'
original_report_id: '321686'
title: '`atob` allocates uninitialized Buffers when number is passed in input on Node.js
  4.x and below'
weakness: Out-of-bounds Read
team_handle: nodejs-ecosystem
created_at: '2018-03-03T23:22:23.359Z'
disclosed_at: '2018-04-08T21:05:09.925Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: atob
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- out-of-bounds-read
---

# `atob` allocates uninitialized Buffers when number is passed in input on Node.js 4.x and below

## Metadata

- HackerOne Report ID: 321686
- Weakness: Out-of-bounds Read
- Program: nodejs-ecosystem
- Disclosed At: 2018-04-08T21:05:09.925Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report an uninitialized Buffer allocation issue in `atob`.
It allows to extract sensitive data from uninitialized memory or to cause a DoS by passing in a large number, in setups where typed user input can be passed (e.g. from JSON), on Node.js 4.x and lower.

# Module

**module name:** `atob`
**version:** 2.0.3
**npm page:** `https://www.npmjs.com/package/atob`

## Module Description

> Uses Buffer to emulate the exact functionality of the browser's atob.

## Module Stats

492 191 downloads in the last day
2 890 027 downloads in the last week
11 036 537 downloads in the last month

# Vulnerability

## Vulnerability Description

The problem arises when a number is passed in, e.g. from user-submitted JSON-encoded data.
The API should not propagate the already-bad Buffer issue further.

On Node.js 4.x and below (4.x is still supported), this exposes uninitialized memory, which could contain sensitive data. This can be also used to cause a DoS by consuming the memory when large numbers are passed on input.

## Steps To Reproduce:

`console.log(require('atob')(1000))` (note uninitialized memory in output)
`console.log(require('atob')(1e8))` (note memory usage and time)

Run on Node.js 4.x (or below).

## Supporting Material/References:

- Arch Linux Current
- Node.js 4.8.7

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Sensitive uninitialized memory exposure
Denail of Service
This issue affects only setups using Node.js 4.x (still supported) or lower.

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
