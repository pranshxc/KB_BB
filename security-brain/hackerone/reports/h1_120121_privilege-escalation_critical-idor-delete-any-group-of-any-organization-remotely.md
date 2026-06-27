---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '120121'
original_report_id: '120121'
title: Critical IDOR - Delete any group of any organization remotely
weakness: Privilege Escalation
team_handle: veris
created_at: '2016-03-02T13:47:12.995Z'
disclosed_at: '2016-06-12T16:06:10.165Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# Critical IDOR - Delete any group of any organization remotely

## Metadata

- HackerOne Report ID: 120121
- Weakness: Privilege Escalation
- Program: veris
- Disclosed At: 2016-06-12T16:06:10.165Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

I have found a critical IDOR for deleting any groups of any organization remotely. It means an attacker can easily delete any group of any organization from his account by just chaning the group_id in delete request.

This is similar to previously reported IDOR to delete any members. So I am not writing down steps to reproduce again as it is also similar but jut to perform in Groups section.

Proof of Concept: Please find the attached screenshots.

Do evaluate it and inform me accordingly.

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
