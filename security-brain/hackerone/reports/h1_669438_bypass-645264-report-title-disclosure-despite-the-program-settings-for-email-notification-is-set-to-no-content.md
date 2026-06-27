---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '669438'
original_report_id: '669438'
title: '[Bypass #645264] Report title disclosure despite the program settings for
  email notification is set to "No Content"'
team_handle: security
created_at: '2019-08-08T02:35:48.109Z'
disclosed_at: '2019-09-09T01:30:46.991Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 102
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# [Bypass #645264] Report title disclosure despite the program settings for email notification is set to "No Content"

## Metadata

- HackerOne Report ID: 669438
- Weakness: 
- Program: security
- Disclosed At: 2019-09-09T01:30:46.991Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

**Summary:**

There is newly disclosed resolved report [Program Email Nofication settings ignored when being added as an external contributor](https://hackerone.com/reports/645264), However i found that the fix is incomplete.

I have found that email invitation for a collaborator (bounty splitting) still disclosing the __Report title__ in email when the notification comes from `Manage Collaborator` invitation.

### Steps To Reproduce

Assumes that __Manage Collaborator__ (bounty splitting) is enabled to the program

  1. As a program admin, navigate to *Program Settings > Click Program >Click Email Notifications*
  2. In email notification settings, select __No Content__
  3. Go to any report in your program and invite any hacker to the report to become a __Collaborator__.
  4. Hacker can also invite __Collaborator__.
  5. Check the invited hackers email, they will see the report title in the collaboration invitation email.


## PoC screenshot below:

{F549793}

{F549792}

## Impact

Sensitive information disclosing bypassing the program settings.

Regards
Japz

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
