---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1183809'
original_report_id: '1183809'
title: Possible Database Details stored in values.yaml
weakness: Cleartext Storage of Sensitive Information
team_handle: sifchain
created_at: '2021-05-17T16:38:48.366Z'
disclosed_at: '2021-12-09T17:47:01.628Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 2
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Possible Database Details stored in values.yaml

## Metadata

- HackerOne Report ID: 1183809
- Weakness: Cleartext Storage of Sensitive Information
- Program: sifchain
- Disclosed At: 2021-12-09T17:47:01.628Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

The database details like username and database name are disclosed in the below mentioned file. Assuming a blank password since the password field was empty.

File Location : https://github.com/Sifchain/sifnode/blob/740331dad061ee0f5a3cf3798d429f294b70f0ae/deploy/helm/block-explorer/values.yaml 

I have attached screenshot in this report.

## Impact

An attacker can use this vulnerability to access the database once he is on the internal system.

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
