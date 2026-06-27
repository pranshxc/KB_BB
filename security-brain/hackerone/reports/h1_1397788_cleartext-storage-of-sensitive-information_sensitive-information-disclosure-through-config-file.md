---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1397788'
original_report_id: '1397788'
title: Sensitive Information Disclosure Through Config File
weakness: Cleartext Storage of Sensitive Information
team_handle: mtn_group
created_at: '2021-11-10T19:03:13.577Z'
disclosed_at: '2022-09-01T20:50:48.872Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: mtncameroon.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Sensitive Information Disclosure Through Config File

## Metadata

- HackerOne Report ID: 1397788
- Weakness: Cleartext Storage of Sensitive Information
- Program: mtn_group
- Disclosed At: 2022-09-01T20:50:48.872Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
An attacker could gain access to sensitive information about usernames, encrypted passwords, internal IP addresses and configuration data of internal services.

## Steps To Reproduce:
- Go to https://zik.mtncameroon.net/common/queryconfig.action

## Remediation
Configure the application to not reveal sensitive information to client.

## References
https://cwe.mitre.org/data/definitions/200.html

## Impact

A malicious user is able to gain sensitive information usernames, encrypted passwords, internal IP addresses and configuration data of internal services.

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
