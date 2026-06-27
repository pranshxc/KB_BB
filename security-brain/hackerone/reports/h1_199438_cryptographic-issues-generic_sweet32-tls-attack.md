---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '199438'
original_report_id: '199438'
title: SWEET32 TLS attack
weakness: Cryptographic Issues - Generic
team_handle: legalrobot
created_at: '2017-01-18T18:03:52.961Z'
disclosed_at: '2017-02-01T18:37:05.005Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- cryptographic-issues-generic
---

# SWEET32 TLS attack

## Metadata

- HackerOne Report ID: 199438
- Weakness: Cryptographic Issues - Generic
- Program: legalrobot
- Disclosed At: 2017-02-01T18:37:05.005Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Researchers have found new attack against 3DES-CBC cipher in TLS,that they can decrypt customer data using a method called SWEET32 Birthday Attack.

This Vulnerability has got CVE-2016-2183 and has cvss score 5.0

This vulnerability can be found manually by simply using nmap script

nmap -Pn -p --script ssl-enum-ciphers ip

Mitigation for SWEET32 attack

->Prefer minimum 128-bit cipher suites

->Limit the length of TLS sessions with a 64-bit cipher, which could be done with TLS renegotiation or closing and starting a new connection

-> Disable cipher suites using 3DES

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
