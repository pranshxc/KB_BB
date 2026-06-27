---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '12949'
original_report_id: '12949'
title: Open Redirection
weakness: Open Redirect
team_handle: urbandictionary
created_at: '2014-05-23T19:07:24.675Z'
disclosed_at: '2014-07-08T10:00:28.260Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- open-redirect
---

# Open Redirection

## Metadata

- HackerOne Report ID: 12949
- Weakness: Open Redirect
- Program: urbandictionary
- Disclosed At: 2014-07-08T10:00:28.260Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Try to connect your facebook using this URL

http://www.urbandictionary.com/auth/facebook?origin=http://google.com

after connecting urbandictionary to FB you will be redirected to google.com

and that is bad because hackers can get the auth token

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
