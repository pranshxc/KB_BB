---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '31166'
original_report_id: '31166'
title: Weak Random Number Generator for Auth Tokens
weakness: Cryptographic Issues - Generic
team_handle: joola-io
created_at: '2014-10-12T18:11:32.566Z'
disclosed_at: '2014-10-25T18:11:24.113Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# Weak Random Number Generator for Auth Tokens

## Metadata

- HackerOne Report ID: 31166
- Weakness: Cryptographic Issues - Generic
- Program: joola-io
- Disclosed At: 2014-10-25T18:11:24.113Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

https://github.com/joola/joola/blob/a534c3dca1a0deaec99c192978e61a35dd3a9069/lib/common/index.js#L90-L98

`Math.random()` is not sufficient for cryptographic purposes (such as authentication tokens).

An example replacement that uses `window.crypto.getRandomValues()` is available here:

https://github.com/resonantcore/lib/blob/9362480647b304aee6819ea94a18409241e79378/js/diceware/diceware.js#L60-L94

Further information:
https://media.blackhat.com/us-13/US-13-Soeder-Black-Box-Assessment-of-Pseudorandom-Algorithms-WP.pdf

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
