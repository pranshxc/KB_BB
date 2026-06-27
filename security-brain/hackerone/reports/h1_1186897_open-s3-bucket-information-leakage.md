---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1186897'
original_report_id: '1186897'
title: Open S3 Bucket | information leakage
team_handle: sifchain
created_at: '2021-05-06T16:58:21.810Z'
disclosed_at: '2021-05-15T19:58:36.066Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: https://github.com/sifchain/sifnode
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Open S3 Bucket | information leakage

## Metadata

- HackerOne Report ID: 1186897
- Weakness: 
- Program: sifchain
- Disclosed At: 2021-05-15T19:58:36.066Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi

I found  an Open S3 Bucket.

- POC :

 aws s3 ls s3://amazon-eks/

Source : `https://github.com/Sifchain/sifnode/blob/bebbe9883560bbde4f452f81a2d85bdbc243636a/deploy/rake/dependencies.rake#21`

regards
oos

## Impact

information leakage

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
