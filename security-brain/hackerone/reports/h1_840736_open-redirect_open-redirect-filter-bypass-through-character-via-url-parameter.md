---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '840736'
original_report_id: '840736'
title: Open Redirect filter bypass through '\' character via URL parameter
weakness: Open Redirect
team_handle: myndr
created_at: '2020-04-05T19:25:29.379Z'
disclosed_at: '2020-04-06T15:39:02.330Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 37
asset_identifier: '*.myndr.net'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open Redirect filter bypass through '\' character via URL parameter

## Metadata

- HackerOne Report ID: 840736
- Weakness: Open Redirect
- Program: myndr
- Disclosed At: 2020-04-06T15:39:02.330Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, I hope I find you all safe and good regarding those hard times nowadays.

## Summary:
Found an Open Redirect vulnerability on http://meta.myndr.net by bypassing the trusted domain filter using a '\' character.

I was able to get the original redirection URL from the register button located at http://dashboard.myndr.net/auth/login

Original Redirection URL
```http://meta.myndr.net/latest/meta-data/filter-id/add?ref_url=http://dashboard.myndr.net/auth/register?id= ```

Malicious URL 
```http://meta.myndr.net/latest/meta-data/filter-id/add/?ref_url=http://phishing.com\dashboard.myndr.net/../../../ ```

The vulnerable URL parameter is ```ref_url```

The trusted domain (or string) is ```dashboard.myndr.net```

It can be bypassed only from its beginning!  (between ```http://``` and the string) and not after ```.net```

## Steps To Reproduce:
Navigate to : ```http://meta.myndr.net/latest/meta-data/filter-id/add/?ref_url=http://phishing.com\dashboard.myndr.net/../../../```

You will be redirected to ```phising.com``` domain

## PoC: attached to the report

## Impact

1. Phishing campaigns can be initiated using such a vulnerability
2. It is an efficient way to bypass monitoring and email filters within an organization (the organization can check the "trust" level of each domains that they receive emails from)

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
