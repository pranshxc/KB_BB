---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '241598'
original_report_id: '241598'
title: Full Name Overwrite on Third party login
team_handle: weblate
created_at: '2017-06-20T07:21:00.626Z'
disclosed_at: '2017-08-21T17:47:12.291Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# Full Name Overwrite on Third party login

## Metadata

- HackerOne Report ID: 241598
- Weakness: 
- Program: weblate
- Disclosed At: 2017-08-21T17:47:12.291Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description
After one might have logged in on a browser using the *Third party login* (Google) and have made changes to the account like the `Full name`. Making a *third party login* on another browser using the same email overwrites the `Full name` to the name on the email.

One would know he is logged in the same account because the username remains the same.

#####NOTE: This happens when you logout and make a `third party login` again. The `Full name` changes.

Shuaib.

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
