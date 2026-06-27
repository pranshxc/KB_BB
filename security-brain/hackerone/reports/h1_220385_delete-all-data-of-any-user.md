---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '220385'
original_report_id: '220385'
title: Delete All Data of Any User
team_handle: nextcloud
created_at: '2017-04-12T04:11:31.638Z'
disclosed_at: '2020-03-01T14:10:36.716Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
---

# Delete All Data of Any User

## Metadata

- HackerOne Report ID: 220385
- Weakness: 
- Program: nextcloud
- Disclosed At: 2020-03-01T14:10:36.716Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

If you are user have permission manage user(admin group), you can delete all data off website.
step:
1. Create new user with username is '.'.
2. Delete user, who just have been created.

Cause:
when you create new use, nextcloud app will make a new folder same name with username, which have been created. in folder (sourceweb/data)
Unfortunately, if username is '.', nextcloud app will make a new folder has name is '.'.
And when you delete user, nextcloud app will remote all folder 'data'.

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
