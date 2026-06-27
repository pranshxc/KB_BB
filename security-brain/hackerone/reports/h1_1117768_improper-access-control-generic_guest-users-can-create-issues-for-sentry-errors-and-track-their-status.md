---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1117768'
original_report_id: '1117768'
title: Guest Users can create issues for Sentry errors and track their status
weakness: Improper Access Control - Generic
team_handle: gitlab
created_at: '2021-03-05T04:24:45.029Z'
disclosed_at: '2021-09-24T12:07:13.150Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Guest Users can create issues for Sentry errors and track their status

## Metadata

- HackerOne Report ID: 1117768
- Weakness: Improper Access Control - Generic
- Program: gitlab
- Disclosed At: 2021-09-24T12:07:13.150Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary
 
According to the [permission docs](https://docs.gitlab.com/ee/user/permissions.html) and [Error Tracking Docs](https://docs.gitlab.com/ee/operations/error_tracking.html#error-tracking-list) , only User with role `Reporter` or more can see or modify the Error Tracking details. However, the "Create Issue" allows a particular `Guest` user to create a reference issue for the error and track its status whenever some other user resolves it.

### Steps to reproduce

(Step-by-step guide to reproduce the issue, including:)

1. Consider a private project with `Guest` role user.
2.  Connect `Sentry` to this project from the `Maintainer` account.
3. And create new issues in Sentry. This automatically populates these errors in https://gitlab.com/project_name/-/error_tracking/.
4. Now, consider the request for creating an issue.

     POST Data format for this is as follows: 
     ```
     issue[title]=Title
     issue[description]= Description
     issue[sentry_issue_attributes][sentry_issue_identifier]=Error_Id
     authenticity_token= your_auth_token
     ```
5. Change `Error_Id` parameter to some  Error's reference id value (this is basically Sentry's Error id).
6. Now, execute the request from `Guest`'s session. This creates an issue for that particular error.
7. Now, go to the `Maintainer`'s login and resolve the error. This will close the issue that created by the `Guest User` with the message `@Maintainer resolved the corresponding error and closed the issue`.

## Impact

Using this vulnerability, Guest Users can create issues for  Sentry errors and track their Status.

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
