---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '107296'
original_report_id: '107296'
title: Possible Timing Side-Channel in XMLRPC Verification
weakness: Cryptographic Issues - Generic
team_handle: automattic
created_at: '2015-12-29T06:40:36.202Z'
disclosed_at: '2016-03-17T14:13:54.586Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cryptographic-issues-generic
---

# Possible Timing Side-Channel in XMLRPC Verification

## Metadata

- HackerOne Report ID: 107296
- Weakness: Cryptographic Issues - Generic
- Program: automattic
- Disclosed At: 2016-03-17T14:13:54.586Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

https://github.com/Automattic/jetpack/blob/bc7a4541ef6f0e9f583376d801ab0c40cfb976c3/class.jetpack-xmlrpc-server.php#L115

I mentioned this to @daljo628 and he suggested submitting it here instead.

This looks very much like a classic [timing attack vulnerability](http://blog.ircmaxell.com/2014/11/its-all-about-time.html). The fix would be to use `hash_equals()` (which I have provided a sane polyfill for in [sarciszewski/php-future](https://github.com/sarciszewski/php-future) if you don't already have one handy).

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
