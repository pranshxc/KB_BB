---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '321687'
original_report_id: '321687'
title: '`base64url` allocates uninitialized Buffers when number is passed in input
  on Node.js 4.x and below'
weakness: Out-of-bounds Read
team_handle: nodejs-ecosystem
created_at: '2018-03-03T23:35:58.959Z'
disclosed_at: '2018-05-11T20:18:15.861Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: base64url
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- out-of-bounds-read
---

# `base64url` allocates uninitialized Buffers when number is passed in input on Node.js 4.x and below

## Metadata

- HackerOne Report ID: 321687
- Weakness: Out-of-bounds Read
- Program: nodejs-ecosystem
- Disclosed At: 2018-05-11T20:18:15.861Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report an uninitialized Buffer allocation issue in `base64url`.
It allows to extract sensitive data from uninitialized memory or to cause a DoS by passing in a large number, in setups where typed user input can be passed (e.g. from JSON), on Node.js 4.x and lower.

# Module

**module name:** `base64url`
**version:** 2.0.0
**npm page:** `https://www.npmjs.com/package/base64url`

## Module Description

> Converting to, and from, base64url

## Module Stats

182 924 downloads in the last day
1 097 142 downloads in the last week
4 601 176 downloads in the last month

# Vulnerability

## Vulnerability Description

The problem arises when a number is passed in, e.g. from user-submitted JSON-encoded data.
The API should not propagate the already-bad Buffer issue further.

On Node.js 4.x and below (4.x is still supported), this exposes uninitialized memory, which could contain sensitive data. This can be also used to cause a DoS by consuming the memory when large numbers are passed on input.

## Steps To Reproduce:

`console.log(require('base64url').encode(1000))`  (note uninitialized memory in output)
`require('base64url').encode(1e8)` (note memory usage and time)

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Arch Linux Current
- Node.js 4.8.7

# Wrap up

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository:  N

I tried to contact the maintainer over email, first time on 2017-03-02, last time on 2018-02-18, but did not receive a reply.

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
