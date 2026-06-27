---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '542258'
original_report_id: '542258'
title: Cross Site Scripting at https://app.oberlo.com/
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2019-04-18T21:25:51.107Z'
disclosed_at: '2019-05-26T22:25:25.725Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
asset_identifier: oberlo.com
asset_type: URL
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Cross Site Scripting at https://app.oberlo.com/

## Metadata

- HackerOne Report ID: 542258
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2019-05-26T22:25:25.725Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1- create an account from **https://app.oberlo.com/**

2- path to https://app.oberlo.com/settings/account/profile

3- inject javascript code or xss payload at **Name** form

4- it will be printed at page and executed

payload that i used it **"><img src=x onerror=alert(document.domain)>**

## Impact

This vulnerability can be used by attacker to serve malicious JavaScript against any user.

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
