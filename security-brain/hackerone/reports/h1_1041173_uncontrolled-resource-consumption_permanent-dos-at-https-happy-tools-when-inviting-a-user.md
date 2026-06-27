---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1041173'
original_report_id: '1041173'
title: Permanent DoS at https://happy.tools/ when inviting a user
weakness: Uncontrolled Resource Consumption
team_handle: automattic
created_at: '2020-11-23T12:18:41.122Z'
disclosed_at: '2021-01-29T08:27:05.402Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Permanent DoS at https://happy.tools/ when inviting a user

## Metadata

- HackerOne Report ID: 1041173
- Weakness: Uncontrolled Resource Consumption
- Program: automattic
- Disclosed At: 2021-01-29T08:27:05.402Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

At [Happy Tools](https://happy.tools/), I found an exception to the exclusion of denial of service. The web app allows creating an account/login into an account either using Gmail or WordPress. The vulnerability lies in the fact that after registration, a user can change their email without verification.

## Steps To Reproduce:
1. Using separate browsers or browser containers, login to two different accounts. At least one account should have admin privileges in order to invite users.
2. In the other account under the [preferences tab](https://schedule.happy.tools/preferences), notice the user email, change the email to ``boy_child@wearehackerone.com`` and save changes.
3. In the admin account under the [users tab](https://schedule.happy.tools/admin/users), click on ``Invite team members`` and input the email ``boy_child@wearehackerone.com``.
4. Scroll down and click on ``Send invite``.
5. The request will fail.
6. Repeat steps 2 to 4, but changing the email to that of other users (test accounts) and the request to send an invite link will continuously fail.

## Impact

Through user enumeration of emails and mass exploitation, there is a permanent denial of service denying a Happy Tools admin from adding team members to their organization.

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
