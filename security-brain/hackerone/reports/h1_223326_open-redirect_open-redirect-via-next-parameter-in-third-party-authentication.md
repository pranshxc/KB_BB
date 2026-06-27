---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223326'
original_report_id: '223326'
title: Open Redirect via "next" parameter in third-party authentication
weakness: Open Redirect
team_handle: weblate
created_at: '2017-04-24T09:02:48.477Z'
disclosed_at: '2017-05-17T14:17:51.878Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- open-redirect
---

# Open Redirect via "next" parameter in third-party authentication

## Metadata

- HackerOne Report ID: 223326
- Weakness: Open Redirect
- Program: weblate
- Disclosed At: 2017-05-17T14:17:51.878Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

It is currently possible to execute an open redirection attack via the `next` parameter with the inclusion of a triple-slash prefix.

## Proof of Concept
### Redirect URL
```
https://demo.weblate.org/accounts/login/github/?next=///google.com
```

After authenticating, the user will be immediately redirected to the attacker-specified target.  I believe this affects all third-party authentication providers on the Weblate platform.

Please let me know if you require any additional details regarding this vulnerability.

Thanks!

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
