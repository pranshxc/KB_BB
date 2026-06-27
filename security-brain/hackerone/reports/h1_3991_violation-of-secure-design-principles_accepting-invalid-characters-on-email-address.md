---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '3991'
original_report_id: '3991'
title: Accepting Invalid characters on email address
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-03-14T11:56:30.458Z'
disclosed_at: '2016-04-25T04:40:07.279Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Accepting Invalid characters on email address

## Metadata

- HackerOne Report ID: 3991
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-04-25T04:40:07.279Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I tried to change my email address on hackerone.com.And when I tried adding null Bytes,it was being accepted by hackerone.com.
I am registered wth ███ and I tried to change my email address to ████%00 
And guess what,this address was granted as an email address.

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
