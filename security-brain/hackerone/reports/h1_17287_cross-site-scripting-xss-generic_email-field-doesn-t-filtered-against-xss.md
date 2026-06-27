---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '17287'
original_report_id: '17287'
title: email field doesn't filtered against XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uzbey
created_at: '2014-06-23T06:54:55.791Z'
disclosed_at: '2014-07-08T18:54:30.321Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# email field doesn't filtered against XSS

## Metadata

- HackerOne Report ID: 17287
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uzbey
- Disclosed At: 2014-07-08T18:54:30.321Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
Pre-configuration, create new contact in Gmail with mail a"><img src=y onerror=prompt(...);>

1. Go to Invites.
2. Click on Invite Gmail Friends.
3. Accept the pop up.
4. XSS will activate on the email field.


Few issues continue during this issue:
1. When you click on this email address you get failure on AJAX functionally.
2. If you try to do the same scenario I describe the system throw Error
The website encountered an unexpected error. Please try again later.

Sasi

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
