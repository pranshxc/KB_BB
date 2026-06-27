---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1131306'
original_report_id: '1131306'
title: User's who are banned from program can still be invited to the new reports
  as collaborators
weakness: Business Logic Errors
team_handle: security
created_at: '2021-03-20T11:32:22.680Z'
disclosed_at: '2021-09-22T19:36:01.370Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# User's who are banned from program can still be invited to the new reports as collaborators

## Metadata

- HackerOne Report ID: 1131306
- Weakness: Business Logic Errors
- Program: security
- Disclosed At: 2021-09-22T19:36:01.370Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello team!

We have found out that the banned user's (who are banned from program) can be invited to the new reports as collaborator users. This is pretty weird because the hacker should be banned and no new reports shouldn't be allowed.  

If program bans the hacker the program can't invite s/he back to be part of program. That's why we see that this is real issue and should be mitigated.

## Steps To Reproduce:

- Login to the system as an user who has right to invite hackers to the program
- Invite two hacker let say hacker A and hacker B at `https://hackerone.com/<program name>/launch`
- Make sure you have bounty split on at `https://hackerone.com/██████████/submission_requirements`
- Login and submit new report as an hacker A
- As a program user navigate to  this new report, close report and ban the user
- As a hacker B login and submit new report to this program
- Invite banned hacker A to this report as a collaborator
- Login as hacker A, check your email inbox and accept the collaborator invitation
- Hacker A were able to participate the program as a banned hacker

## Recommendation:

After a hacker is banned from a program the hackerone should ensure that s/he can't be invited to the new reports as a collaborator

## References:

-

## Impact

Banned hackers can still participate the program as a collaborator user

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
