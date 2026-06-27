---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1971589'
original_report_id: '1971589'
title: CSRF with logout action
weakness: Cross-Site Request Forgery (CSRF)
team_handle: weblate
created_at: '2023-05-03T20:27:08.462Z'
disclosed_at: '2023-06-16T07:59:20.707Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 26
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF with logout action

## Metadata

- HackerOne Report ID: 1971589
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: weblate
- Disclosed At: 2023-06-16T07:59:20.707Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, I wanted let you know and saw that previously similar issue was fixed.
Repro steps: Go to https://weblate.org/pl/ and click top right icon for logging in (user-tab user-anonymous, https://weblate.org/saml2/login/?next=/pl/).
Log in using username and password (https://hosted.weblate.org/accounts/login/?next=/idp/login/process/). 
Logged in on site https://weblate.org/pl/ use link: https://weblate.org/logout/
See logged out.

The similar result with using external page with prepared CSRF payload like:
`<a href="https://weblate.org/logout/"> Click me to see bonus pack`
Here as logged in user use this link from external page, next go to tab where logged in and refresh the page - see logged out there too.

Best regards,

## Impact

Bad actor can affect the user's login status - logged out.

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
