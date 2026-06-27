---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1005020'
original_report_id: '1005020'
title: Identify unique user ID of all the profiles
weakness: Insecure Direct Object Reference (IDOR)
team_handle: bumble
created_at: '2020-10-11T09:42:06.236Z'
disclosed_at: '2020-12-25T10:53:51.918Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Identify unique user ID of all the profiles

## Metadata

- HackerOne Report ID: 1005020
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: bumble
- Disclosed At: 2020-12-25T10:53:51.918Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Through this vulnerability, one can know the unencrypted user ID of all the profiles 


Steps to reproduce:
1. Login to your Bumble profile
2. In the SERVER_GET_USER_LIST API replace the folder ID 0 with 7. This folder contains all the profiles in your deck /which you have right-swiped on (screenshot 1); Through this, we may choose to again swipe left on them if desired.
3. Intercept the response. The unique user ID of the profile is shown in plain text. 
4. Adding additional parameters to the projection field also gives us information like the user vote, etc. 
5. We can even increase the 'count' to get details of more profiles

## Impact

In case of a match, this information can be used by a male's profile to craft a message and initiate the chat, as the 'is_match' field is true and the 'user_id' field is now available. (Screenshot 2)

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
