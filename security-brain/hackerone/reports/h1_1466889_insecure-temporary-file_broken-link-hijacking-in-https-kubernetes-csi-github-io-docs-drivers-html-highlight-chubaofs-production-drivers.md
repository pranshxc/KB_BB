---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1466889'
original_report_id: '1466889'
title: Broken link hijacking in https://kubernetes-csi.github.io/docs/drivers.html?highlight=chubaofs#production-drivers
weakness: Insecure Temporary File
team_handle: kubernetes
created_at: '2022-02-01T15:26:33.661Z'
disclosed_at: '2022-03-25T06:49:29.980Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: kubernetes-csi.github.io
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-temporary-file
---

# Broken link hijacking in https://kubernetes-csi.github.io/docs/drivers.html?highlight=chubaofs#production-drivers

## Metadata

- HackerOne Report ID: 1466889
- Weakness: Insecure Temporary File
- Program: kubernetes
- Disclosed At: 2022-03-25T06:49:29.980Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Report Submission Form

## Summary:
When a web application has any pages, sources, links to external 3rd party services and are broken then the attacker can claim those endpoints to successfully conduct the attack and claim those endpoints on behalf of the target website and impersonate his identity.

## Steps To Reproduce
1) Visit `https://kubernetes-csi.github.io/docs/drivers.html?highlight=chubaofs#production-drivers`
2) Search for ChubaoFS
3) Click on that link
(Steps I followed --> 
Click Link 

{F1601565}

404 Error

{F1601567}

Change my Username to match the broken link 

{F1601566}

Create the required repo.

{F1601568}

4) You will be redirected to My github repo
5) When someone clicks on the ChubaoFS link they will be redirected to the attacker repository

## Supporting Material/References:

1. `https://hackerone.com/reports/1031321`
2. `https://hackerone.com/reports/1117079`
3. `https://edoverflow.com/2017/broken-link-hijacking/`

## Impact

The user will install the wrong drivers which leads to impersonation attacks. The attacker can install Ransomware, trojan, etc.

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
