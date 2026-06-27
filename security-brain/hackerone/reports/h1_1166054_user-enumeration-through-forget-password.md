---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1166054'
original_report_id: '1166054'
title: User enumeration through forget password
team_handle: upchieve
created_at: '2021-04-15T21:54:00.967Z'
disclosed_at: '2021-05-16T01:59:36.203Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 47
asset_identifier: app.upchieve.org
asset_type: URL
max_severity: none
tags:
- hackerone
---

# User enumeration through forget password

## Metadata

- HackerOne Report ID: 1166054
- Weakness: 
- Program: upchieve
- Disclosed At: 2021-05-16T01:59:36.203Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Vulnerability:-
->User enumeration is possible through forgot password feature.
steps to reproduce:-
->Go to the above selected domain and go to forgot password.
->submit random email and then intercept request  by burp suit 
->in response you will get { HTTP/1.1 500 Internal Server Error with {{"err":"No account with that id found."} } 

Remediation:-
->It should display like "if that mail address exists in our system, then we will send password reset link."
I hope that you will consider this issue as you also welcome the reports of best practices.
Thank you

## Impact

Leaking users' emails. / Information Disclosure.

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
