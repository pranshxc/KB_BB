---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '187410'
original_report_id: '187410'
title: Store XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2016-12-01T17:55:00.658Z'
disclosed_at: '2017-01-01T20:46:32.675Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 43
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Store XSS

## Metadata

- HackerOne Report ID: 187410
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2017-01-01T20:46:32.675Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team.

I found a Store XSS. Where the company name is the vulnerable to XSS. If you give this below XSS script as Company name, you will get the XSS pop up after the login in message option where it'll randomly generated at the message room.
“><IMG SRC=x onerror=javascript:alert(&quot;XSS-by-Imran&quot;)> 

 Here is the POC:
https://youtu.be/dqrH2WhIgtk

Thanks

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
