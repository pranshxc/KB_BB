---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2638'
original_report_id: '2638'
title: CSRF on add comment section
weakness: Cross-Site Request Forgery (CSRF)
team_handle: slack
created_at: '2014-03-01T23:27:57.170Z'
disclosed_at: '2014-04-12T00:34:45.972Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF on add comment section

## Metadata

- HackerOne Report ID: 2638
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: slack
- Disclosed At: 2014-04-12T00:34:45.972Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Steps to repro:

1) Go to this link https://sehacure.slack.com/help/requests/237956

2) The malicious guy should now the request number and the username.

3) Open Tamper data using tamper data firefox addon,Fill the reply in the form.

4) Submit the request.You will see there are no anti-csrf token in the request.

Impact:

Submit a lot of fake response from the victim account.

Please have a look.

Best,
Anand

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
