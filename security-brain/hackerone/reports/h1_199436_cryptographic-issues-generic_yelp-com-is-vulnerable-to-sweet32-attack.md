---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '199436'
original_report_id: '199436'
title: Yelp.com is vulnerable to SWEET32 attack
weakness: Cryptographic Issues - Generic
team_handle: yelp
created_at: '2017-01-18T17:43:32.478Z'
disclosed_at: '2017-11-09T21:47:52.672Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cryptographic-issues-generic
---

# Yelp.com is vulnerable to SWEET32 attack

## Metadata

- HackerOne Report ID: 199436
- Weakness: Cryptographic Issues - Generic
- Program: yelp
- Disclosed At: 2017-11-09T21:47:52.672Z
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
Reference link: https://sweet32.info/

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
