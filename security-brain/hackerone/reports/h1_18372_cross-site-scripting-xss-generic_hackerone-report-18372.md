---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '18372'
original_report_id: '18372'
title: HackerOne Report 18372
weakness: Cross-site Scripting (XSS) - Generic
team_handle: jsdelivr
created_at: '2014-06-29T09:47:12.991Z'
disclosed_at: '2014-07-29T10:55:13.703Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HackerOne Report 18372

## Metadata

- HackerOne Report ID: 18372
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: jsdelivr
- Disclosed At: 2014-07-29T10:55:13.703Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Dear Team,

Step-by-step instructions on how to reproduce the problem:

It was found the application is vulnerable to XSS attack.
To achieve the same,

open this link
http://staging.jsdelivr.net/g//%3Cimg/src=%22%3E%22+onerror=alert%28927942%29%3E

in firefox.

it can't prompt bcoz there is nothng just some code that's why it's can't prompt.
but when u write something there it will prompt.

Regard
Shubham Gupta

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
