---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '317548'
original_report_id: '317548'
title: Regular Expression Denial of Service (ReDoS)
weakness: Uncontrolled Resource Consumption
team_handle: nodejs-ecosystem
created_at: '2018-02-19T11:29:12.393Z'
disclosed_at: '2019-04-03T20:00:47.887Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Regular Expression Denial of Service (ReDoS)

## Metadata

- HackerOne Report ID: 317548
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs-ecosystem
- Disclosed At: 2019-04-03T20:00:47.887Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The issue was already fixed.

**Module:** is-my-json-valid

**Summary:** 
Affected versions of this package are vulnerable to Regular Expression Denial of Service (ReDoS) attacks. It used a regular expression (/^\S+@\S+$/) in order to validate emails. This can cause an impact of about 10 seconds matching time for data 90K characters long.

**Description:** 
Regex:
 formats.js
 exports[‘email’] = /^\S+@\S+$/
(introduced in 2014, 34a1a706)


## Supporting Material/References:

* https://github.com/mafintosh/is-my-json-valid/pull/159
* https://github.com/mafintosh/is-my-json-valid/commit/b3051b277f7caa08cd2edc6f74f50aeda65d2976

## Impact

Denial of service through blocking the event loop.

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
