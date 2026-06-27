---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '11073'
original_report_id: '11073'
title: XSS in gist integration
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2014-05-06T18:21:27.236Z'
disclosed_at: '2019-04-28T00:11:34.790Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 154
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in gist integration

## Metadata

- HackerOne Report ID: 11073
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2019-04-28T00:11:34.790Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Create a gist called:
"><svg onload=alert(1)>
2. have gist integration enabled and put a link in a slack chat
3. Visit the 'raw' or 'new window' pages for this gist, for example: https://outpost.slack.com/files/zemnmez/F029MDY33/___svg_onload_alert_1__

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
