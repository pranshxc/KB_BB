---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '23363'
original_report_id: '23363'
title: Forgot Password Issue
weakness: Improper Authentication - Generic
team_handle: phabricator
created_at: '2014-08-09T20:02:01.015Z'
disclosed_at: '2014-09-10T19:16:02.866Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-authentication-generic
---

# Forgot Password Issue

## Metadata

- HackerOne Report ID: 23363
- Weakness: Improper Authentication - Generic
- Program: phabricator
- Disclosed At: 2014-09-10T19:16:02.866Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The application authenticates user before the password is changed by the user.

POC:
1. User attempts password reset
2. User gets verification link
3. User access link and gets authenticated automatically before performing any password change

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
