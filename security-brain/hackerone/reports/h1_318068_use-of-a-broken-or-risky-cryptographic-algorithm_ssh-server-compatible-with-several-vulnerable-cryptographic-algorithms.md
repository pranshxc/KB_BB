---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '318068'
original_report_id: '318068'
title: SSH server compatible with several vulnerable cryptographic algorithms
weakness: Use of a Broken or Risky Cryptographic Algorithm
team_handle: gsa_bbp
created_at: '2018-02-21T02:23:21.045Z'
disclosed_at: '2018-03-02T20:44:31.260Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: ssh.fr.cloud.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- use-of-a-broken-or-risky-cryptographic-algorithm
---

# SSH server compatible with several vulnerable cryptographic algorithms

## Metadata

- HackerOne Report ID: 318068
- Weakness: Use of a Broken or Risky Cryptographic Algorithm
- Program: gsa_bbp
- Disclosed At: 2018-03-02T20:44:31.260Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

An ssh-audit scan found that ssh.fr.cloud.gov supports sha1 for various purposes(including exclusively for MAC addresses), as well as arcfour. Both of these are outdated and known vulnerable.

The algorithms used are also indicative of an outdated SSH version (OpenSSH 6 or Dropbear 2013). It's probably a good idea to upgrade.

The output of ssh-audit is attached.

## Impact

A man-in-the-middle attack may expose data encrypted with arcfour and/or hashed with sha1, which can then be decrypted to find things like passwords or payloads sent over SSH.

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
