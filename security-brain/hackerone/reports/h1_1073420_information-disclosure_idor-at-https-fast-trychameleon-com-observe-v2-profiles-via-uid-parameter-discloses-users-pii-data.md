---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1073420'
original_report_id: '1073420'
title: IDOR at https://fast.trychameleon.com/observe/v2/profiles/ via uid parameter
  discloses users' PII data
weakness: Information Disclosure
team_handle: topcoder
created_at: '2021-01-07T12:15:17.863Z'
disclosed_at: '2021-02-03T16:56:02.718Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: www.topcoder.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# IDOR at https://fast.trychameleon.com/observe/v2/profiles/ via uid parameter discloses users' PII data

## Metadata

- HackerOne Report ID: 1073420
- Weakness: Information Disclosure
- Program: topcoder
- Disclosed At: 2021-02-03T16:56:02.718Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hello,

A API on apps.topcoder.com/forums/ exposes the email of any user on topcoder.com and some PIIs (name, surname, id).


## Steps To Reproduce:
1) Create a profile at topcoder.com
2) Go to apps.topcoder.com/forums and login forum
3) Entery any topic (example: https://apps.topcoder.com/forums/?module=Thread&threadID=966515&start=0)
4) Open Intercept and click "Watch Thread" button
5) Catch the request and send to repeater, it will look like this:
F1147918
(This request comes from fast.trychameleon.com, but fast.trychameleon.com is not the cause of the security vulnerability.)
6) Let's go into the profile of any user on topcoder.com. (this is my other user and target user: https://www.topcoder.com/members/nomadex41)
7) Press F12 and search(CTRL-F) "userID"
F1147928
8) Copy the "userID" value and replace it with the "uid" part in the HTTP request.
9) Also give a random value to the title of the request ( POST /observe/v2/profiles/randomvalue HTTP/1.1) and sumbit.
poC: F1147950

Leaked all topcoder users email, name, surname and profile_id information. 
This is not public visible to other users.

This vulnerability is not caused by fast.trychameleon.com, because the userID values ​​are open in the topcoder.

Best Regards.

## Impact

Leaked all topcoder users email
PIIs leak

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
