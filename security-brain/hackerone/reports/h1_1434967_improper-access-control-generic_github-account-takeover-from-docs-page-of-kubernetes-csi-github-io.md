---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1434967'
original_report_id: '1434967'
title: Github Account Takeover from Docs page of `kubernetes-csi.github.io`
weakness: Improper Access Control - Generic
team_handle: kubernetes
created_at: '2021-12-23T13:52:04.068Z'
disclosed_at: '2022-06-04T17:58:23.464Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: kubernetes-csi.github.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Github Account Takeover from Docs page of `kubernetes-csi.github.io`

## Metadata

- HackerOne Report ID: 1434967
- Weakness: Improper Access Control - Generic
- Program: kubernetes
- Disclosed At: 2022-06-04T17:58:23.464Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Report Submission Form

## Summary:
Kubernetes in its docs https://kubernetes-csi.github.io have a drivers list.
One of the driver was pointing to an external github account. That github account was not registered on github.com
So I was able to takeover the account and host PoC

## Kubernetes Version:
NA

## Component Version:
NA

## Steps To Reproduce:

  1. Go to https://kubernetes-csi.github.io/docs/drivers.html
  2. Search for `MacroSAN`
  3. Click on  `MacroSAN`
  4. You will be taken to this repository https://github.com/macrosan-csi/macrosan-csi-driver
  5. You will see takeover message there

## Supporting Material/References:

- https://github.com/macrosan-csi/macrosan-csi-driver
- https://kubernetes-csi.github.io/docs/drivers.html

{F1556768}

## Reference

- https://hackerone.com/reports/1212853

## Impact

An attacker can takeover the repository and host malicious code on it, when any user or employee will refer the docs and tries to download the dirver, they will end up using malicious code which could lead to RCE.

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
