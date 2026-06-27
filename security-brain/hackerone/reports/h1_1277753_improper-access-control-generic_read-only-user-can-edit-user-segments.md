---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1277753'
original_report_id: '1277753'
title: Read-only user can edit user segments.
weakness: Improper Access Control - Generic
team_handle: mailru
created_at: '2021-07-26T10:00:32.408Z'
disclosed_at: '2021-12-30T18:28:24.183Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: Ext. A Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Read-only user can edit user segments.

## Metadata

- HackerOne Report ID: 1277753
- Weakness: Improper Access Control - Generic
- Program: mailru
- Disclosed At: 2021-12-30T18:28:24.183Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Domain
--
https://tracker.my.com/segment/list

Testing environment
--
Open two separate browsers with two independent accounts created at https://tracker.my.com/

Steps to reproduce
--
**In browser A**
1. Log in to your account at https://tracker.my.com/ as user 1.
2. Create a new account at https://tracker.my.com/account/add for user 1.
3. Now in the created account, create a new random project.
4. Now create an unpublished or standalone app. Add any data.
5. Now create a segment.
6. Go to https://tracker.my.com/account/user/list/?idAccount=NUMERIC_ID
7. Add user 2 as a ``read-only`` user.

**In browser B**
1. Log in to your account at https://tracker.my.com/ as user 2.
2. Go to https://tracker.my.com/account/list/.
3. Select the account where your a ``read-only`` user.
4. Now go to https://tracker.my.com/segment/list.
5. Edit the added segment title.
6. Done.

Actual results
--
``Read-only`` user can edit the title of a created segment by the account owner.

Expected results
--
``Read-only`` user should not have this ability as the role describes.

## Impact

The ``read-only`` user can edit limited parts of segments authored by the account owner which is not supposed to happen as described at the Tracker documentation [here](https://tracker.my.com/docs/environment/account).

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
