---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1210043'
original_report_id: '1210043'
title: Enumerate all the class codes via google dorking
weakness: Improper Access Control - Generic
team_handle: khanacademy
created_at: '2021-05-26T16:19:43.319Z'
disclosed_at: '2021-07-22T01:44:36.165Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 39
tags:
- hackerone
- improper-access-control-generic
---

# Enumerate all the class codes via google dorking

## Metadata

- HackerOne Report ID: 1210043
- Weakness: Improper Access Control - Generic
- Program: khanacademy
- Disclosed At: 2021-07-22T01:44:36.165Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I used this particular google dork `site:khanacademy.org/join/*` to enumerate all the links of joining classes. 

1. Go to google and use the above query to enumerate all of them. 
2. Create the student account by filling all the required details 
3. Now you're in the class without being actually invited by the teacher 

Attached POC:
████████

## Impact

An attacker can enumerate all the classes and join in them and make chaos there are chances of IDOR too... a class code can look like `a57d5d5548f302ef4a` instead of `A45JST`

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
