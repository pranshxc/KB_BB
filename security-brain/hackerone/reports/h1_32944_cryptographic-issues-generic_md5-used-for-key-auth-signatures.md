---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '32944'
original_report_id: '32944'
title: MD5 used for Key-Auth signatures
weakness: Cryptographic Issues - Generic
team_handle: wp-api
created_at: '2014-10-27T15:37:26.557Z'
disclosed_at: '2014-10-29T20:38:07.150Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- cryptographic-issues-generic
---

# MD5 used for Key-Auth signatures

## Metadata

- HackerOne Report ID: 32944
- Weakness: Cryptographic Issues - Generic
- Program: wp-api
- Disclosed At: 2014-10-29T20:38:07.150Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

https://github.com/WP-API/Key-Auth/blob/f9b74b3e4df667cfb44baba556eafde65fa3aec9/key-auth.php#L65

MD5 is vulnerable to length-extension attacks.

Maybe consider changing this to `hash_hmac('sha256', json_encode($args), $secret)`?

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
