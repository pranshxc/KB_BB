---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '340208'
original_report_id: '340208'
title: Command injection in 'pdf-image'
weakness: Command Injection - Generic
team_handle: nodejs-ecosystem
created_at: '2018-04-18T18:24:40.746Z'
disclosed_at: '2018-05-29T20:43:43.830Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: pdf-image
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# Command injection in 'pdf-image'

## Metadata

- HackerOne Report ID: 340208
- Weakness: Command Injection - Generic
- Program: nodejs-ecosystem
- Disclosed At: 2018-05-29T20:43:43.830Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report command injection in pdf-image
It allows executing commands on the server 

# Module

**module name:** pdf-image
**version:** 1.0.5
**npm page:** `https://www.npmjs.com/package/pdf-image`

## Module Description

> Provides an interface to convert PDF's pages to png files in Node.js by using ImageMagick.


## Module Stats

[2013] downloads in the last week

# Vulnerability

## Vulnerability Description

> Description about how the vulnerability was found and how it can be exploited, how it harms package users (data modification/lost, system access, other.

## Steps To Reproduce:

> The constructGetInfoCommand would be initializing the command that is to the passed to 'exec' of getInfo(). The user input is not getting validated in #L26 of constructGetInfoCommand and it leads to command injection in #L43.

https://github.com/mooz/node-pdf-image/blob/master/index.js#L26
https://github.com/mooz/node-pdf-image/blob/master/index.js#L43## Patch

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Kali linux 
- Nodejs v8.10.0
- Npm v5.8.0

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

An attacker could execute arbitrary shell commands

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
