---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '442901'
original_report_id: '442901'
title: Take over of accounts created using Google or Facebook
weakness: Cross-Site Request Forgery (CSRF)
team_handle: khanacademy
created_at: '2018-11-16T20:54:56.443Z'
disclosed_at: '2019-05-17T03:36:27.301Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 178
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Take over of accounts created using Google or Facebook

## Metadata

- HackerOne Report ID: 442901
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: khanacademy
- Disclosed At: 2019-05-17T03:36:27.301Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

When a user creates an account using Google or Facebook and does not set an additional password, it is possible to set their passwords via CSRF.
Since the account is created using a social media account, no existing password check is needed and the CSRF check on the endpoint is broken. 
To reproduce, create an account with Google or Facebook and make account load the attached HTML file. You should now be able to login to the account with password=ATTACKER_PASS.

## Impact

An attacker can take over of accounts created using Google or Facebook.

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
