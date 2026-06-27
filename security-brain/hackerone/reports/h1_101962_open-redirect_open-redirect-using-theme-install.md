---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '101962'
original_report_id: '101962'
title: Open redirect using theme install
weakness: Open Redirect
team_handle: shopify
created_at: '2015-11-25T07:39:40.187Z'
disclosed_at: '2015-12-14T21:38:41.325Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 52
tags:
- hackerone
- open-redirect
---

# Open redirect using theme install

## Metadata

- HackerOne Report ID: 101962
- Weakness: Open Redirect
- Program: shopify
- Disclosed At: 2015-12-14T21:38:41.325Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

An open redirect is an application that takes a parameter and redirects a user to the parameter value without any validation. This vulnerability is used in phishing attacks to get users to visit malicious sites without realizing it. 

Vulnerable Endpoint - https://app.shopify.com/services/google/themes/preview/supply--blue?domain_name=example.com
Impact - Medium
CVSS - 6.5 

Proof of concept :- 

[1] Go to https://app.shopify.com/services/google/themes/preview/supply--blue?domain_name=example.com
[2] You will be redirected to http://example.com/admin
[3] I can host a site where /admin is not 404 {not valid page } , This can lead and increase risk of phisiing attacks & so on .

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
