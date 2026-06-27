---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1187820'
original_report_id: '1187820'
title: Reflected XSS on /admin/stats.php
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: revive_adserver
created_at: '2021-05-07T14:35:04.156Z'
disclosed_at: '2021-06-03T12:38:57.290Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: https://github.com/revive-adserver/revive-adserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on /admin/stats.php

## Metadata

- HackerOne Report ID: 1187820
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: revive_adserver
- Disclosed At: 2021-06-03T12:38:57.290Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, Security Team!

Linked to the reports:
- https://hackerone.com/reports/1083376
- https://hackerone.com/reports/1097217

In the past reports, we have corrected Reflected XSS. But recently it turned out that with the parameter `breakdown = affiliates`, this vulnerability still works. (Fixed when parameter `breakdown = history`).

- Go to `http://revive-adserver.loc/admin/stats.php?entity=global&breakdown=affiliates&statsBreakdown=day%27%20onclick=alert(document.domain)%20accesskey=X%20`
- For the payload to be executed, the user needs to press the access key combination for the hidden input field (for Firefox, Alt+Shift+X, see [this](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/accesskey) for other browsers).

{F1292520}

{F1292519}

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
