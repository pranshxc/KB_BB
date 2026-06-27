---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '390631'
original_report_id: '390631'
title: '[ascii-art] Command injection'
weakness: Command Injection - Generic
team_handle: nodejs-ecosystem
created_at: '2018-08-05T06:31:48.648Z'
disclosed_at: '2018-09-08T08:36:27.752Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: ascii-art
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# [ascii-art] Command injection

## Metadata

- HackerOne Report ID: 390631
- Weakness: Command Injection - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2018-09-08T08:36:27.752Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a command injection vulnerability in the **ascii-art npm** module.
It allows arbitrary shell command execution through a maliciously crafted command line argument.

# Module

**module name:** ascii-art
**version:** 1.4.3
**npm page:** `https://www.npmjs.com/package/ascii-art`

## Module Description

>Images, fonts, tables, ansi styles and compositing in Node.js & the browser. 100% JS.
>
>In the beginning there was colors.js but in the fine tradition of vendors calling out a problem they have the solution to, chalk was introduced. In that same vein, I offer ascii-art as an update, expansion and generalization of MooAsciiArt and at the same time it can replace your existing ansi colors library.
>
>It features support for Images, Styles, Tables and Figlet Fonts as well as handling multi-line joining automatically.

## Module Stats

56 downloads in the last day
217 downloads in the last week
1432 downloads in the last month

# Vulnerability

## Vulnerability Description

ascii-art does not sanitize the `target` command line argument, and subsequently passes it to `child_process.exec()`, thus allowing arbitrary shell command injection.

## Steps To Reproduce:

1. Install ascii-art: `sudo npm install -g ascii-art` (On a pristine Google Cloud instance, I also had to install pkg-config, libcairo2-dev, libjpeg-dev and libgif-dev, and then install ascii-art with unsafe-perm=true).
2. Run ascii-art with malicious argument: `ascii-art preview 'doom"; touch /tmp/malicious; echo "'`
3. Check that the injected command was executed: `ls /tmp/`

## Patch

Command execution happens [here](https://github.com/khrome/ascii-art/blob/9059daa5fcbf2c6a8813bbf072a1477d91e7b61d/bin/ascii-art#L210):

`exec('open "http://www.figlet.org/fontdb_example.cgi?font='+target.toLowerCase()+'.flf"')`

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
