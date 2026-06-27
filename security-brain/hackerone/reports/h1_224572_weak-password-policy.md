---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '224572'
original_report_id: '224572'
title: Weak password policy
team_handle: weblate
created_at: '2017-04-28T06:59:25.061Z'
disclosed_at: '2017-08-18T05:21:02.751Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
---

# Weak password policy

## Metadata

- HackerOne Report ID: 224572
- Weakness: 
- Program: weblate
- Disclosed At: 2017-08-18T05:21:02.751Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
i get to know that you are using strong password policy.
i gone through application and checked for that.

and get to know that as per ISO9001 security compliance weak password policy.

#Steps :
1) signup with  https://hosted.weblate.org/ with password vikas@123
2) forget password and change to some other password
3) change again to vikas@123
it will allow.

as per strong password security last 5 used password should not allowed from application,

#Scenario:
if by mistake attacker get to know victim's password and then only victim will change password.
again victim changed and he changed to same password that will not always good policy.

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
