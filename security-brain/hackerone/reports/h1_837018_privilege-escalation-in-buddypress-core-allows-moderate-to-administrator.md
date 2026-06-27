---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '837018'
original_report_id: '837018'
title: Privilege Escalation in BuddyPress core allows Moderate to Administrator
team_handle: wordpress
created_at: '2020-04-02T10:44:14.895Z'
disclosed_at: '2020-05-22T00:31:34.282Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: BuddyPress Core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Privilege Escalation in BuddyPress core allows Moderate to Administrator

## Metadata

- HackerOne Report ID: 837018
- Weakness: 
- Program: wordpress
- Disclosed At: 2020-05-22T00:31:34.282Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description:

BuddyPress core allows Moderate to Administrator in Manage Group Members module

## Steps To Reproduce:

Step 1 : Create two account with two groups
Step 2 : In account A, create group abc with this two users.
Step 3 : Administrator in group abc promote account B to Moderator
Step 4 : In account B, create own group(without account A), only account B.
Step 5: In account B, access quick link here:
domain/groups/[group_name]/admin/manage-members/ 
Change your B's group.
There are  Edit | Ban | Remove for you to select. Focusing to admin(When you are admin, all thing belongs you).
Therefore, I select Edit. Change to Moderate(To capture this request)
Change such as here:
In POST method: 
POST /wp-json/buddypress/v1/groups/[group_A_id]/members/[id_user] HTTP/1.1
In body/data:
action=promote&role=admin
Note: change [group_A_id] to group you are moderator and [id_user]- your id
Step 6: Done, you are admin's group A. You can do anything.

Poc with video

## Recommendations
Valid user with their roles

## Impact

User will takeover group, do anything such as, edit roles,remove, ban, delelte group,..... (Perform as administrator)

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
