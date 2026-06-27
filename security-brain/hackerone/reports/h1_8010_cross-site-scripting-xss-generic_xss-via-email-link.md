---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8010'
original_report_id: '8010'
title: XSS via Email Link
weakness: Cross-site Scripting (XSS) - Generic
team_handle: respondly
created_at: '2014-04-18T10:50:35.253Z'
disclosed_at: '2014-04-21T16:13:35.952Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS via Email Link

## Metadata

- HackerOne Report ID: 8010
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: respondly
- Disclosed At: 2014-04-21T16:13:35.952Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey,

So, we can send emails to team email address like  - **kfvm@mail.respond.ly** . In the email body if there is a hyperlink pointing to `javascript:alert(0);` or any other `javascript: URI` then open viewing the email in your web application with *original HTML* view and then on clicking it will trigger javascript execution, that is XSS.

Thanks!

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
