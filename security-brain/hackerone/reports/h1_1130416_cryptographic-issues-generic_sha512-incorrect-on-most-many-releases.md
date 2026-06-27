---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1130416'
original_report_id: '1130416'
title: SHA512 incorrect on most/many releases
weakness: Cryptographic Issues - Generic
team_handle: kubernetes
created_at: '2021-03-19T01:13:24.894Z'
disclosed_at: '2021-05-09T20:16:48.395Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: https://github.com/kubernetes/kubernetes
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cryptographic-issues-generic
---

# SHA512 incorrect on most/many releases

## Metadata

- HackerOne Report ID: 1130416
- Weakness: Cryptographic Issues - Generic
- Program: kubernetes
- Disclosed At: 2021-05-09T20:16:48.395Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Report Submission Form

## Summary:
SHA512 is incorrect for most versions of kubernetes.tar.gz releases (https://github.com/kubernetes/kubernetes/releases/).

## Kubernetes Version:
all

## Component Version:
all

## Steps To Reproduce:
[add details for how we can reproduce the issue, including relevant cluster setup and configuration]

curl -sLO https://github.com/kubernetes/kubernetes/releases/download/v1.20.0/kubernetes.tar.gz
shasum -a 512 kubernetes.tar.gz (mac)
openssl dgst -sha512 kubernetes.tar.gz (linux)
sha512sum kubernetes.tar.gz (linux)

All report:
ebfe49552bbda02807034488967b3b62bf9e3e507d56245e298c4c19090387136572c1fca789e772a5e8a19535531d01dcedb61980e42ca7b0461d3864df2c14

Per website, it should be:
cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e

## Supporting Material/References:
https://github.com/kubernetes/kubernetes/releases/tag/v1.20.0

another example:

https://github.com/kubernetes/kubernetes/releases/tag/v1.19.5

Same SHA512:
cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e

## Impact

I suspect its an automation release issue (hence same hash in all places).

* Impact 1: Can't verify artifact is correct artifact.
* Impact 2: Hacked?

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
