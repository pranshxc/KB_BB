---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1202408'
original_report_id: '1202408'
title: No Rate Limit on redditgifts gift  when Adding Comment
weakness: Violation of Secure Design Principles
team_handle: reddit
created_at: '2021-05-19T06:09:45.737Z'
disclosed_at: '2021-10-21T19:52:19.094Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
asset_identifier: '*.redditgifts.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# No Rate Limit on redditgifts gift  when Adding Comment

## Metadata

- HackerOne Report ID: 1202408
- Weakness: Violation of Secure Design Principles
- Program: reddit
- Disclosed At: 2021-10-21T19:52:19.094Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,
I hope this report should not be closed as INFORMATIVE

#**Summary:**
The add comment endpoint was improperly rate-limited so the potential attacker could post a large number of comments, overloading the server .

#**Description:**
The add comment endpoint has a speed limit, but the number is set too high, so speed limiting is activated when you write more than 1000 comments per minute.

#**Environment:**
Scope: Web Application
Attack type: OWASP API TOP10 Lack of Resources & Rate Limiting
Maximum user privileges needed to reproduce your issue: no privileges

#**Steps To Reproduce:**
1.Go to any post.
2.Turn on Intercept and Add a Comment.
3.Send request to Intruder.
4.Set your payloads and start attack.
5.There is no rate-limit.

#**Note:**
If there is any problem in reproduction from your side then i will provide you with video poc.

#**POC:**
You can observe the time taken to load the post before performing the attack and after performing the attack. It will show  that the post takes alot time to load after the attack. 

#**Fix:**
Developers alleviated the problem by setting the speed limit to low for endpoints that set the speed too high. 

Regards,
Gaurav Bhatia

## Impact

No rate limit on comments can lead to slow down of server due to large number of comments in the post.

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
