---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1033107'
original_report_id: '1033107'
title: DNS Max Responses for DOS
weakness: Uncontrolled Resource Consumption
team_handle: nodejs
created_at: '2020-11-12T18:32:25.883Z'
disclosed_at: '2020-12-16T22:08:53.517Z'
has_bounty: true
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

# DNS Max Responses for DOS

## Metadata

- HackerOne Report ID: 1033107
- Weakness: Uncontrolled Resource Consumption
- Program: nodejs
- Disclosed At: 2020-12-16T22:08:53.517Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

See Github (my issue): https://github.com/nodejs/node/issues/36063


When i try to fetch the A Dns records of following domain: ticbrasil.com.br I dont get any response.
I think thats the case because there are over 1300 responses.

Version: v12.18.4, v14.15.0
Platform: 64-bit Windows 10 Pro & Enterprise

What steps will reproduce the bug?
var dns = require('dns'); dns.resolve4('ticbrasil.com.br', function (err, addresses, family) { console.log(err); console.log(addresses); console.log(family); });

How often does it reproduce? Is there a required condition?
It happends everytime

What is the expected behavior?
https://pastebin.com/Tv53Na89

What do you see instead?
Nothing/No output

## Impact

mmomtchev commented 3 hours ago
@mhdawson someone should contact Mitre or whoever you usually contact, this is a confirmed remote security vulnerability. If an attacker can trigger a DNS resolution for an address chosen by him, then it is exploitable for DoS. It is a very high-risk vulnerability. I don't think a remote access is possible, but this should probably be evaluated by an expert.

@jasnell
 
Member
jasnell commented 2 hours ago
We can look into this further but I have to point out: we have a defined process for properly reporting and investigating potential security vulnerabilities. As soon as this issue was suspected as being a security issue, that process should have been followed with investigation and fixes investigated in the private Node.js repo we use for that purpose, otherwise this ends up risking a zero-day for all Node.js users.

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
