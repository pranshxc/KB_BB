---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '902739'
original_report_id: '902739'
title: bunyan - RCE via insecure command formatting
weakness: Code Injection
team_handle: nodejs-ecosystem
created_at: '2020-06-19T10:29:37.243Z'
disclosed_at: '2020-06-27T01:53:03.703Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# bunyan - RCE via insecure command formatting

## Metadata

- HackerOne Report ID: 902739
- Weakness: Code Injection
- Program: nodejs-ecosystem
- Disclosed At: 2020-06-27T01:53:03.703Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report RCE in bunyan
It allows arbitrary commands remotely inside the victim's PC

# Module

**module name:** bunyan
**version:** 1.8.12
**npm page:** `https://www.npmjs.com/package/bunyan`

## Module Description

> Bunyan is a simple and fast JSON logging library for node.js services:

## Module Stats

[920,196] weekly downloads

# Vulnerability

## Vulnerability Description

> The issue occurs because a user input is formatted inside a command that will be executed without any check. https://github.com/trentm/node-bunyan/blob/master/bin/bunyan#L1224

## Steps To Reproduce:

> Run the following command
npm install bunyan
./node_modules/bunyan/bin/bunyan -p "S'11;touch hacked ;'"
> Recheck the files: now hacked has been created
## Patch

> Check input before command

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- [OPERATING SYSTEM VERSION]: Ubuntu 18.04
- [NODEJS VERSION]: v8.10.0
- [NPM VERSION]: 3.5.2

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [Y/N] N 
- I opened an issue in the related repository: [Y/N] N

## Impact

RCE on bunyan.

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
