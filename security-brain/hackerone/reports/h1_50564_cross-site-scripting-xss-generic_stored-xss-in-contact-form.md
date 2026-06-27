---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '50564'
original_report_id: '50564'
title: Stored XSS in Contact Form
weakness: Cross-site Scripting (XSS) - Generic
team_handle: concretecms
created_at: '2015-03-08T10:28:48.870Z'
disclosed_at: '2015-07-08T18:33:15.224Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in Contact Form

## Metadata

- HackerOne Report ID: 50564
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: concretecms
- Disclosed At: 2015-07-08T18:33:15.224Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In Contact form there is an option to display Message  when completed.
There I have put the payload
payload: "><img src=x onerror=alert(1)>

and the payload executed and saved permanently.

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
