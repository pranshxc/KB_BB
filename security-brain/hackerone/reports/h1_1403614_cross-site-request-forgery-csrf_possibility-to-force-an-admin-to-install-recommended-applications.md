---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1403614'
original_report_id: '1403614'
title: Possibility to force an admin to install recommended applications
weakness: Cross-Site Request Forgery (CSRF)
team_handle: nextcloud
created_at: '2021-11-18T00:00:52.498Z'
disclosed_at: '2022-04-29T11:50:18.775Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Possibility to force an admin to install recommended applications

## Metadata

- HackerOne Report ID: 1403614
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: nextcloud
- Disclosed At: 2022-04-29T11:50:18.775Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Endpoint /nextcloud/index.php/core/apps/recommended is accessible via GET http method and doesn't check anti-csrf token. If an admin visits this endpoint in a browser the process of installation of recommended applications begins immediately.

## Steps To Reproduce:
1. an attacker creates a malicious page on controlled domain
1. an attacker enforce an admin to visit this page
1. an admin visits this page
1. applications will be installed in a while

## Affected version:
nextcloud/server: 22.2.2 (at least)

## Recommendation:
require requesttoken for this GET query
or you can change behaviour so to initiate the installation process by manual click (POST query with checking of requesttoken)

## [attachment / reference]
{F1517676}

## Impact

Increasing of attack surface.
Any unused plugins should be disabled or removed. But this way allows to install them.

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
