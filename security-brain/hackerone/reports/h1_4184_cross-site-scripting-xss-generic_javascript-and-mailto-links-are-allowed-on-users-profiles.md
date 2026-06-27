---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '4184'
original_report_id: '4184'
title: 'javascript: and mailto: links are allowed on users'' profiles'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: security
created_at: '2014-03-17T02:23:21.441Z'
disclosed_at: '2015-05-13T16:32:01.960Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# javascript: and mailto: links are allowed on users' profiles

## Metadata

- HackerOne Report ID: 4184
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: security
- Disclosed At: 2015-05-13T16:32:01.960Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

For user's Profile settings, you accept website URLs like mailto:hello@foo.com and even javascript:alert(1).  The Content Security Policy directive in Chrome catches the JavaScript one, but older browsers will almost certainly execute the code, allowing for session stealing or XSS code execution attacks when the link is clicked.

Your JS prints "Website is not valid.", but hitting return still submits it.

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
