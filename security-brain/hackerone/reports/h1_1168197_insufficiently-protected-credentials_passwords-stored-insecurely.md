---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1168197'
original_report_id: '1168197'
title: Passwords Stored Insecurely
weakness: Insufficiently Protected Credentials
team_handle: versa-networks
created_at: '2019-02-20T00:00:00.000Z'
disclosed_at: '2021-05-05T20:19:21.655Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- insufficiently-protected-credentials
---

# Passwords Stored Insecurely

## Metadata

- HackerOne Report ID: 1168197
- Weakness: Insufficiently Protected Credentials
- Program: versa-networks
- Disclosed At: 2021-05-05T20:19:21.655Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In Versa Director, Versa Analytics and VOS, Passwords are not hashed using an adaptive cryptographic hash function or key derivation function prior to storage. Popular hashing algorithms based on the Merkle-Damgardconstruction (such as MD5 and SHA-1) alone are insufficient in thwarting password cracking. Attackers can generate and use precomputed hashes for all possible password character combinations (commonly referred to as "rainbow tables") relatively quickly. The use of adaptive hashing algorithms such asscryptorbcryptor Key-Derivation Functions (i.e.PBKDF2) to hash passwords make generation of such rainbow tables computationally infeasible.

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
