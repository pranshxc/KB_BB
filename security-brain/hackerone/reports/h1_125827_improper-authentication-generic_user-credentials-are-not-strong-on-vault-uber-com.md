---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '125827'
original_report_id: '125827'
title: User credentials are not strong on vault.uber.com
weakness: Improper Authentication - Generic
team_handle: uber
created_at: '2016-04-07T06:41:20.923Z'
disclosed_at: '2016-07-26T00:30:23.469Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# User credentials are not strong on vault.uber.com

## Metadata

- HackerOne Report ID: 125827
- Weakness: Improper Authentication - Generic
- Program: uber
- Disclosed At: 2016-07-26T00:30:23.469Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

I was just trying to login vault.uber.com

I entered email **xx** and password **xx**,  I got loggedin to someones account.
I entered email **zz** and password **zz**,  I got loggedin to someones account.

It means passowrd complexity and length of username/email is not enforced. This allowed my to access the someones account. Since it contains payment related information, password complexity and email should be there.

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
