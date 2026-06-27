---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1434179'
original_report_id: '1434179'
title: Broken Domain Link Takeover from kubernetes.io docs
weakness: Insecure Temporary File
team_handle: kubernetes
created_at: '2021-12-22T17:22:58.381Z'
disclosed_at: '2022-04-03T04:47:16.175Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: kubernetes.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-temporary-file
---

# Broken Domain Link Takeover from kubernetes.io docs

## Metadata

- HackerOne Report ID: 1434179
- Weakness: Insecure Temporary File
- Program: kubernetes
- Disclosed At: 2022-04-03T04:47:16.175Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Report Submission Form

## Summary:
Kubernetes docs have Spanish translation available. One of the pages of the Portuguese doc has an external reference to a  website .
The website is not registered and can be purchased and used to host malicious content.

## Kubernetes Version:
NA

## Component Version:
NA
## Steps To Reproduce:

1. Go to https://kubernetes.io/pt-br/docs/concepts/cluster-administration/addons/
2. Search for `contiv`
3. Click on 'Contiv`
You will be redirected to https://contiv.io/ which does not exist...

## Supporting Material/References:
1. https://contiv.io/
2.  https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=contiv.io

## Impact

As an attacker, I can host malicious content on the website.
I can also, host malicious sdk or softwares, which user will think is part of the deployment docs as its referred in kubernetes.io, this can lead to RCE for users who are referring to this doc.

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
