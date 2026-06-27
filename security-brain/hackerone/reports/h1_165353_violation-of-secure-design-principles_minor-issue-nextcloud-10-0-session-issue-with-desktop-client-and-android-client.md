---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '165353'
original_report_id: '165353'
title: '**minor issue ** -Nextcloud 10.0 session issue with desktop client and android
  client'
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-09-02T18:16:30.152Z'
disclosed_at: '2020-03-01T15:01:20.331Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# **minor issue ** -Nextcloud 10.0 session issue with desktop client and android client

## Metadata

- HackerOne Report ID: 165353
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2020-03-01T15:01:20.331Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Scenario:
***********
--> Installed nextcloud 10.0 locally and created "admin" account
--> Installed nextcloud desktop client and andoid client

I found session related vulnerability in nextcloud 10.0 where killing session in User(admin) --> Personal --> Sessions not actually killing sessions in desktop client

Steps:
1) Logged into admin account in browser
2) Logged into admin account in desktop client and android client. Currently admin account is having 3 sessions : browser, desktop, andoid
3) Goto User(admin) --> Personal --> Sessions --> kill desktop client session --> upload new file using browser --> Still dekstop client is syncing files without asking any password prompt (issue1)
4) Though android client is still  active, sessions are not capturing in personal --> sessions tab

Hope these are minor issues

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
