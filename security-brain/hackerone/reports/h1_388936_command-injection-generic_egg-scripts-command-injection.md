---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '388936'
original_report_id: '388936'
title: '[egg-scripts] Command injection'
weakness: Command Injection - Generic
team_handle: nodejs-ecosystem
created_at: '2018-07-31T13:54:26.547Z'
disclosed_at: '2018-08-19T07:27:08.095Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: egg-scripts
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# [egg-scripts] Command injection

## Metadata

- HackerOne Report ID: 388936
- Weakness: Command Injection - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2018-08-19T07:27:08.095Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a command injection vulnerability in egg-scripts.
It allows arbitrary shell command execution through a maliciously crafted command line argument.

# Module

**module name:** [egg-scripts]
**version:** [2.6.0]
**npm page:** `https://www.npmjs.com/package/egg-scripts`

## Module Description

"deploy tool for egg project."

## Module Stats

Replace stats below with numbers from npm’s module page:

209 downloads in the last day
1,958 downloads in the last week
8,333 downloads in the last month

# Vulnerability

## Vulnerability Description

egg-script does not sanitize the --stderr command line argument, and subsequently passes it to child_process.exec(), thus allowing arbitrary shell command injection.

## Steps To Reproduce:

1. Install egg: `npm i egg --save`
2. Install egg-scripts: `sudo npm i egg-scripts -g --save`
3. Run eggctl with malicious argument: `eggctl start --daemon --stderr=/tmp/eggctl_stderr.log; touch /tmp/malicious`
4. Check that the injected command was executed: `ls /tmp/`
5. Stop eggctl: `eggctl stop`

## Patch

Command execution happens [here](https://github.com/eggjs/egg-scripts/blob/22faa4cfbb84cc5bc819d981dce962d8f95f8357/lib/cmd/start.js#L214):
```
const [ stdout ] = yield exec('tail -n 100 ' + stderr);
```
`exec` could be replaced by `execFile`, which would force developers to separate the command and its arguments.

## Supporting Material/References:
- Operating system: Debian GNU/Linux 9.5 (stretch)
- Node.js v8.11.3
- npm v5.6.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Arbitrary shell command execution.

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
