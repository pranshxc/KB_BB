---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1139520'
original_report_id: '1139520'
title: Bypassing the External Link Warning
weakness: Open Redirect
team_handle: security
created_at: '2021-03-29T05:09:25.088Z'
disclosed_at: '2021-05-07T20:14:45.871Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Bypassing the External Link Warning

## Metadata

- HackerOne Report ID: 1139520
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2021-05-07T20:14:45.871Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

As the HackerOne team is aware, the URL `https://hackerone.com/users/saml/sign_in?email=test@hackerone.com` can redirect users to external pages. Because of this, there is a protection in the links created by Markdown to show the user a warning when clicking in any link started with `https://hackerone.com/users/saml/sign_in` or pointing to third-party domains.

But this protection can be bypassed.

## Steps To Reproduce:

Give a look at the report below:

[https://hackerone.com/reports/9128701](https://hackerone.com/users/%2E/saml/sign_in?email=test██████&remember_me=false)

As you saw, the above link doesn't open a real report but redirects the user to an external page, without any warning.

Malicious Markdown:

`[https://hackerone.com/reports/9128701](https://hackerone.com/users/%2E/saml/sign_in?email=test██████████&remember_me=false)`

## Recommendation:

Show an external link warning for any link to `https://hackerone.com/users/saml/sign_in*`.
Attackers can try to bypass the protection by using `/.` and/or `/..`, like in the above case.

## Impact

This bug can be used in social engineering attacks to try to steal credentials from HackerOne users.

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
