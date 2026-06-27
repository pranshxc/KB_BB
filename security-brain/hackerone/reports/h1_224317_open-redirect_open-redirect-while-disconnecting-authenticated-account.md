---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '224317'
original_report_id: '224317'
title: Open redirect while disconnecting authenticated account
weakness: Open Redirect
team_handle: weblate
created_at: '2017-04-27T12:45:43.745Z'
disclosed_at: '2017-06-08T16:43:46.455Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- open-redirect
---

# Open redirect while disconnecting authenticated account

## Metadata

- HackerOne Report ID: 224317
- Weakness: Open Redirect
- Program: weblate
- Disclosed At: 2017-06-08T16:43:46.455Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team, 
there is a open redirect end point when any account owner disconnect authenticated accounts say
google. He is redirected to some other domain.

Vulnerable URL
---
[demo.weblate.org/accounts/disconnect/google-oauth2/2335/?next=](demo.weblate.org/accounts/disconnect/google-oauth2/2335/?next=)

POC 
1. Go to authentication tab.
2. Disconnect Google account and capture the request.
3. Now, after next= write https://evil.com.
4. You are redirected to evil.com

video POC is attached.

Best Regards
Gurwinder

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
