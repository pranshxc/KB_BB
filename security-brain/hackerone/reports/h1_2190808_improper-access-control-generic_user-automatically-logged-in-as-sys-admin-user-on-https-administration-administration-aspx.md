---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2190808'
original_report_id: '2190808'
title: User automatically logged in as Sys Admin user on https://███/Administration/Administration.aspx
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2023-10-03T11:57:38.098Z'
disclosed_at: '2023-11-03T17:15:45.291Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 79
tags:
- hackerone
- improper-access-control-generic
---

# User automatically logged in as Sys Admin user on https://███/Administration/Administration.aspx

## Metadata

- HackerOne Report ID: 2190808
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2023-11-03T17:15:45.291Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Any user can access the Administration section of the following URL: https://███
When the user goes to the following domain they are automatically logged in as "████████" which is a sys admin user on the application, this allows any user to upload files, add users, change permissions for users and delete users.

## References

## Impact

A malicious actor can modify other user's privileges on the application, add users, upload files, delete users. They can also add false information to the application which will jeopardize the integrity of the application. With administrator privileges they have no restrictions on the application.

## System Host(s)
https://█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Step 1) Go to the following URL: https://███ 
There you will se that you are logged in as a Sys Admin user

## Suggested Mitigation/Remediation Actions
The application should prompt a user to authenticate first before being able to do any other actions on the system.

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
