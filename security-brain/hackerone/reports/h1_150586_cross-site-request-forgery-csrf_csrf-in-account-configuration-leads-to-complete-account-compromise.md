---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '150586'
original_report_id: '150586'
title: CSRF in account configuration leads to complete account compromise
weakness: Cross-Site Request Forgery (CSRF)
team_handle: olx
created_at: '2016-07-11T12:50:34.703Z'
disclosed_at: '2016-10-05T14:08:02.297Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in account configuration leads to complete account compromise

## Metadata

- HackerOne Report ID: 150586
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: olx
- Disclosed At: 2016-10-05T14:08:02.297Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Although listed as out of scope, this vulnerability presents serious risk that can compromise any account, and hope you consider it as such.

When updating a user in the configuration tab, there is no CSRF token to prevent other pages from updating the user. This allows any third party site to edit the user's email, then able to reset the password.

POC:

1. Visit http://d214mfsab.org/olx.html while logged into your OLX account. This is a demo CSRF page I set up that changes your email to 'example@example.com'.
2. Click 'Submit'.
3. The JSON response will be returned, showing that your email was changed. An attacker could then reset your password using the 'Forgot Password' feature and gain access to your account.

Suggested fix:

Require a CSRF token with all sensitive GET and POST requests.

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
