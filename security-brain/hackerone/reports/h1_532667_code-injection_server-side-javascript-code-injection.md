---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '532667'
original_report_id: '532667'
title: Server Side JavaScript Code Injection
weakness: Code Injection
team_handle: nodejs-ecosystem
created_at: '2019-04-09T15:23:13.508Z'
disclosed_at: '2019-10-03T18:17:41.756Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: fastify
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# Server Side JavaScript Code Injection

## Metadata

- HackerOne Report ID: 532667
- Weakness: Code Injection
- Program: nodejs-ecosystem
- Disclosed At: 2019-10-03T18:17:41.756Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I would like to report a Service Side JavaScript Code Injection in `fastify`.
It allows an attacker that can control a single property name in the serialization schema to achieve Remote Command Execution in the context of the web server.

# Module

**module name:** fastify
**version:** 2.2.0
**npm page:** `https://www.npmjs.com/package/fastify`

## Module Description

> An efficient server implies a lower cost of the infrastructure, a better responsiveness under load and happy users. How can you efficiently handle the resources of your server, knowing that you are serving the highest number of requests as possible, without sacrificing security validations and handy development? Enter Fastify. Fastify is a web framework highly focused on providing the best developer experience with the least overhead and a powerful plugin architecture. It is inspired by Hapi and Express and as far as we know, it is one of the fastest web frameworks in town.

## Module Stats

39,119 downloads in the last week

# Vulnerability

## Vulnerability Description

> Description about how the vulnerability was found and how it can be exploited, how it harms package users (data modification/lost, system access, other.

## Steps To Reproduce:

> Detailed steps to reproduce with all required references/steps/commands. If there is any exploit code or reference to the package source code this is the place where it should be put.

## Patch

Escape `"`, `'` and ``` ` ``` in properties names in schema definition.

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- **OS:** Kali Rolling
- **NodeJS:** 11.9
- **NPM:** 6.5.0
- **fast-json-stringify:** 1.14.0

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: Y (sent message to Matteo Collina)
- I opened an issue in the related repository: N

## Impact

If an attacker can control somehow the schema definition, he/she can achieve arbitrary code execution as the user running the web server.

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
