---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7919'
original_report_id: '7919'
title: XSS via Email
weakness: Cross-site Scripting (XSS) - Generic
team_handle: respondly
created_at: '2014-04-17T20:24:39.725Z'
disclosed_at: '2014-04-21T16:11:30.529Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS via Email

## Metadata

- HackerOne Report ID: 7919
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: respondly
- Disclosed At: 2014-04-21T16:11:30.529Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

This one was easy.

Someone needs send an email with **Subject** line : *"><img src=x onerror=alert(document.cookie);>* to the team email, mine was **kfvm@mail.respond.ly**

So once the email arrives it will execute Javascript (See attachment)

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
