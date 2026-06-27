---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1112297'
original_report_id: '1112297'
title: Reporters can upload design to issues using the "Move to" feature
weakness: Privilege Escalation
team_handle: gitlab
created_at: '2021-02-26T15:57:15.935Z'
disclosed_at: '2021-10-18T05:57:16.621Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Reporters can upload design to issues using the "Move to" feature

## Metadata

- HackerOne Report ID: 1112297
- Weakness: Privilege Escalation
- Program: gitlab
- Disclosed At: 2021-10-18T05:57:16.621Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary

 According to the [permission documentation](https://docs.gitlab.com/ee/user/permissions.html), only role of `Developer` or more can upload  [Design Management](https://docs.gitlab.com/ee/user/project/issues/design_management.html) files. However, using the issue "Move to" feature, a reporter can create a issue with designs.

### Steps to reproduce

1. Consider a private project (say **Private Project**) with a member `Reporter`.
2. From Reporter's login, create a new project. (say **Reporter Project**).
3. Create an issue in *Reporter Project*.
4. Once the issue is created, upload a design to it.
5. Now, on the right hand panel bottom, click the *Move* button. 
6. Choose the *Private Project* as the destination project.
7. Now the issue along with the design are migrated to  the *Private Project*.

Let me know if you need anything else to reproduce this issue.

## Impact

Using the vulnerability, a Reporter can escalate his privilege to upload Design Management Files which he is not allowed to perform.

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
