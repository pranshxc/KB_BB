---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1398572'
original_report_id: '1398572'
title: Broken Link Takeover from kubernetes.io docs
weakness: Improper Access Control - Generic
team_handle: kubernetes
created_at: '2021-11-12T04:48:36.870Z'
disclosed_at: '2021-12-16T00:31:22.858Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: kubernetes.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Broken Link Takeover from kubernetes.io docs

## Metadata

- HackerOne Report ID: 1398572
- Weakness: Improper Access Control - Generic
- Program: kubernetes
- Disclosed At: 2021-12-16T00:31:22.858Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Report Submission Form

## Summary:
Kubernetes docs has Spanish translation available. One of the page of Portuguese doc has an external reference to a github repository.
The github account was not registered on github.com.
So I was able to takeover the page and host the PoC

## Kubernetes Version:
NA

## Component Version:
NA

## Steps To Reproduce:

  1. Go to https://kubernetes.io/pt-br/docs/concepts/cluster-administration/addons/
  2. Search for `Multus`
  3. Click on `Multus`
  4. You will be taken to this repository https://github.com/Intel-Corp/multus-cni and you will see takeover message there

## Supporting Material/References:

- https://github.com/Intel-Corp/multus-cni
- https://kubernetes.io/pt-br/docs/concepts/cluster-administration/addons/

{F1511425}

## Impact

As an attacker, I can host malicious content on the github repository.
I can also, host malicious sdk or softwares, which user will think is part of the deployment docs as its referreded in kubernetes.io, this can lead to RCE for users who are referring to this doc

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
