---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '90643'
original_report_id: '90643'
title: No email verification during registration
weakness: Improper Authentication - Generic
team_handle: owncloud
created_at: '2015-09-27T08:58:39.807Z'
disclosed_at: '2015-09-28T15:49:01.694Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# No email verification during registration

## Metadata

- HackerOne Report ID: 90643
- Weakness: Improper Authentication - Generic
- Program: owncloud
- Disclosed At: 2015-09-28T15:49:01.694Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

When you register for a new account, there is no verification link sent to the email for confirmation. The account is directly activated and can be used without confirming the email.

This is vulnerable as anyone can use anyone's email without verification. and one with valid email owner cant signup with his own email as someone else already took it before him.

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
