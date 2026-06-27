---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '120126'
original_report_id: '120126'
title: Critical IDOR - Delete any rule of any organization remotely
weakness: Privilege Escalation
team_handle: veris
created_at: '2016-03-02T14:15:05.456Z'
disclosed_at: '2016-06-12T16:05:49.771Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# Critical IDOR - Delete any rule of any organization remotely

## Metadata

- HackerOne Report ID: 120126
- Weakness: Privilege Escalation
- Program: veris
- Disclosed At: 2016-06-12T16:05:49.771Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

I have found a critical IDOR issue which escalates a user privilege and allows and attacker to delete any rule of any organization remotely through his own account by just changing the [rule id] in DELETE Request.

This is again similar to previously reported critical IDORs to delete a member,group and venue. Thus, I am not writing steps again as they are same but just to perform under venue section.

Proof of Concept: Please find the attached screenshots.

Best Regards,

Hely H. Shah

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
