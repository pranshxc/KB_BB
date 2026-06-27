---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181748'
original_report_id: '181748'
title: '[IDOR][translate.twitter.com] Opportunity to change any comment at the forum'
weakness: Privilege Escalation
team_handle: x
created_at: '2016-11-12T13:24:04.119Z'
disclosed_at: '2017-05-12T20:35:58.486Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 37
tags:
- hackerone
- privilege-escalation
---

# [IDOR][translate.twitter.com] Opportunity to change any comment at the forum

## Metadata

- HackerOne Report ID: 181748
- Weakness: Privilege Escalation
- Program: x
- Disclosed At: 2017-05-12T20:35:58.486Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

POC: https://translate.twitter.com/forum/getting-started/topics/7037/posts/43287/edit
Steps to reproduce:
1) Go to any forums topic for example: https://translate.twitter.com/forum/getting-started/topics/7037
2) View source code of the page and take post id (screenshot "idor edit.jpg")
3) Append "/posts/*post_id*/edit" to url at the first step (screenshot "idor edit 2.jpg")
4) Make some change at the comment and save it

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
