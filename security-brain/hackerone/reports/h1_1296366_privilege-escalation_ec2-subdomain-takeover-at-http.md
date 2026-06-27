---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1296366'
original_report_id: '1296366'
title: EC2 subdomain takeover at http://████████/
weakness: Privilege Escalation
team_handle: deptofdefense
created_at: '2021-08-09T16:26:45.944Z'
disclosed_at: '2022-02-14T21:24:17.776Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 32
tags:
- hackerone
- privilege-escalation
---

# EC2 subdomain takeover at http://████████/

## Metadata

- HackerOne Report ID: 1296366
- Weakness: Privilege Escalation
- Program: deptofdefense
- Disclosed At: 2022-02-14T21:24:17.776Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

There is a dangling DNS A record that points to an EC2 instance that no longer exists, I was able to claim the EC2 instance and host content on http://███████/.

## Steps To Reproduce:

  1. Visit http://█████████/██████████.html and view the PoC:  ██████


## Suggested Remediation Steps

  Remove the A record pointing to the current ec2 instance. 

## Impact

Hosting content on http://█████/ and potentionally fully bypassing web protections like CORS (in cases of `████████`) or redirecting users to malicious pages.

## Impact

Hosting content on http://██████/ and potentionally fully bypassing web protections like CORS (in cases of `██████████`) or redirecting users to malicious pages,

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Visit http://██████████/█████.html and view the PoC:  █████

## Suggested Mitigation/Remediation Actions
Remove the A record pointing to the current ec2 instance.

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
