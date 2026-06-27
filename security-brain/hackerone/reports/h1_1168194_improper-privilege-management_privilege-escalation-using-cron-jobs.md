---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1168194'
original_report_id: '1168194'
title: Privilege Escalation Using Cron Jobs
weakness: Improper Privilege Management
team_handle: versa-networks
created_at: '2018-11-19T00:00:00.000Z'
disclosed_at: '2021-05-05T20:17:51.227Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- improper-privilege-management
---

# Privilege Escalation Using Cron Jobs

## Metadata

- HackerOne Report ID: 1168194
- Weakness: Improper Privilege Management
- Program: versa-networks
- Disclosed At: 2021-05-05T20:17:51.227Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In Versa Analytics, the cron jobs are used for scheduling tasks by executing commands at specific dates and times on the server. If the job is run as the user root, there is a potential privilege escalation vulnerability. In this case, the job runs a script as root that is writable by users who are members of the versa group.

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
