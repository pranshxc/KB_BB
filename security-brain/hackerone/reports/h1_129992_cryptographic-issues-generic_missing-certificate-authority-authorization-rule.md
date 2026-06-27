---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '129992'
original_report_id: '129992'
title: Missing Certificate Authority Authorization rule
weakness: Cryptographic Issues - Generic
team_handle: security
created_at: '2016-04-12T08:02:44.567Z'
disclosed_at: '2017-08-17T02:55:24.775Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cryptographic-issues-generic
---

# Missing Certificate Authority Authorization rule

## Metadata

- HackerOne Report ID: 129992
- Weakness: Cryptographic Issues - Generic
- Program: security
- Disclosed At: 2017-08-17T02:55:24.775Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Certificate Authority Authorization (supported by LetsEncrypt and other CAs) allows a domain owner to specify which Certificate Authorities should be allowed to issue certificates for the domain. All CAA-compliant certificate authorities should refuse to issue a certificate unless they are the CA of record for the target site. This helps reduce the threat of a bad guy tricking a Certificate Authority into issuing a phony certificate for your site.

The CAA rule is stored as a DNS resource record of type 257. You can view a domain’s CAA rule using a DNS lookup service:

https://dns.google.com/query?name=hackerone.com&type=257&dnssec=true

Hackerone should set a CAA record to help prevent misissuance of a certificate for its domains.

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
