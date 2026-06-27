---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1067547'
original_report_id: '1067547'
title: Unauthenticated access to webmail at maildev.happytools.dev leading to compromised
  wordpress site api.happytools.dev [RCE]
weakness: Information Disclosure
team_handle: automattic
created_at: '2020-12-28T17:39:22.639Z'
disclosed_at: '2021-02-01T15:37:32.327Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 71
tags:
- hackerone
- information-disclosure
---

# Unauthenticated access to webmail at maildev.happytools.dev leading to compromised wordpress site api.happytools.dev [RCE]

## Metadata

- HackerOne Report ID: 1067547
- Weakness: Information Disclosure
- Program: automattic
- Disclosed At: 2021-02-01T15:37:32.327Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Dear Team,

Today when I trying to find bugs on happy tools I have found 2 domains below for staging environment
- https://maildev.happytools.dev
- https:// api.happytools.dev

Two websites above ssl certificate was expired. But you can adjust your date-time to 02/02/2020 or before that time to access those sites normally

## Platform(s) Affected:
https:// api.happytools.dev

## Steps To Reproduce:

  1. https://api.happytools.dev/wp-login.php?action=lostpassword and forgot password for user `api`
  1. Go to https://maildev.happytools.dev to get reset password link and set new password for user `api` (I did not try to do that)
  1. After changing password for user `api`, we can control wordpress cms and may upload plugins/themes contain backdoor or harmful scripts to this server

## Supporting Material/References:
Some screen shots PoC

{F1132811}

{F1132810}

████████

## Impact

Takeover wordpress site api.happytools.dev

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
