---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1195325'
original_report_id: '1195325'
title: Default Admin Username and Password on █████ Server at █████████mil
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2021-05-13T05:39:02.777Z'
disclosed_at: '2021-06-15T19:28:16.108Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 23
tags:
- hackerone
- improper-access-control-generic
---

# Default Admin Username and Password on █████ Server at █████████mil

## Metadata

- HackerOne Report ID: 1195325
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2021-06-15T19:28:16.108Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
A ██████ Server is running at https://███mil you can access the login at https://████mil/█████████ the application is using the default "Administrator for the default organization" credentials 

#POC 
Go to  https://███mil/████████ and login with *█████*

██████████

████

████

## How to remediate the vulnerability

Change the password of the user or disable the account 

## References
█████
https://cwe.mitre.org/data/definitions/521.html


##EXTRA

If you have any questions or concerns regarding the above let me know!

Cheers,

## Impact

A Department of Defense website was misconfigured in a manner that may have allowed a malicious user to login with administrator for the default organization account credentials.

## System Host(s)
████mil

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Read the POC

## Suggested Mitigation/Remediation Actions
Change the password of the user or disable the account

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
