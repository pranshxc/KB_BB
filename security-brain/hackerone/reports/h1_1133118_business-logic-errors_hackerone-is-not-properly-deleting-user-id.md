---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1133118'
original_report_id: '1133118'
title: Hackerone is not properly deleting user id
weakness: Business Logic Errors
team_handle: security
created_at: '2021-03-23T16:28:58.180Z'
disclosed_at: '2021-06-11T18:55:27.451Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 344
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Hackerone is not properly deleting user id

## Metadata

- HackerOne Report ID: 1133118
- Weakness: Business Logic Errors
- Program: security
- Disclosed At: 2021-06-11T18:55:27.451Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Long  ago, i had an account on hackerone that is now deleted.
I used the alias email provided by h1 to sigbup on a site for bug testing.
To my surprise, i receive an email to my account routed from an alias email that should not exist.

**Description:**

### Steps To Reproduce

1. SignUp on H1
2.  Use h1 alias email to signup on some website
3.  Delete h1 account and the email still exists

### Optional: Your Environment (Browser version, Device, etc)

 * 

### Optional: Supporting Material/References (Screenshots)

 * as you can see.the email i just received. You can check your database that **█████** dont exist in your database coz I deleted the account long back..but you can see the email address
.
 
███████

## Impact

Privacy concern

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
