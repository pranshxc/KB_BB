---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '51817'
original_report_id: '51817'
title: Post in private groups after getting removed
weakness: Privilege Escalation
team_handle: vimeo
created_at: '2015-03-13T22:50:28.924Z'
disclosed_at: '2015-05-01T14:21:08.112Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- privilege-escalation
---

# Post in private groups after getting removed

## Metadata

- HackerOne Report ID: 51817
- Weakness: Privilege Escalation
- Program: vimeo
- Disclosed At: 2015-05-01T14:21:08.112Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Steps to reproduce:

1. A user(victim) have a private video and he have added it on his private groups. Now the group members can see it and comment to it.
2. The attacker is on the group and he adds a new comment and capture the request using burp proxy.
3. Then the attacker is removed from the group by the victim.
4.Now the attacker can't access the video and group anymore. But he can comment on that video by replaying the request captured in step 2.

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
