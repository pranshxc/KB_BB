---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '238117'
original_report_id: '238117'
title: Open redirect while disconnecting Email
weakness: Open Redirect
team_handle: weblate
created_at: '2017-06-08T17:12:28.261Z'
disclosed_at: '2017-06-08T19:10:55.468Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- open-redirect
---

# Open redirect while disconnecting Email

## Metadata

- HackerOne Report ID: 238117
- Weakness: Open Redirect
- Program: weblate
- Disclosed At: 2017-06-08T19:10:55.468Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team, 
there is a open redirect end point when any account owner disconnect email accounts. He is redirected to some other domain.

Vulnerable URL

https://demo.weblate.org/accounts/disconnect/email/2354/?next=http://google.com
POC

Steps:
Go to authentication tab.
Disconnect Email account and capture the request.
Now, after next= write https://evil.com.
You are redirected to evil.com

Thanks,

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
