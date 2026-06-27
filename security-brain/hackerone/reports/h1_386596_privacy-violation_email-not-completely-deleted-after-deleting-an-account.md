---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '386596'
original_report_id: '386596'
title: Email Not Completely Deleted after Deleting an account
weakness: Privacy Violation
team_handle: semmle
created_at: '2018-07-25T07:20:56.013Z'
disclosed_at: '2019-03-25T13:45:19.354Z'
has_bounty: true
visibility: full
substate: informative
vote_count: 18
asset_identifier: lgtm-com.pentesting.semmle.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# Email Not Completely Deleted after Deleting an account

## Metadata

- HackerOne Report ID: 386596
- Weakness: Privacy Violation
- Program: semmle
- Disclosed At: 2019-03-25T13:45:19.354Z
- Has Bounty: Yes
- Visibility: full
- Substate: informative

## Original Report

**Description:** 
If one of the user deletes their account it should be fully deleted in account while semmle doesnt delete it completely.

## Steps To Reproduce:
* Register email1
* After registering, confirm your account.
* once email1 is confirmed. add another email which we will name as email2
* Now Verify the email of email2.
* Delete account of email1 completely
* Now register email2
* after registering email2, confirm the account of email2
* after confirming with the link given in email2 it will automatically logged in and you will notice that email1 and email2 is in there and no need confirmation for email1.

**Fix/Remediation**
As per the rules, once you delete your data in an account it should be completely deleted. it should be another life for an account.

## Impact

User know that after deleting account to semmle, their data will be lost to semmle's database however, it still there which is a privacy violation.

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
