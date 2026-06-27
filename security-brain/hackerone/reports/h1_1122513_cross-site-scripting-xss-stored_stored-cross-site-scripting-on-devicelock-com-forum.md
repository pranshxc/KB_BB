---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1122513'
original_report_id: '1122513'
title: Stored Cross-site Scripting on devicelock.com/forum/
weakness: Cross-site Scripting (XSS) - Stored
team_handle: acronis
created_at: '2021-03-10T18:04:32.499Z'
disclosed_at: '2022-02-08T10:49:21.823Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 64
asset_identifier: '*.devicelock.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored Cross-site Scripting on devicelock.com/forum/

## Metadata

- HackerOne Report ID: 1122513
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: acronis
- Disclosed At: 2022-02-08T10:49:21.823Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary

Hello, @acronis Team I hope you all doing well.

I just found A Stored Cross-site Scripting on devicelock.com/forum/ by changing the ***City*** value on https://www.devicelock.com/bitrix/admin/user_edit.php? to HTML/javascript code and lead to Stored Cross-site Scripting.


  1. go to https://www.devicelock.com/forum/view_profile.php?register=yes  and create a new account 
  1. go to https://www.devicelock.com/bitrix/admin/user_edit.php? and click on **Personal information** and in `City` input put and xss payload like: `<img src=x onerror=alert(document.cookie)>` and click on apply.
  1. Go to https://www.devicelock.com/forum/view_profile.php?UID=<your_user_id> and change `<your_user_id>` to your id 

## POC
https://www.devicelock.com/forum/view_profile.php?UID=28349

{F1225664}

## Impact

Stored XSS.

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
