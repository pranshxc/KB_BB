---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1186740'
original_report_id: '1186740'
title: Misconfiguration Certificate Authority Authorization Rule
weakness: Misconfiguration
team_handle: sifchain
created_at: '2021-05-06T16:08:09.566Z'
disclosed_at: '2021-12-09T19:49:18.159Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- misconfiguration
---

# Misconfiguration Certificate Authority Authorization Rule

## Metadata

- HackerOne Report ID: 1186740
- Weakness: Misconfiguration
- Program: sifchain
- Disclosed At: 2021-12-09T19:49:18.159Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello,Sifchain Security Team,
I found a bug called Missing CAA. Certificate Authority Authorization (supported by LetsEncrypt and other CAs) allows a domain owner to specify which Certificate Authorities should be allowed to issue certificates for the domain. All CAA-compliant certificate authorities should refuse to issue a certificate unless they are the CA of record for the target site. This helps reduce the threat of a bad guy tricking a Certificate Authority into issuing a phony certificate for your site. The CAA rule is stored as a DNS resource record of type 257. You can view a domain’s CAA rule using a DNS lookup service:
https://caatest.co.uk/sifchain.finance
Sifchain should set a CAA record to help prevent misissuance of a certificate for its domains.

## Impact

Impact:-
Domain Authority Can Be Takeover. If you need further information let me know

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
