---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '224108'
original_report_id: '224108'
title: Cross Site Scripting
team_handle: nextcloud
created_at: '2017-04-26T17:06:48.936Z'
disclosed_at: '2017-04-26T17:36:30.399Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
---

# Cross Site Scripting

## Metadata

- HackerOne Report ID: 224108
- Weakness: 
- Program: nextcloud
- Disclosed At: 2017-04-26T17:36:30.399Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello team,
While i was hunting (https://help.nextcloud.com), i found xss there in comment/reply box..

**Steps to reproduce**
1. go to https://help.nextcloud.com.
2. Click On Any (I'm selecting "Welcome to the Nextcloud forums")
3. Sign in or Sign up in your account.
4. Click Reply..
5. Type or paste ( <abbr title='" class="comment-link"><a href='
href="'> :-) <abbr title='" ' class="<script>alert(document.cookie)</script>">x</abbr></a> ) Without brackets..
6. You will get popup (You need to be logged in to do that.)
7. This mean xss payload is executing!

**Detail:**
I think xss payload is executing because you're using old version of akismet..
Akismet 2.5.0-3.1.4 - Is vulnerable to  Unauthenticated Stored Cross-Site Scripting (XSS).. 

Reference: https://wpvulndb.com/vulnerabilities/8215

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
