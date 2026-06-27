---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15578'
original_report_id: '15578'
title: Same user name and uuid for multiple user names
weakness: Violation of Secure Design Principles
team_handle: fanfootage
created_at: '2014-06-08T04:08:13.666Z'
disclosed_at: '2014-07-13T00:02:31.732Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Same user name and uuid for multiple user names

## Metadata

- HackerOne Report ID: 15578
- Weakness: Violation of Secure Design Principles
- Program: fanfootage
- Disclosed At: 2014-07-13T00:02:31.732Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Two things I observe
1. same user name can be used by number of users. This may create confusion to another user
2. The uuid parameter using which a user's profile is accessed is also controllable during signup. I can change that value during signup to a value already assigned to user. When I like any video or post any comment. The hyperlink to my userid will be the same as that of an existing user whose uuid value I have used. Depending upon how the values are fetched from database, The link to his user id may lead to my profile page or link to my userid lead to his profile page.
Screenshots attached.

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
