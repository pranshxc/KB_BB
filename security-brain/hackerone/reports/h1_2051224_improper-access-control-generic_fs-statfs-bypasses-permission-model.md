---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2051224'
original_report_id: '2051224'
title: fs.statfs bypasses Permission Model
weakness: Improper Access Control - Generic
team_handle: nodejs
created_at: '2023-07-05T15:16:06.056Z'
disclosed_at: '2023-09-10T15:26:01.801Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# fs.statfs bypasses Permission Model

## Metadata

- HackerOne Report ID: 2051224
- Weakness: Improper Access Control - Generic
- Program: nodejs
- Disclosed At: 2023-09-10T15:26:01.801Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

`fs.statfs` is not limited by the permission model check

**Description:**

`fs.statfs` doesn't throw ERR_ACCESS_DENIED when accessing an restricted path, being able to get stat information of the file

## Steps To Reproduce:

```console
touch ./test.js
```

```js
// index.js
const fs = require('fs')

fs.statfs('./test.js', (err, stats) => {
  console.log('stats', stats)
})
```

```
$ node --experimental-permission --allow-fs-read=/path/to/index.js
(node:756097) ExperimentalWarning: Permission is an experimental feature
(Use `node --trace-warnings ...` to show where the warning was created)
stats StatFs {
  type: 61267,
  bsize: 4096,
  blocks: 56377128,
  bfree: 27380986,
  bavail: 24498982,
  files: 14393344,
  ffree: 12478020
}
```

## Impact

Even though it can't read the file contents, it's still can perform I/O against that file to retrieve file stats and to check if a file exists.

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
