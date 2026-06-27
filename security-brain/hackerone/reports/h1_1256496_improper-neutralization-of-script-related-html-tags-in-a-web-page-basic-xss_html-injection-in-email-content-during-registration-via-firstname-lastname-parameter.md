---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1256496'
original_report_id: '1256496'
title: HTML injection in email content during registration via FirstName/LastName
  parameter
weakness: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic
  XSS)
team_handle: mtn_group
created_at: '2021-07-09T22:41:59.788Z'
disclosed_at: '2021-12-18T09:42:30.575Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: mtnbusiness.com.ng
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-neutralization-of-script-related-html-tags-in-a-web-page-basic-xss
---

# HTML injection in email content during registration via FirstName/LastName parameter

## Metadata

- HackerOne Report ID: 1256496
- Weakness: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)
- Program: mtn_group
- Disclosed At: 2021-12-18T09:42:30.575Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi,
I just found an issue when register account in https://mtnmobad.mtnbusiness.com.ng/#/auth/registerUser
It allows an attacker to inject malicious text include html code in email content.

## Steps To Reproduce:


  1. Go to https://uat.id.manulife.ca/mortgagecreditor/register?ui_locales=en-CA.
  1. Use the following payload as your First Name:
  1. Put the following code as first name:
```
<h1>Ibrahim</h1>
```
  1. Fill other forms and submit


  {F1371367}

## Impact

html code injection

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
