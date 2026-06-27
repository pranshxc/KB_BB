---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1369312'
original_report_id: '1369312'
title: SSRF mitigation bypass using DNS Rebind attack
weakness: Server-Side Request Forgery (SSRF)
team_handle: concretecms
created_at: '2021-10-13T13:27:58.015Z'
disclosed_at: '2022-11-25T18:11:12.845Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: https://github.com/concrete5/concrete5
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF mitigation bypass using DNS Rebind attack

## Metadata

- HackerOne Report ID: 1369312
- Weakness: Server-Side Request Forgery (SSRF)
- Program: concretecms
- Disclosed At: 2022-11-25T18:11:12.845Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

We noticed that the upload functionality contains the ability to upload files from remote server, however there are some mitigations against accessing the AWS Instance Metadata service.

We've managed to bypass these mitigations using DNS rebinding and we've managed to fetch the AWS IAM keys when Concrete CMS is running in the cloud.

We've used http://1u.ms/ service for DNS rebinding, please see screenshots with evidence.

## Impact

An attacker can bypass the SSRF protections and he can fetch the AWS IAM keys under which the application is running. From here on he can do enumeration and mount other attacks.

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
