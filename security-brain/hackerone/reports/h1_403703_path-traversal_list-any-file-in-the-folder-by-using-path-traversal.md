---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '403703'
original_report_id: '403703'
title: List any file in the folder by using path traversal
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2018-09-01T03:35:12.717Z'
disclosed_at: '2018-11-23T08:03:07.307Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: simplehttpserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# List any file in the folder by using path traversal

## Metadata

- HackerOne Report ID: 403703
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2018-11-23T08:03:07.307Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report Path Traversal in simplehttpserver. It allows to list any file in another folder of web root.

# Module

**module name:** simplehttpserver
**version:** v0.2.1
**npm page:** `https://www.npmjs.com/package/simplehttpserver`

## Module Description

 'simpehttpserver' is an simple imitation of python's SimpleHTTPServer and is intended for testing, development and debugging purposes

## Module Stats

 [319] downloads in the last week

# Vulnerability

## Vulnerability Description

 simpehttpserver is simply get the path name of url and add it to the web root.If there is a symlink file in the directory. You can access files outside the web root directory.

## Steps To Reproduce:
 create symlink file 
$ ln -s ../../ symdir

 install simplehttpserver
$ npm install simplehttpserver -g

start program
$ simplehttpserver ./

{F340863}

## Patch

Disable symlink file access in webserver.

## Supporting Material/References:

Configuration I've used to find this vulnerability:

macos 10.13.6
nodejs v10.9.0
npm 6.4.1
chrome 68.0.3440.106

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

This vulnerability allows malicious user to list file in the folder. This might expose vectors to attack system with Remote Code Execution, reveals files with usernames and passwords and many other possibilites.

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
