---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '43846'
original_report_id: '43846'
title: No Limitation on Following allows user to follow people automatically!
weakness: Cross-Site Request Forgery (CSRF)
team_handle: vimeo
created_at: '2015-01-15T01:06:36.337Z'
disclosed_at: '2016-05-02T14:46:24.611Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# No Limitation on Following allows user to follow people automatically!

## Metadata

- HackerOne Report ID: 43846
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: vimeo
- Disclosed At: 2016-05-02T14:46:24.611Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
i'm not sure it's intentional or somehow you missed it, I noticed that when User follow people on Vimeo, CSRF token of the request doesn't change at all.
It's become something like a static code for a single session.
ex:
POST: https://vimeo.com/user12345 <= [ID]
POST CONTENT: action=toggle_follow&token=[TOKEN]

An attacker can misuse this function with intruder/repeater and Follow as much people he want to follow.
like all he have do is put the URL on repeater/intruder with auto increment value (a number increased by 1 for every request). that's it.

for testing purpose, i ran a intruder attack with 500 user id and it successfully followed all available users from the list. (screenshot attached)
you can check here too: https://vimeo.com/faisalahmed/following

FIX:
it can be fixed by implementing unique CSRF token for every request (regenerating CSRF token)
or you can limit following feature.

Looking forward!

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
