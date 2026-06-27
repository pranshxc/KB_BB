---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '177757'
original_report_id: '177757'
title: Stored XSS in Restoring Archived Tasks
weakness: Cross-site Scripting (XSS) - Generic
team_handle: harvest
created_at: '2016-10-24T10:11:35.407Z'
disclosed_at: '2016-12-15T11:07:06.008Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in Restoring Archived Tasks

## Metadata

- HackerOne Report ID: 177757
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: harvest
- Disclosed At: 2016-12-15T11:07:06.008Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Harvest Team,

There is stored XSS in restoring archived/deleted tasks.

POC:
1. Create a task with name with xss payload "><img src=x onerror=alert(document.domain)>
2. Now from Tasks, delete the task and the task will be archived.
3. Now Click on Manage archived tasks, to restore it back.
4. Click on the task with xss payload, XSS is triggered.

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
