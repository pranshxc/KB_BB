---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '288'
original_report_id: '288'
title: Session Management
team_handle: security
created_at: '2013-11-07T17:19:36.545Z'
disclosed_at: '2014-04-19T20:59:20.960Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
---

# Session Management

## Metadata

- HackerOne Report ID: 288
- Weakness: 
- Program: security
- Disclosed At: 2014-04-19T20:59:20.960Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hackerone fails to expire the session cookie from the server side even when the user logs off upon clicking "Sign-Out" from the application. The cookie is cleared from the client side (browser), but is not cleared from the server side. If reused, it provides access to the user's account.
                Upon logging in again, a new session cookie is created, but the old session cookies still stay active on the server side. Therefore, any session cookie can be reused to gain access to the user's account.

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
