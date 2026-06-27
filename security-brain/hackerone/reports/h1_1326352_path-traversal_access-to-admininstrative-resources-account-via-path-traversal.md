---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1326352'
original_report_id: '1326352'
title: Access to admininstrative resources/account via path traversal
weakness: Path Traversal
team_handle: deptofdefense
created_at: '2021-08-31T21:38:19.783Z'
disclosed_at: '2022-09-06T18:59:23.016Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- path-traversal
---

# Access to admininstrative resources/account via path traversal

## Metadata

- HackerOne Report ID: 1326352
- Weakness: Path Traversal
- Program: deptofdefense
- Disclosed At: 2022-09-06T18:59:23.016Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
A user can login as an administrator without the need of an ██████████ account, or an authenticated user can access and manipulate administrative resources without needing to login as an administrator. An ████████ (███████) account is required.
## References

## Impact

Exfiltration of sensitive data (IPs, system configurations, passwords, usernames, email addresses, names), website defacing, denial of service, potential rce, deletion of data.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
If you do not have an ██████(██████████) account:

Navigate to https://██████/
Login using your ████████ account. 
When you login you should be at the page https://██████/Saba/██████/CustomLogin.jsp with the error "There was an error while processing your request.  Please try again. If the problem persists, please contact the help desk at ████████".
Navigate to https://█████████/home
Your account name should say "Samba administrator"

If you do have an █████████(███████) account:

Navigate to https://█████/
Login using your ███████ account. 
Navigate to a page in the admin directory i.e. https://███████/Saba/Web_wdk/████████/platform/system/admin/systemMain.rdf  or https://██████████/Saba/Web_wdk/███████/Platform/system/admin/usersStatistics.rdf

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
