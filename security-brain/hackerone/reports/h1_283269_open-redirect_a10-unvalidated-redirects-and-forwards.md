---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '283269'
original_report_id: '283269'
title: A10 – Unvalidated Redirects and Forwards
weakness: Open Redirect
team_handle: infogram
created_at: '2017-10-26T15:23:12.018Z'
disclosed_at: '2017-11-09T13:08:19.382Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# A10 – Unvalidated Redirects and Forwards

## Metadata

- HackerOne Report ID: 283269
- Weakness: Open Redirect
- Program: infogram
- Disclosed At: 2017-11-09T13:08:19.382Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

https://infogram.com/login

Web applications frequently redirect and forward users to other pages and websites, and use untrusted data to determine the destination pages. Without proper validation.
when i intercept the twitter request and change it to the google then it will redirect you to the google.
application should also verify the original request from the browser.

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
