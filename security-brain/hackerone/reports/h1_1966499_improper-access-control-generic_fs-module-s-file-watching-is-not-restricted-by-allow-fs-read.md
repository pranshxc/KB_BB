---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1966499'
original_report_id: '1966499'
title: fs module's file watching is not restricted by --allow-fs-read
weakness: Improper Access Control - Generic
team_handle: nodejs
created_at: '2023-04-29T22:43:56.045Z'
disclosed_at: '2023-07-20T20:56:52.134Z'
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

# fs module's file watching is not restricted by --allow-fs-read

## Metadata

- HackerOne Report ID: 1966499
- Weakness: Improper Access Control - Generic
- Program: nodejs
- Disclosed At: 2023-07-20T20:56:52.134Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** [add summary of the vulnerability]
The `--allow-fs-read` flag of the permission system does not prevent file watching.

**Description:** [add more details about this vulnerability]
Attackers can watch files that they don't have read access to.

## Steps To Reproduce:
Run the following code with `--experimental-permission` and do not grant read access to `file.txt`. Modify `file.txt` in another process. Information is leaked to the attacker about a file they should not have access to.

```js
'use strict';
const fs = require('node:fs');

async function main() {
	fs.watchFile(__dirname + '/file.txt', () => {
		console.log('able to watch a file without any permissions');
	});
}

main();
```

## Impact: [add why this issue matters]

The permission system is bypassed. Attackers can receive events related to files they do not have access to.

## Supporting Material/References:

None

## Impact

The permission system is bypassed.

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
