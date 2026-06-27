---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '192284'
original_report_id: '192284'
title: olx.ph is vulnerable to POODLE attack
weakness: Cryptographic Issues - Generic
team_handle: olx
created_at: '2016-12-18T22:46:48.046Z'
disclosed_at: '2017-04-07T07:56:59.455Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# olx.ph is vulnerable to POODLE attack

## Metadata

- HackerOne Report ID: 192284
- Weakness: Cryptographic Issues - Generic
- Program: olx
- Disclosed At: 2017-04-07T07:56:59.455Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

https://www.olx.ph supports SSLv3 and hence is vulnerable to POODLE attack, which is a kind of Man in the middle attack.

This vulnerability was discovered in 2014 by Google(More Information below):
https://security.googleblog.com/2014/10/this-poodle-bites-exploiting-ssl-30.html
http://chrisburgess.com.au/how-to-test-for-the-sslv3-poodle-vulnerability/

Disabling SSL 3.0 support, or CBC-mode ciphers with SSL 3.0, is sufficient to mitigate this issue.

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
