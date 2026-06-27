---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '243609'
original_report_id: '243609'
title: The username of an account can be ..
weakness: Business Logic Errors
team_handle: weblate
created_at: '2017-06-27T12:11:53.127Z'
disclosed_at: '2017-07-27T12:44:47.559Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- business-logic-errors
---

# The username of an account can be ..

## Metadata

- HackerOne Report ID: 243609
- Weakness: Business Logic Errors
- Program: weblate
- Disclosed At: 2017-07-27T12:44:47.559Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

## Description:

The username of an account can be set to `..`. This makes it impossible to view the public profile of this account.

## POC:

I have claimed the username `..` on the demo.weblate.org site. It is impossible to view this account's public profile page. 
Here is the public profile page: https://demo.weblate.org/user/../

## Mitigation

I recommend you filtering usernames to prevent them from starting with `.`.

Thanks!

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
