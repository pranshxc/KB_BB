---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '978768'
original_report_id: '978768'
title: Adding everyone to the repo due to the lack of rate limit
weakness: Insecure Direct Object Reference (IDOR)
team_handle: gitlab
created_at: '2020-09-10T22:21:21.780Z'
disclosed_at: '2020-09-14T23:28:30.952Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 6
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Adding everyone to the repo due to the lack of rate limit

## Metadata

- HackerOne Report ID: 978768
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: gitlab
- Disclosed At: 2020-09-14T23:28:30.952Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

### Summary

Since there is no rate limit in the inviting users to the repository section, it is possible to add all users on gitlab to a repository.

### Steps to reproduce

(Step-by-step guide to reproduce the issue, including:)

1. Create a repository
2. go to the project members section
3. choose a random user
4. before clicking the invite button, we need to capture the request with the burp suite..
5. ███████
6. Send it to the Intruder module, specify the █████ field here between 1 and 7006996 and send the request.

### Impact

It is possible to collect all users on Gitlab in a single repository, so users' mailboxes will be filled with notifications.


### Note

Because the rate limit is out of scope, I tested it and I could not stop the python script, and there were users affected.

## Impact

It is possible to collect all users on Gitlab in a single repository, so users' mailboxes will be filled with notifications.

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
