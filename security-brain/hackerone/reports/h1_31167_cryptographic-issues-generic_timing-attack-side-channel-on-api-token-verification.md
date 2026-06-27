---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '31167'
original_report_id: '31167'
title: Timing Attack Side-Channel on API Token Verification
weakness: Cryptographic Issues - Generic
team_handle: joola-io
created_at: '2014-10-12T18:17:52.168Z'
disclosed_at: '2014-10-25T18:11:13.588Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cryptographic-issues-generic
---

# Timing Attack Side-Channel on API Token Verification

## Metadata

- HackerOne Report ID: 31167
- Weakness: Cryptographic Issues - Generic
- Program: joola-io
- Disclosed At: 2014-10-25T18:11:13.588Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://github.com/joola/joola/blob/develop/lib/dispatch/users.js#L514

Because tokens are compared with the `===` operator, this may be susceptible to timing attacks. More info: http://codahale.com/a-lesson-in-timing-attacks/

This is probably not the lowest hanging fruit for an attacker, but it's something you might want to fix. :)

Replacement utility: https://github.com/cryptocat/cryptocat/blob/32fd02f8d899e219a004281eb0ce364cb52dd62a/src/core/js/lib/otr.js#L145-L152

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
