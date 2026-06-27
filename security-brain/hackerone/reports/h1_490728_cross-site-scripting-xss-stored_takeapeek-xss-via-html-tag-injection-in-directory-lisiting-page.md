---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '490728'
original_report_id: '490728'
title: '[takeapeek] XSS via HTML tag injection in directory lisiting page'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: nodejs-ecosystem
created_at: '2019-02-03T17:29:57.570Z'
disclosed_at: '2019-07-01T08:52:17.316Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
asset_identifier: takeapeek
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [takeapeek] XSS via HTML tag injection in directory lisiting page

## Metadata

- HackerOne Report ID: 490728
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: nodejs-ecosystem
- Disclosed At: 2019-07-01T08:52:17.316Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I was taking a peek at `takeapeek` module and found it is vulnerable to XSS via malicious injection in directory listing.
It allows execution of arbitrary JS code.

# Module

**module name:** takeapeek
**version:** 0.2.2
**npm page:** `https://www.npmjs.com/package/takeapeek`

## Module Description

A simple static webserver with only one command. Heavily inspired by glance, this is really more of a learning experience then anything.

## Module Stats

**weekly downloads**
4

# Vulnerability

## Vulnerability Description

`takeapeek` module provides a directory listing feature in it's HTTP server but it doesn't sanitize the filename hence a malicious payload in the filename cane be used to invoke an XSS. For example a file can be strategically named as `javascript:alert(1)` and we can see the XSS executing in the browser on clicking that link.

## Steps To Reproduce:

- Install `takeapeek`
```
$ npm install -g takeapeek
```

- Create a file with name `javascript:alert(1)`
```
 $ touch 'javascript:alert(1)'
```

- Start server in current directory
```
$ takeapeek
takepeek listening at http://localhost:3141
```

- Visit the address in any browser and click on malicous file link that we created.
{F417367}

## Supporting Material/References:

- Ubuntu 16.04
- node v11.3.0
- npm 6.7.0
- Chrome 72

# Wrap up


- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

An attacker is able to execute malicious JavaScript in context of other user's browser.

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
