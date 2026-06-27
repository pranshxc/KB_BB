---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '147203'
original_report_id: '147203'
title: Insecure password change mechanism may lead to full account takeover
weakness: Cryptographic Issues - Generic
team_handle: fantasytote
created_at: '2016-06-25T14:55:51.458Z'
disclosed_at: '2016-07-23T17:34:41.085Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- cryptographic-issues-generic
---

# Insecure password change mechanism may lead to full account takeover

## Metadata

- HackerOne Report ID: 147203
- Weakness: Cryptographic Issues - Generic
- Program: fantasytote
- Disclosed At: 2016-07-23T17:34:41.085Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

###Description:
The password change mechanism which is located at https://www.fantasytote.com/users/edit is insecure as there is no old password field deployed in it. Any unauthorized user can access the account and can change the password directly without knowing the old password. The current password or old password field is necessary because it prevents any unauthorized user from changing the password.

Facebook, Google and many other companies have deployed this fix.

###Steps to Reproduce:

* Goto https://www.fantasytote.com
* Sign in 
* Goto https://www.fantasytote.com/users/edit
* You will see password change area
* Change the password and it will be changed without prompting the old password

###Fix / Patch:
Deploy a mechanism that asks the user for the old password in order to change his password. If the user knows his old password, the password should be changed otherwise not.

Waiting for positive response,
Thanks.

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
