---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '20049'
original_report_id: '20049'
title: Cross-site Scripting in mailing (username)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: relateiq
created_at: '2014-07-14T17:01:53.000Z'
disclosed_at: '2014-12-27T13:43:20.853Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Cross-site Scripting in mailing (username)

## Metadata

- HackerOne Report ID: 20049
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: relateiq
- Disclosed At: 2014-12-27T13:43:20.853Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There appears to be a Cross-site Scripting vulnerability related to [my previous report](https://hackerone.com/reports/2735) in the newsletter mailing. See my attached screenshot.

The steps to exploit and the impact are the same as in the previous report, but to exploit this specific XSS an attacker would have to register an account with someone else's e-mail address. 

Because the previous issue is fixed, this implies that there is no global sanitation for e-mails. I recommend checking all mailing scripts/tools for proper sanitation of variables (like the username).

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
