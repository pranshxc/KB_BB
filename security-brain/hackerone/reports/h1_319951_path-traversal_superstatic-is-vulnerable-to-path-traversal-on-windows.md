---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '319951'
original_report_id: '319951'
title: '`superstatic` is vulnerable to path traversal on Windows'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2018-02-26T17:53:06.527Z'
disclosed_at: '2018-04-29T16:10:30.241Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: superstatic
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# `superstatic` is vulnerable to path traversal on Windows

## Metadata

- HackerOne Report ID: 319951
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2018-04-29T16:10:30.241Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report path traversal vulnerability in `superstatic`
It allows to read arbitrary out-of-dir files when running on the Windows platform

# Module

**module name:** `superstatic`
**version:** 5.0.1
**npm page:** `https://www.npmjs.com/package/superstatic`

## Module Description

> Superstatic is an enhanced static web server that was built to power. It has fantastic support for HTML5 pushState applications, clean URLs, caching, and many other goodies.

## Module Stats

2 196 downloads in the last day
33 588 downloads in the last week
139 118 downloads in the last month

~1 669 416 estimated downloads per year

# Vulnerability

## Vulnerability Description

`superstatic` verifies that current dir is not evaded by checking the presense of `../` in the decoded path, but on Windows, `..\` works.
Code: https://github.com/firebase/superstatic/blob/v5.0.1/lib/providers/fs.js#L71

## Steps To Reproduce:

Install and run superstatic (`npx superstatic` in any dir). It could be also used as a Node.js lib.

Go to `http://localhost:3474/..%5c..%5c..%5c/Windows/notepad.exe` (adjust the path accordingly, that's for `C:\Users\User\tmp`).

*Note: don't use Edge for that, it decodes the path itself. Use e.g. Chromium.*

## Supporting Material/References:

- OS: Windows 10
- Node.js v8.9.4
- npm v5.6.0
- Chromium

# Wrap up

- I contacted the maintainer to let him know: N
- I opened an issue in the related repository: N

## Impact

Read any accessible files outside of the restricted directory.

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
