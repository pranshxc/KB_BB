---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '321701'
original_report_id: '321701'
title: '`utile` allocates uninitialized Buffers when number is passed in input'
weakness: Out-of-bounds Read
team_handle: nodejs-ecosystem
created_at: '2018-03-04T00:51:49.916Z'
disclosed_at: '2018-06-14T19:48:57.679Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- out-of-bounds-read
---

# `utile` allocates uninitialized Buffers when number is passed in input

## Metadata

- HackerOne Report ID: 321701
- Weakness: Out-of-bounds Read
- Program: nodejs-ecosystem
- Disclosed At: 2018-06-14T19:48:57.679Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report an uninitialized Buffer allocation issue in `utile`.
It allows to extract sensitive data from uninitialized memory or to cause a DoS by passing in a large number, in setups where typed user input can be passed (e.g. from JSON).

# Module

**module name:** `utile`
**version:** 0.3.0
**npm page:** `https://www.npmjs.com/package/utile`

## Module Description

> A drop-in replacement for util with some additional advantageous functions

## Module Stats

101 762 downloads in the last day
560 195 downloads in the last week
2 301 434 downloads in the last month

# Vulnerability

## Vulnerability Description

See https://github.com/flatiron/utile/blob/master/lib/base64.js#L19 in `utile.base64.encode` (and similar in `utile.base64.decode` below that).

The problem arises when a number is passed in, e.g. from user-submitted JSON-encoded data.
The API should not propagate the already-bad Buffer issue further.

On Node.js 6.x and below, this exposes uninitialized memory, which could contain sensitive data.

This can be also used to cause a DoS on any Node.js version by consuming the memory when large numbers are passed on input.

## Steps To Reproduce:

`console.log(require('utile').base64.encode(200))` (Node.js 6.x and lower — note uninitialized memory in output)

`require('utile').base64.encode(1e8)` (any Node.js verision — note memory usage and time)

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- OS: Arch Linux current
- Node.js 6.13.0
- Node.js 9.5.0

# Wrap up

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository: N

I contacted the maintainer over email on 2016-01-20, got an initial reply, replied back, but nothing happened since then.

## Impact

Sensitive uninitialized memory exposure on Node.js 6.x or lower
Denail of Service on any Node.js version

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
