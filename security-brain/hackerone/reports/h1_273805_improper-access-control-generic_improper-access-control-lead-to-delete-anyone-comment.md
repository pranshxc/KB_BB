---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '273805'
original_report_id: '273805'
title: Improper access control lead  To delete anyone comment
weakness: Improper Access Control - Generic
team_handle: paragonie
created_at: '2017-10-02T16:38:32.956Z'
disclosed_at: '2017-10-16T05:48:54.911Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- improper-access-control-generic
---

# Improper access control lead  To delete anyone comment

## Metadata

- HackerOne Report ID: 273805
- Weakness: Improper Access Control - Generic
- Program: paragonie
- Disclosed At: 2017-10-16T05:48:54.911Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

SUMMURY
========================
Here server dont check the owner of any comment.
During Comment deletion it does not check whether the comment is  created by user or not.
so i can delete a comment of others user.

STEP TO REPRODUCE
=======================
1. goto https://localhost:8080/blog/comments .

2. select any commnet which is already aproved.

3.Unaprove it by clicking "Hide Comment".

4. Now delete that commnet and see comment is deleted which is not created by himself.

FIX
========
implement proper access control mechanism so that when user try to delete a comment first check the comment is belongs to that user or not.

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
