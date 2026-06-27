---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '324423'
original_report_id: '324423'
title: Reflected XSS (myynti.lahitapiolarahoitus.fi)
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: localtapiola
created_at: '2018-03-11T13:37:30.037Z'
disclosed_at: '2018-06-19T06:03:31.330Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: myynti.lahitapiolarahoitus.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS (myynti.lahitapiolarahoitus.fi)

## Metadata

- HackerOne Report ID: 324423
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: localtapiola
- Disclosed At: 2018-06-19T06:03:31.330Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
There is an Reflected XSS on myynti.lahitapiolarahoitus.fi.

**Description:** 
There is an Reflected XSS on myynti.lahitapiolarahoitus.fi website. redirect parameter is vulnerable to XSS.

**Impact:**
Steals cookies from other logged in users.

## Browsers / Apps Verified In:

Tested on Chrome Version 57.0.2987.98 Built on 8.7, running on Debian 8.10 (64-bit)
Tested on Firefox 52.5.2 (64-bit)

## Steps To Reproduce:

Click following link;
https://myynti.lahitapiolarahoitus.fi/#/?redirect=javascript%3Aalert(document.cookie)

## Additional material

{F271480}

## Impact

Steals cookies from other logged in users.

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
