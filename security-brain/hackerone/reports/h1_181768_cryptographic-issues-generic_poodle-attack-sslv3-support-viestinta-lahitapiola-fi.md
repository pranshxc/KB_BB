---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181768'
original_report_id: '181768'
title: Poodle attack SSLv3 Support (viestinta.lahitapiola.fi)
weakness: Cryptographic Issues - Generic
team_handle: localtapiola
created_at: '2016-11-12T15:24:01.414Z'
disclosed_at: '2016-12-15T08:34:55.516Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cryptographic-issues-generic
---

# Poodle attack SSLv3 Support (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 181768
- Weakness: Cryptographic Issues - Generic
- Program: localtapiola
- Disclosed At: 2016-12-15T08:34:55.516Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Websites that support SSLv3 and CBC-mode ciphers are potentially vulnerable to an active MITM (Man-in-the-middle) attack. This attack, called POODLE, is similar to the BEAST attack and also allows a network attacker to extract the plaintext of targeted parts of an SSL connection, usually cookie data. Unlike the BEAST attack, it doesn't require such extensive control of the format of the plaintext and thus is more practical. 
Any website that supports SSLv3 is vulnerable to POODLE, even if it also supports more recent versions of TLS. SSLv3 is disabled by default in Firefox 34, which was released on Nov 25 2014.
An attacker may be able to exploit this problem to conduct man-in-the-middle attacks and decrypt communications between the affected service and clients

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
