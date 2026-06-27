---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '398285'
original_report_id: '398285'
title: '[serve] XSS via HTML tag injection in directory lisiting page'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nodejs-ecosystem
created_at: '2018-08-22T19:24:44.393Z'
disclosed_at: '2018-10-19T07:53:01.485Z'
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

# [serve] XSS via HTML tag injection in directory lisiting page

## Metadata

- HackerOne Report ID: 398285
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nodejs-ecosystem
- Disclosed At: 2018-10-19T07:53:01.485Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report HTML injection in serve module.
It allows malicious HTML tags injection and execution of arbitrary JS code

# Module

**module name:** serve
**version:** 9.6.0
**npm page:** `https://www.npmjs.com/package/serve`

## Module Description
Assuming you would like to serve a static site, single page application or just a static file (no matter if on your device or on the local network), this package is just the right choice for you.

It behaves exactly like static deployments on Now, so it's perfect for developing your static project. Then, when it's time to push it into production, you deploy it.

Furthermore, it provides a neat interface for listing the directory's contents:

## Module Stats

95,383 weekly downloads

# Vulnerability

## Vulnerability Description

`serve` module provides a neat directory listing feature in it's HTTP server but it does'nt sanitize the filename hence a malicious payload in the filename cane be used to invoke an XSS. For example a file can be strategically named as `<img src=x onerror=alert('XSS')>` and we can see the XSS executing in the browser.

Alternatively a file can be created containing `iframe` tag with `src` attribute pointing to a malicious html which executes javascript on loading as pointed out in https://hackerone.com/reports/355458

## Steps To Reproduce:

* Install `serve`

`yarn global add serve`

or

`npm i serve -g`

* Create a file and name it

 `<img src=x onerror='alert("XSS")'>`

or

`"><iframe src="malware_frame.html">`

* Start `serve` in the folder containing the payload file

`serve`

* Open up `localhost:5000` in browser

## Patch

In `serve-handler` the file `directory.js` takes in a list of all files in directory and adds it in `<a>` tag without sanitizing.

```
var out = '<!DOCTYPE ............. 
.
.
.
out += ' <a href="/<a' + (value.url) + '">' + (value.name) + '</a> '
```

Fixing this here might mitigate the issue IMO

## Supporting Material/References:

- Ubuntu 16.04
- Node v10.9.0
- npm v6.2.0
- Firefox 61.0.1

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

An attacker is able to execute malicious JavaScript in context of other user's browser.

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
