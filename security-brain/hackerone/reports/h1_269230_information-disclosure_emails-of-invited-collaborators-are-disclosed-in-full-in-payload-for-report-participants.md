---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '269230'
original_report_id: '269230'
title: Emails of invited collaborators are disclosed in full in payload for report
  participants
weakness: Information Disclosure
team_handle: security
created_at: '2017-09-18T14:20:15.669Z'
disclosed_at: '2019-04-09T16:00:34.467Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 111
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Emails of invited collaborators are disclosed in full in payload for report participants

## Metadata

- HackerOne Report ID: 269230
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2019-04-09T16:00:34.467Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Hackerone added new feature in which hackers can add collaborators to their reports.
this can be done using two ways: 
 1. by email address
 2. by user name  
adding hackers using their email address doesn't disclose the email address of the hacker and every participant will see something like this in the comments section of the specific report:

```
flashdisk  invited m.*************************om as a collaborator.
```
 
but moving the mouse pointer over the hacker icon would reveal his email address to all participants for that report which is definitely should hidden.  

#Fix

the email address should be hidden also in the upper report section.
please look at the attached screenshot which discloses my email address:

{F221867}

 
thanks.

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
