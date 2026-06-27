---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1212853'
original_report_id: '1212853'
title: Broken link hijacing in https://kubernetes-csi.github.io/docs/drivers.html
weakness: Violation of Secure Design Principles
team_handle: kubernetes
created_at: '2021-05-30T04:22:32.909Z'
disclosed_at: '2021-11-06T18:04:40.918Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
asset_identifier: kubernetes-csi.github.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Broken link hijacing in https://kubernetes-csi.github.io/docs/drivers.html

## Metadata

- HackerOne Report ID: 1212853
- Weakness: Violation of Secure Design Principles
- Program: kubernetes
- Disclosed At: 2021-11-06T18:04:40.918Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary : When a web application has any pages, sources, links to external 3rd party services and are broken then the attacker can claim those endpoints to successfully conduct the attack and claim those endpoints on behalf of the target website and impersonate his identity.

Steps To Reproduce
1) visit https://kubernetes-csi.github.io/docs/drivers.html
2) search for DriveScale
3) click on that link
4) you will be redirected to github and it shows 404 
5) change your username to  DriveScale
6) create k8s-plugins repository
7) When someone clicks on DriveScale link they will be redirected to attacker repository

References
https://hackerone.com/reports/1031321
https://hackerone.com/reports/1117079
https://edoverflow.com/2017/broken-link-hijacking/

For POC I have attached video

## Impact

The user will install wrong CSI driver which leads to impersonation attack. The attacker can install Ransomware, trojan etc.

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
