---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '120115'
original_report_id: '120115'
title: Critical - Insecure Direct Object Reference - Deleting any member of any organization
  remotely
weakness: Privilege Escalation
team_handle: veris
created_at: '2016-03-02T13:26:48.647Z'
disclosed_at: '2016-06-12T16:06:40.854Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- privilege-escalation
---

# Critical - Insecure Direct Object Reference - Deleting any member of any organization remotely

## Metadata

- HackerOne Report ID: 120115
- Weakness: Privilege Escalation
- Program: veris
- Disclosed At: 2016-06-12T16:06:40.854Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

I have found an extremely critical issue with the help of which an attacker can delete any member of any organization. The vulnerability is Insecure Direct Object Reference(IDOR) which leads to privilege escalation as an attacker can perform such a critical attack from his own account.

Vulnerable URL: DELETE /api/v1/org-member/4/[MEMBER_ID]/

On changing the member id, application allows an attacker to delete that member. I tried using my 2 accounts and got success in the same.

Steps to Reproduce:'

1. Login to your Veris View Portal.
2. Go to Member Book.
3. Set up Burp Suite to intercept the request OR simply edit the member id from browser's Inspect Element feature.
4. Delete a Member and intercept the request.
5. Replace the member id with some other member of other organization.
6. Forward the request.
7. Check in the other organization. Member would be deleted.

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
