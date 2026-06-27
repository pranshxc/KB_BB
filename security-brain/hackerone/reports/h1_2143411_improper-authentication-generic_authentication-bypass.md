---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2143411'
original_report_id: '2143411'
title: authentication bypass
weakness: Improper Authentication - Generic
team_handle: deptofdefense
created_at: '2023-09-11T07:20:41.545Z'
disclosed_at: '2023-09-29T17:27:40.385Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- improper-authentication-generic
---

# authentication bypass

## Metadata

- HackerOne Report ID: 2143411
- Weakness: Improper Authentication - Generic
- Program: deptofdefense
- Disclosed At: 2023-09-29T17:27:40.385Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
hello team!

the endpoint https://www.████████/852585B6003EBA25/Login.html?open
There is a page to log in!
however, it is possible to ignore this page using just a single quote '

let's go!

1: go to https://www.███████/852585B6003EBA25/Login.html?open
2: in the login field put a single quote '
3: boom! Now you have access to the portal completely ignoring the login and password field!!

little video:
███

## Impact

Improper Authentication

## System Host(s)
www.█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
let's go!

1: go to https://www.████████/852585B6003EBA25/Login.html?open
2: in the login field put a single quote '
3: boom! Now you have access to the portal completely ignoring the login and password field!!

## Suggested Mitigation/Remediation Actions

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
