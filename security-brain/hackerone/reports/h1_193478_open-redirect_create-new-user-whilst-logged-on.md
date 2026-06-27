---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '193478'
original_report_id: '193478'
title: Create New User Whilst Logged On
weakness: Open Redirect
team_handle: starbucks
created_at: '2016-12-22T20:02:29.563Z'
disclosed_at: '2017-01-13T00:28:37.384Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
tags:
- hackerone
- open-redirect
---

# Create New User Whilst Logged On

## Metadata

- HackerOne Report ID: 193478
- Weakness: Open Redirect
- Program: starbucks
- Disclosed At: 2017-01-13T00:28:37.384Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

The website www.teavana.com allows users already logged on to create new account with a very simple url redirect. When an account is created a page is displayed with your account information and what you want to update. By simply refreshing the page allows you to create a new account whilst still logged on. If you try to recreate the same account with the same email but different password, there will be no error message displayed though when you try to login, the password will be incorrect.

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
