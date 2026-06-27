---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '78052'
original_report_id: '78052'
title: xss in group
weakness: Cross-site Scripting (XSS) - Generic
team_handle: ok
created_at: '2015-07-23T06:11:43.051Z'
disclosed_at: '2016-07-10T05:35:59.729Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# xss in group

## Metadata

- HackerOne Report ID: 78052
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: ok
- Disclosed At: 2016-07-10T05:35:59.729Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

step:

payload : "><svg onload=prompt(document.domain) >

1.first create a new group.
2. now create new post,
3. now put payload in new topic and than click on add poll.
4. xss executed.

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
