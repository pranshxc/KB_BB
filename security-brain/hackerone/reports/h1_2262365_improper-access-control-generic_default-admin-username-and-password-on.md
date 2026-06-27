---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2262365'
original_report_id: '2262365'
title: Default Admin Username and Password on ███
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2023-11-23T12:30:00.416Z'
disclosed_at: '2023-12-21T17:35:19.800Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- improper-access-control-generic
---

# Default Admin Username and Password on ███

## Metadata

- HackerOne Report ID: 2262365
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2023-12-21T17:35:19.800Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It is possible to access the application is using the default username and password 
Steps To Reproduce:
1-Go to https://███/geoportal/ and login with credentials:
user and password: admin
user and password: gptadmin
Poc video attached

## Impact

A Department of Defense website was misconfigured in a manner that may have allowed a malicious user to login with administrator for the default organization account credentials and delete posts , edit website

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
POC video

## Suggested Mitigation/Remediation Actions

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
