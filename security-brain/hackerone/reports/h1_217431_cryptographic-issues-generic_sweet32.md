---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '217431'
original_report_id: '217431'
title: sweet32
weakness: Cryptographic Issues - Generic
team_handle: udemy
created_at: '2017-03-31T12:18:22.679Z'
disclosed_at: '2017-05-04T13:32:29.537Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# sweet32

## Metadata

- HackerOne Report ID: 217431
- Weakness: Cryptographic Issues - Generic
- Program: udemy
- Disclosed At: 2017-05-04T13:32:29.537Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

hello
have found new attack against 3DES-CBC cipher in TLS,that they can decrypt customer data using a method called SWEET32 Birthday Attack.
This Vulnerability has got CVE-2016-2183 and has cvss score 5.0
in atach you will see a print screen vuln confirmation by nmap script 
Mitigation for SWEET32 attack
Prefer minimum 128-bit cipher suites
Limit the length of TLS sessions with a 64-bit cipher, which could be done with TLS renegotiation or closing and starting a new connection
 Disable cipher suites using 3DES

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
