---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260928'
original_report_id: '260928'
title: Missing Certificate Authority Authorization rule
weakness: Cryptographic Issues - Generic
team_handle: gratipay
created_at: '2017-08-20T11:06:01.195Z'
disclosed_at: '2017-09-09T17:23:46.490Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 2
asset_identifier: https://gratipay.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cryptographic-issues-generic
---

# Missing Certificate Authority Authorization rule

## Metadata

- HackerOne Report ID: 260928
- Weakness: Cryptographic Issues - Generic
- Program: gratipay
- Disclosed At: 2017-09-09T17:23:46.490Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Certificate Authority Authorization (supported by LetsEncrypt and other CAs) allows a domain owner to specify which Certificate Authorities should be allowed to issue certificates for the domain. All CAA-compliant certificate authorities should refuse to issue a certificate unless they are the CA of record for the target site. This helps reduce the threat of a bad guy tricking a Certificate Authority into issuing a phony certificate for your site.

The CAA rule is stored as a DNS resource record of type 257. You can view a domain’s CAA rule using a DNS lookup service:

https://dns.google.com/query?name=gratipay.com&type=257&dnssec=true

Gratipay should set a CAA record to help prevent misissuance of a certificate for its domains.

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
