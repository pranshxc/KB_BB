---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '403692'
original_report_id: '403692'
title: '[tianma-static] Stored xss on filename'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nodejs-ecosystem
created_at: '2018-09-01T02:29:04.350Z'
disclosed_at: '2018-11-02T10:45:04.803Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: tianma-static
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [tianma-static] Stored xss on filename

## Metadata

- HackerOne Report ID: 403692
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nodejs-ecosystem
- Disclosed At: 2018-11-02T10:45:04.803Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report stored xss in tianma-static
It allows anyone to execute arbitary javascript for doing anything.

# Module

**module name:** tianma-static
**version:** 1.0.4
**npm page:** `https://www.npmjs.com/package/tianma-static`

## Module Description

Provide a static file service.

# Vulnerability

## Vulnerability Description

it was possible to embed malicious js code in filename there was no sanitization performed. 

## Steps To Reproduce:

1. create filename `<img src=x onerror=alert(1)>`
2. start tianma-static
3. xss fired

F340845


# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows anyone to execute arbitary javascript for doing anything.

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
