---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1166535'
original_report_id: '1166535'
title: Brew bootstrap process is insecure
weakness: Code Injection
team_handle: homebrew
created_at: '2021-04-16T15:03:16.510Z'
disclosed_at: '2021-04-30T12:15:42.999Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 8
tags:
- hackerone
- code-injection
---

# Brew bootstrap process is insecure

## Metadata

- HackerOne Report ID: 1166535
- Weakness: Code Injection
- Program: homebrew
- Disclosed At: 2021-04-30T12:15:42.999Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The process described in this page is not secure - no checksum / PGP signature is published and there is no way to check the download is
legit:
https://brew.sh/

"/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)""

This can lead to supply chain attacks such as the one that just happened here:
https://about.codecov.io/security-update/

This can lead to two possible attacks:
1. Supply chain attacks if the script is modified on the server.
2. Injection attacks if the TLS connections are compromised.

## Impact

For brew, a checksum and a way to check it should be provided, and security information should be added to the webpage referenced above. This way users can check the downloads.

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
