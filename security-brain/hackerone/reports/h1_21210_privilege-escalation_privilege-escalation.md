---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '21210'
original_report_id: '21210'
title: privilege escalation
weakness: Privilege Escalation
team_handle: mavenlink
created_at: '2014-07-23T13:15:52.763Z'
disclosed_at: '2014-08-05T16:33:52.257Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# privilege escalation

## Metadata

- HackerOne Report ID: 21210
- Weakness: Privilege Escalation
- Program: mavenlink
- Disclosed At: 2014-08-05T16:33:52.257Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Consider Two browsers say X and Y, also consider two users say A and B.
2. Sign in to https://app.mavenlink.com using user A through browser X, same as login with user B through browser Y.
3. Now create a project through user A, and add user B as a consultant with Team Lead privilege.
4. Now access this project through user B, and click on invite. A console will open asking for email id. Leave it as it is here and move to user A.
5.  Access the user A console through browser X, and set the privilege of user B to Collaboration and also remove the invite privilege just corresponding to that user, as shown in image below.Now save it.
6. Now move to user B again from where we left in step 4. Enter any email id and submit the request. You will see request will get completed successfully and given user will be invited, while this user doesn't having any privilege to do so..

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
