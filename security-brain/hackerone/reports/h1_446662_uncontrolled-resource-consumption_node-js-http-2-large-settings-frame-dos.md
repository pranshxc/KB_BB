---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '446662'
original_report_id: '446662'
title: Node.js HTTP/2 Large Settings Frame DoS
weakness: Uncontrolled Resource Consumption
team_handle: nodejs
created_at: '2018-11-18T12:19:36.854Z'
disclosed_at: '2020-07-02T19:55:27.225Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Node.js HTTP/2 Large Settings Frame DoS

## Metadata

- HackerOne Report ID: 446662
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs
- Disclosed At: 2020-07-02T19:55:27.225Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
 
I would like to report a vulnerability in the http2 module of Node.js. 
 
In section 10.5 of the HTTP/2 RFC an attack is described where an attacker is sending large SETTINGS frames that includes many settings inside it. 
We tested this scenario by opening many connections to the server and sending a SETTINGS frame with payload size of 14400 bytes and we were able to overload one CPU core with 100% usage with a single machine. 
Another important thing to mention is that node doesn’t close the connection to the server after some time so the attacker is able to continue sending those large SETTINGS frames.

This was tested against Node version 8.11.3
You can the code that was used to start the http2 server and also the script that we used for attacking it attached.

## Impact

Denial of Service

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
