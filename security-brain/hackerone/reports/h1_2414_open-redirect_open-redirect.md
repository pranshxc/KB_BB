---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2414'
original_report_id: '2414'
title: open redirect
weakness: Open Redirect
team_handle: relateiq
created_at: '2014-02-28T12:12:30.939Z'
disclosed_at: '2014-05-19T08:37:33.173Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- open-redirect
---

# open redirect

## Metadata

- HackerOne Report ID: 2414
- Weakness: Open Redirect
- Program: relateiq
- Disclosed At: 2014-05-19T08:37:33.173Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

1. go to https://www.relateiq.com/sign-up
2. Fill the form and click on signup free button.
3. Intercept the request using tamper data and change the 'retURL' parameter to any value like https://google.com (any evil url) and submit the request.
4. The web app redirect to any evil website.

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
