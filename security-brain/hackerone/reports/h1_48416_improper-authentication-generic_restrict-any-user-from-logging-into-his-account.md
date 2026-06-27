---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '48416'
original_report_id: '48416'
title: Restrict any user from logging into his account.
weakness: Improper Authentication - Generic
team_handle: security
created_at: '2015-02-20T22:39:05.924Z'
disclosed_at: '2015-03-24T00:56:05.924Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# Restrict any user from logging into his account.

## Metadata

- HackerOne Report ID: 48416
- Weakness: Improper Authentication - Generic
- Program: security
- Disclosed At: 2015-03-24T00:56:05.924Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hackerone's destroys user sessions automatically after signing out,changing password etc.So Old sessions are seems to be worthless for any attacker.But I found something,by exploiting this you can restrict any hackerone user to logging into his account.

**Pre-Requisition**
I just need one of his old sessions.

**steps to reproduce**
1. Login to hackerone.
2. Capture any request.
3. Send it to burp intruder.
4. Logout from hackerone.
5. Now start intruding that captured request,which is carrying the old destroyed session.
6. Try log in from other device.
7. Every time burp intruder sends a request,the present logged in account will be logged out automatically.
So if you keep continue intruding,that user will never be able to login to his own ID.

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
