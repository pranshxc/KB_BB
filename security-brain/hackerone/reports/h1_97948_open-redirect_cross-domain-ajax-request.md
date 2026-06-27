---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '97948'
original_report_id: '97948'
title: Cross-domain AJAX request
weakness: Open Redirect
team_handle: security
created_at: '2015-11-05T02:02:04.633Z'
disclosed_at: '2015-11-14T15:22:16.880Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- open-redirect
---

# Cross-domain AJAX request

## Metadata

- HackerOne Report ID: 97948
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2015-11-14T15:22:16.880Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Two weeks ago, I found a Cross-domain AJAX request, but due to the fact that you uses a very strict Content Security Policy, I hesitated to send this. Today, I noticed that bug has been fixed. But this fix can be bypassed.

This example not working now (screenshot 1):

https://hackerone.com/bugs?subject=/google.com/


But if will be (screenshot 2):

https://hackerone.com/bugs?subject=/hackerone.com@google.com/
or https://hackerone.com/bugs?subject=%2Fhackerone.com.google.com


It's will work.

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
