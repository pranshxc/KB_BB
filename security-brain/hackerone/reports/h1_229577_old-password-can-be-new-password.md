---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '229577'
original_report_id: '229577'
title: Old password can be new password
team_handle: weblate
created_at: '2017-05-18T09:58:45.364Z'
disclosed_at: '2017-06-03T05:07:16.115Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
---

# Old password can be new password

## Metadata

- HackerOne Report ID: 229577
- Weakness: 
- Program: weblate
- Disclosed At: 2017-06-03T05:07:16.115Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

### Affected Domain:
https://demo.weblate.org/ 

### Issue: 
The sites like Facebook and Google keeps tracks of old password and does not allow user to set password similar to their old passwords.
However in case of demo.weblate.org. It is possible for a user to set new password which is exactly similar to old passwords. 

### Impact:
Thought the impact of the issue is not high, it is always best practice to now allow so. 

### Solution:
The password history of the user should be tracked and user should not be allowed to set password which are similar to his old passwords.

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
