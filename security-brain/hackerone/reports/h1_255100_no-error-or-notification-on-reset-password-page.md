---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '255100'
original_report_id: '255100'
title: No error or notification on Reset password page
team_handle: legalrobot
created_at: '2017-07-31T07:57:00.672Z'
disclosed_at: '2017-09-26T01:07:11.378Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: app.legalrobot.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# No error or notification on Reset password page

## Metadata

- HackerOne Report ID: 255100
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-09-26T01:07:11.378Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello
I found that there is no error occurring at Reset password page. There should error occur when user enter the wrong email-id or the entered password is used in 180 previous days or token got expired because from previous reset link also the page got opened so, user would not be able to understand the reason why he/she could not able to reset the password. Although it is not a security bug but my request to you to add error message or notification for these things on Reset Password page for user convenience.
Thanks

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
