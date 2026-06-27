---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47349'
original_report_id: '47349'
title: Stored xss in user name (2) affected another user.
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mobilevikings
created_at: '2015-02-10T18:07:53.209Z'
disclosed_at: '2015-03-04T14:30:14.798Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored xss in user name (2) affected another user.

## Metadata

- HackerOne Report ID: 47349
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mobilevikings
- Disclosed At: 2015-03-04T14:30:14.798Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Again we have to users:
A - attacker
B - victim

User A (attacker) has name - name<script>alert(1)</script> and add auth to user B (victim).
User B receive a letter and get remider about new request on website. And open it
https://mobilevikings.com/account/requests/
And probably press "Accept" and got xss fired.
x:confirm parameter is the reason of this issue.

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
