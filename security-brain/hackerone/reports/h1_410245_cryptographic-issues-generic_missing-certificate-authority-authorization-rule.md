---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '410245'
original_report_id: '410245'
title: Missing Certificate Authority Authorization rule
weakness: Cryptographic Issues - Generic
team_handle: security
created_at: '2018-09-16T06:34:51.908Z'
disclosed_at: '2019-04-11T18:29:36.372Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: https://ctf.hacker101.com
asset_type: URL
max_severity: low
tags:
- hackerone
- cryptographic-issues-generic
---

# Missing Certificate Authority Authorization rule

## Metadata

- HackerOne Report ID: 410245
- Weakness: Cryptographic Issues - Generic
- Program: security
- Disclosed At: 2019-04-11T18:29:36.372Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Certificate Authority Authorization (supported by LetsEncrypt and other CAs) allows a domain owner to specify which Certificate Authorities should be allowed to issue certificates for the domain. All CAA-compliant certificate authorities should refuse to issue a certificate unless they are the CA of record for the target site. This helps reduce the threat of a bad guy tricking a Certificate Authority into issuing a phony certificate for your site.

The CAA rule is stored as a DNS resource record of type 257. You can view a domain’s CAA rule using a DNS lookup service:

https://dns.google.com/query?name=hacker101.com&type=257&dnssec=true

https://dns.google.com/query?name=ctf.hacker101.com&type=257&dnssec=true

hacker101 should set a CAA record to help prevent misissuance of a certificate for its domains.

Reference Report :  https://hackerone.com/reports/129992

## Impact

Misissuance of a certificate

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
