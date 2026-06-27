---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '825729'
original_report_id: '825729'
title: '[logkitty] RCE via insecure command formatting'
weakness: Code Injection
team_handle: nodejs-ecosystem
created_at: '2020-03-21T00:53:36.972Z'
disclosed_at: '2020-05-09T08:42:11.023Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: logkitty
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# [logkitty] RCE via insecure command formatting

## Metadata

- HackerOne Report ID: 825729
- Weakness: Code Injection
- Program: nodejs-ecosystem
- Disclosed At: 2020-05-09T08:42:11.023Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a `RCE` issue in the `logkitty` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `logkitty`
**version:** `0.7.0`
**npm page:** `https://www.npmjs.com/package/logkitty`

## Module Description
> Display pretty Android and iOS logs without Android Studio or Console.app, with intuitive Command Line Interface.

## Module Stats
[170,222] downloads in the last week

## Vulnerability Description
The issue occurs because a `user input` is formatted inside a `command` that will be executed without any check. The issue arises here: https://github.com/zamotany/logkitty/blob/master/src/android/adb.ts#L55

## Steps To Reproduce:
1. Check there aren't files called `HACKED` 
1. Execute the following commands in another terminal:

```bash
npm i logkitty # Install affected module
logkitty android app 'test; touch HACKED' #  Note the *touch command* is inside the *'* (single quote), so it's an argument, while it will be executed anyway
```
1. Recheck the files: now `HACKED` has been created :) {F754955}

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

`RCE` via command formatting on `logkitty`

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
