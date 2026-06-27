---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2582'
original_report_id: '2582'
title: Session Fixation disclosing email address
weakness: Information Disclosure
team_handle: slack
created_at: '2014-03-01T16:49:14.281Z'
disclosed_at: '2014-03-31T20:20:52.683Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# Session Fixation disclosing email address

## Metadata

- HackerOne Report ID: 2582
- Weakness: Information Disclosure
- Program: slack
- Disclosed At: 2014-03-31T20:20:52.683Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Desc:
Session fixation occurs due to SessionID in URL. A valid session-URL should be only a one time use. In this case a valid session-URL remains active for infinite time. The browser/cache may store this unique Session-URL and disclose EMAIL address of the user.

Working:
1>Register
2>One registering, you will redirected to unique URL: https://slack.com/go/x-2xxxxx-f8xx7#signup
3>This link remains useable and valid and doesn't have an expiry.
4>Anyone having access to the browser history can access the link and hence the email is disclosed.

Fix:
One time use of the URL
Use of Expiry time (for ex: 10 mins) or so

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
