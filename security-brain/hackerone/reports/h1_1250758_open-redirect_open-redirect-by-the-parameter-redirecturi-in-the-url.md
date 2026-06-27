---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1250758'
original_report_id: '1250758'
title: Open redirect by the parameter redirectUri in the URL
weakness: Open Redirect
team_handle: blackrock
created_at: '2021-07-03T18:36:16.443Z'
disclosed_at: '2022-04-21T22:10:00.486Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: '*.blackrock.com'
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open redirect by the parameter redirectUri in the URL

## Metadata

- HackerOne Report ID: 1250758
- Weakness: Open Redirect
- Program: blackrock
- Disclosed At: 2022-04-21T22:10:00.486Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The following URL is vulnerable to an open redirect (it will redirect to google.com)
https://www.blackrock.com/authplatform/user/activate-success?redirectUri=https://google.com
After clicking on "return to site" it will be redirected to the page


Steps To Reproduce:


Enter on this link https://www.blackrock.com/authplatform/user/activate-success?redirectUri=https://google.com
Redirected to https://google.com

## Impact

Phishing attacks to redirect users to malicious sites without realizing it

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
