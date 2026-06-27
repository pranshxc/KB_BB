---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '804772'
original_report_id: '804772'
title: Prototype pollution in multipart parsing
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2020-02-25T17:51:30.156Z'
disclosed_at: '2020-02-28T10:55:15.010Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: fastify
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Prototype pollution in multipart parsing

## Metadata

- HackerOne Report ID: 804772
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2020-02-28T10:55:15.010Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a prototype pollution attack in fastify-multipart it allows to crash a remote server parsing multipart requests by sending a specially crafted request.

# Module

**module name:** fastify-multipart
**version:** all versions before < v1.0.5. v1.0.5 contains the fix. 
**npm page:** `https://www.npmjs.com/package/fastify-multipart`

## Module Description

[Fastify](https://www.fastify.io) plugin to parse the multipart content-type.

Under the hood it uses [busboy](http://npm.im/busboy).

## Module Stats

weekly downloads: 4900

# Vulnerability

## Vulnerability Description

Eran Hammer found this vulnerability for Hapi, he tested Fastify as well and found it vulnerable.
Here is the Hapi vulnerability report: https://www.npmjs.com/advisories/1479. 

## Steps To Reproduce:

> Detailed steps to reproduce with all required references/steps/commands. If there is any exploit code or reference to the package source code this is the place where it should be put.

## Patch

This was already released in https://github.com/fastify/fastify-multipart/pull/116 and version 1.0.5 issued.

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: Y
- I opened an issue in the related repository: N

I just need a CVE issued.

## Impact

It's a Denial of Service attack

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
