---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6035'
original_report_id: '6035'
title: open redirect in https://slack.com
weakness: Open Redirect
team_handle: slack
created_at: '2014-04-06T11:01:05.186Z'
disclosed_at: '2014-05-31T18:42:06.536Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- open-redirect
---

# open redirect in https://slack.com

## Metadata

- HackerOne Report ID: 6035
- Weakness: Open Redirect
- Program: slack
- Disclosed At: 2014-05-31T18:42:06.536Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Navigate to Https://slack.com
append "/link?url=url=http://bing.com" or enter any website of your choice with http://
vulnerable link https://slack.com/link?url=http://bing.com
notice that user is redirected to bing.com without being validated or notified

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
