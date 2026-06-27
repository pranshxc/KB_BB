---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '115422'
original_report_id: '115422'
title: Full Path Disclosure in password lock
weakness: Information Disclosure
team_handle: paragonie
created_at: '2016-02-08T19:09:50.672Z'
disclosed_at: '2017-10-16T05:51:57.429Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- information-disclosure
---

# Full Path Disclosure in password lock

## Metadata

- HackerOne Report ID: 115422
- Weakness: Information Disclosure
- Program: paragonie
- Disclosed At: 2017-10-16T05:51:57.429Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi,

Password input must be string but not checked in PasswordLock lib,
It will throw an exception on `hash` function call

    Warning: hash() expects parameter 2 to be string

So you must validate it in `hashAndEncrypt` and `decryptAndVerify`

Regards

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
