---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '877402'
original_report_id: '877402'
title: Hard coded Username and password in GiHub commit
weakness: Use of Hard-coded Credentials
team_handle: kubernetes
created_at: '2020-05-18T18:43:10.513Z'
disclosed_at: '2020-07-24T00:43:07.805Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: https://github.com/kubernetes/kubernetes
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- use-of-hard-coded-credentials
---

# Hard coded Username and password in GiHub commit

## Metadata

- HackerOne Report ID: 877402
- Weakness: Use of Hard-coded Credentials
- Program: kubernetes
- Disclosed At: 2020-07-24T00:43:07.805Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Report Submission Form

## Summary:
I was exploring the GitHub repository and I found some hard coded credentials in the commit history. These credentials are related to Vagrant  tool which is used to setup virtual machines environment, This is a very critical disclosure and can lead to bigger damages. So I am informing this to you guys, please let me know what do you guys think.


## Steps To Reproduce:
VISIT THESE LINKS
Repository :  kubernetes /kubernetes 
Commit Link : https://github.com/kubernetes/kubernetes/commit/5a0159ea00e082bc85bbec18d1ab7ae78d90fa4f
Repository Link : https://github.com/kubernetes/kubernetes/blob/5a0159ea00e082bc85bbec18d1ab7ae78d90fa4f/cluster/kubecfg.sh


## Supporting Material/References:

Reference:
https://hackerone.com/reports/124100

## Impact

Vagrant is a tool for building and managing virtual machine environments in a single workflow. This can give hacker access to the hacker to the automation tool to setup VMs and their environment, which he can use for further escalation.

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
