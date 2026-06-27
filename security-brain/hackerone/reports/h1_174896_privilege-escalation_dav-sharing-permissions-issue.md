---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '174896'
original_report_id: '174896'
title: Dav sharing permissions issue
weakness: Privilege Escalation
team_handle: nextcloud
created_at: '2016-10-10T07:55:37.422Z'
disclosed_at: '2017-05-20T21:57:21.170Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- privilege-escalation
---

# Dav sharing permissions issue

## Metadata

- HackerOne Report ID: 174896
- Weakness: Privilege Escalation
- Program: nextcloud
- Disclosed At: 2017-05-20T21:57:21.170Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

### Steps

1. Create users "Test 1" and "Test 2", make "Test 1" member of "Group A"
2. Share a calendar with group "Group A" editable
3. Share the same calendar with user "Test 2" readonly
4. As "Test 1" open the calendar app and unshare the calendar from "Test 2" - works
5. As "Test 1" open the calendar app and remove edit permissions for "Group A" - works

In my opinion steps 4 and 5 should not be possible. The shares should not even be visible in my opinion.

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
