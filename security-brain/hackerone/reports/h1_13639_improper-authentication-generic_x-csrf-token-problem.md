---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13639'
original_report_id: '13639'
title: X/Csrf token problem
weakness: Improper Authentication - Generic
team_handle: factlink
created_at: '2014-05-27T14:18:28.100Z'
disclosed_at: '2014-05-30T13:22:08.861Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# X/Csrf token problem

## Metadata

- HackerOne Report ID: 13639
- Weakness: Improper Authentication - Generic
- Program: factlink
- Disclosed At: 2014-05-30T13:22:08.861Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found that you are using X/Csrf token as a protection against CSRF attacks.

But you are using same X/Csrf token in and out.

eg
z3qrwilV8lz7CXsMhmvqxn+93GDZm/m9w/d5DZjoj8w=

This token is same before and after log-in.
This must be patch as it me result session hacks.

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
