---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '210384'
original_report_id: '210384'
title: Open Redirect
weakness: Open Redirect
team_handle: mailru
created_at: '2017-03-03T14:08:15.791Z'
disclosed_at: '2017-03-17T13:08:00.879Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- open-redirect
---

# Open Redirect

## Metadata

- HackerOne Report ID: 210384
- Weakness: Open Redirect
- Program: mailru
- Disclosed At: 2017-03-17T13:08:00.879Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey
I would like to report an open redirect issue it.mail.ru

Proof of Concept:

1. go to Register page https://it.mail.ru/en/users/register/?next=////www.evil.com/%2e%2e and Register a account
2.  now open your mail and click the  activation link

This will redirect you to evil.com after click the activation link

Please let me know if you need more information.

Hope You'll fix this one..

Thanks

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
