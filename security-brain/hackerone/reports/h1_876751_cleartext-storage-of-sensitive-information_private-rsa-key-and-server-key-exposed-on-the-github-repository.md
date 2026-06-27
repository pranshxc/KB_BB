---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '876751'
original_report_id: '876751'
title: Private RSA key and Server key exposed on the GitHub repository
weakness: Cleartext Storage of Sensitive Information
team_handle: kubernetes
created_at: '2020-05-17T23:02:39.364Z'
disclosed_at: '2020-10-22T18:07:16.840Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: https://github.com/kubernetes/kubernetes
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Private RSA key and Server key exposed on the GitHub repository

## Metadata

- HackerOne Report ID: 876751
- Weakness: Cleartext Storage of Sensitive Information
- Program: kubernetes
- Disclosed At: 2020-10-22T18:07:16.840Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Report Submission Form

## Summary:
I was searching for sensitive data in Kubernetes repository where I found these private keys. These are private RSA key and private server key, which could be used for unauthorized access.

## Steps To Reproduce:

VISIT THESE LINKS

Repository : kubernetes / kubernetes

https://github.com/kubernetes/kubernetes/blob/ce3ddcd5f691b5777e7b2f4d89cac1da316970b4/staging/src/k8s.io/legacy-cloud-providers/vsphere/vclib/fixtures/ca.key

https://github.com/kubernetes/kubernetes/blob/ce3ddcd5f691b5777e7b2f4d89cac1da316970b4/staging/src/k8s.io/legacy-cloud-providers/vsphere/vclib/fixtures/server.key

## Supporting Material/References:
https://hackerone.com/reports/50170
https://hackerone.com/reports/638401

## Impact

1).Private key leakage
2). All of the servers using this key will be compromised

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
