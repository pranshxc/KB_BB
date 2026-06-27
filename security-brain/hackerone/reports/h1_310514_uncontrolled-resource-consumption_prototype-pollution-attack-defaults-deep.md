---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '310514'
original_report_id: '310514'
title: Prototype pollution attack (defaults-deep)
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2018-01-30T15:14:22.664Z'
disclosed_at: '2018-02-15T19:26:35.249Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: defaults-deep
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Prototype pollution attack (defaults-deep)

## Metadata

- HackerOne Report ID: 310514
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2018-02-15T19:26:35.249Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

As discussed in #309391, here's the separate report for each of the library. This one is the information for the defaults-deep library.

**Module:**

[https://www.npmjs.com/package/defaults-deep](defaults-deep)

**Summary:**

Utilities function in all the listed modules can be tricked into modifying the prototype of "Object" when the attacker control part of the structure passed to these function. This can let an attacker add or modify existing property that will exist on all object.

**Description:**

## Steps To Reproduce:

The simplest test case to reproduce the issue is the following code snippet. In the code snippet, "malicious_payload" would come from an endpoint which accepts JSON data. 

> var defaults-deep = require('defaults-deep');
> var malicious_payload = '{"\_\_proto\_\_":{"oops":"It works !"}}';
> 
> var a = {};
> console.log("Before : " + a.oops);
> defaults-deep({}, JSON.parse(malicious_payload));
> console.log("After : " + a.oops);

This shows that an attacker can add attributes to all existing object on the server. Additional attribute can be used to change the execution code flow or cause error on every subsequent request by replacing "toString" or "valueOf".

## Impact

This vulnerability is garanteed to at least obtain denial of service as all the library allow the property "toString" and "valueOf" to be replaced by a "String". This breaks the express module and forces the server to either crash or return a 500 to every subsequent request.

More complex payload can be crafted to gain remote code execution (see PoC in #309391).

## Supporting Material/References:

If extra information is needed don't hesitate to ask.

## Impact

Variable. Server crash or the server becoming unable to respond to all request is guaranteed, but more significant impact like remote code execution can be achieved in some cases.

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
