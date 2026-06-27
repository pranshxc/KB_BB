---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2178941'
original_report_id: '2178941'
title: Unauthenticated Jenkins instance exposed information related to █████
weakness: Improper Authentication - Generic
team_handle: deptofdefense
created_at: '2023-09-24T14:11:31.569Z'
disclosed_at: '2024-01-26T18:55:52.109Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 35
tags:
- hackerone
- improper-authentication-generic
---

# Unauthenticated Jenkins instance exposed information related to █████

## Metadata

- HackerOne Report ID: 2178941
- Weakness: Improper Authentication - Generic
- Program: deptofdefense
- Disclosed At: 2024-01-26T18:55:52.109Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Affected URLs - ██████████blue/organizations/jenkins/pipelines
████████


██████████

████

Also notice that the information is transmitted in clear text as the server is running on HTTP.

## Impact

An attacker can read or edit sensitive information belonging to █████ by abusing this vulnerability.

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Navigate to ███████ , and other sections. It is exposing information related to ███

## Suggested Mitigation/Remediation Actions
It is recommended to Implement authentication on this Jenkins instance

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
