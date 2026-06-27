---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '19640'
original_report_id: '19640'
title: Session Hijacking attack (Different Scenario)
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2014-07-10T06:00:49.279Z'
disclosed_at: '2014-07-17T22:35:24.956Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
tags:
- hackerone
- improper-authentication-generic
---

# Session Hijacking attack (Different Scenario)

## Metadata

- HackerOne Report ID: 19640
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2014-07-17T22:35:24.956Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hey 
I was able to replay a cookie of a current active session and hijack that by replaying the cookie. Now this is different from any conventional vanilla session hijacking because it works even when the user is not logged in. But the condition is that the victim's session must be active at the time of replay
1. Capture a cookie from one account using tamper data just note that you learn the Referer and X-XHR-Referer values

2. Open a new windows click on the same link without logging in. For example in the victim account i clicked on "bugs" so here in order to replay the cookie i have to click on bugs again. Replay the X-XHR value with the other one. Replay the session cookie and you are in. You hacked the account.

I hope this impresses you because i have been trying hard to get you guys impressed. Although i have managed to do with the other ones :)
Waiting for your reply

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
