---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '31168'
original_report_id: '31168'
title: Cryptographic Side Channel in OAuth Library
weakness: Cryptographic Issues - Generic
team_handle: wp-api
created_at: '2014-10-12T18:27:30.330Z'
disclosed_at: '2014-10-29T19:57:02.804Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# Cryptographic Side Channel in OAuth Library

## Metadata

- HackerOne Report ID: 31168
- Weakness: Cryptographic Issues - Generic
- Program: wp-api
- Disclosed At: 2014-10-29T19:57:02.804Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Because hashes and tokens are compared with the `!==` and `===` operators, these checks may be susceptible to timing attacks. More info: http://codahale.com/a-lesson-in-timing-attacks/

Affected code:

https://github.com/WP-API/OAuth1/blob/45197eca2925f5022192903d3639decd0ae1811c/lib/class-wp-json-authentication-oauth1.php#L562
https://github.com/WP-API/OAuth1/blob/45197eca2925f5022192903d3639decd0ae1811c/lib/class-wp-json-authentication-oauth1.php#L290

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
