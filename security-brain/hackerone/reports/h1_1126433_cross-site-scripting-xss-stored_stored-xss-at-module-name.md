---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1126433'
original_report_id: '1126433'
title: Stored XSS at Module Name
weakness: Cross-site Scripting (XSS) - Stored
team_handle: stripo
created_at: '2021-03-15T19:45:30.462Z'
disclosed_at: '2021-04-12T14:06:47.774Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 23
asset_identifier: my.stripo.email
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS at Module Name

## Metadata

- HackerOne Report ID: 1126433
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: stripo
- Disclosed At: 2021-04-12T14:06:47.774Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello, I found stored xss at module name with this payload ```"><div onmouseover="alert('XSS');">Hello :)```

## Steps To Reproduce:
1. Add new container, it doesn't matter which is it
2. Paste this payload  in the module name```"><div onmouseover="alert('XSS');">Hello :)```
3. Update it then check the module name again in setting
4. Alert Popup

## Stored XSS
Stored cross-site scripting (also known as second-order or persistent XSS) arises when an application receives data from an untrusted source and includes that data within its later HTTP responses in an unsafe way.

## Impact

Execute Js in victims browser

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
