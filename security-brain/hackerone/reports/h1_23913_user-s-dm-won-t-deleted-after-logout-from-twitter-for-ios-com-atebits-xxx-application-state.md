---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '23913'
original_report_id: '23913'
title: User's DM won't deleted after logout from Twitter for iOS (com.atebits.xxx.application-state)
team_handle: x
created_at: '2014-08-12T20:19:05.869Z'
disclosed_at: '2015-02-25T23:10:44.337Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# User's DM won't deleted after logout from Twitter for iOS (com.atebits.xxx.application-state)

## Metadata

- HackerOne Report ID: 23913
- Weakness: 
- Program: x
- Disclosed At: 2015-02-25T23:10:44.337Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to add an additional information regarding my previous report about "Unencrypted User's DM and Statuses on twitter.db at Twitter for iOS". I have already tried to logout from my Twitter apps (including from built-in twitter apps for iOS), and then, I already reboot the iDevice too. (tested on iPhone 5 with the same version of Twitter Apps).

In this situation, the twitter.db that located on Cache isn't appear anymore. But, Attacker could still access the User's DM including username and their chat partner from "app.acct.username-some.random.number.detail.10" that could be found on: "Applications > Documents > com.atebits.xxx.application-state".

For support my explanation, I attached the screenshot in this post too.

nb: I'm sorry for opening another ticket. Because, I see that the status is already closed on previous ticket.


Best Regard,

YoKo

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
