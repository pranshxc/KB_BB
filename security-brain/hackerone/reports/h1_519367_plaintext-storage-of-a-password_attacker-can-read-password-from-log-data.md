---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '519367'
original_report_id: '519367'
title: Attacker can read password from log data
weakness: Plaintext Storage of a Password
team_handle: midpoint_h1c
created_at: '2019-03-31T20:55:20.158Z'
disclosed_at: '2019-06-15T12:47:55.648Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
asset_identifier: https://github.com/evolveum/midpoint
asset_type: URL
max_severity: critical
tags:
- hackerone
- plaintext-storage-of-a-password
---

# Attacker can read password from log data

## Metadata

- HackerOne Report ID: 519367
- Weakness: Plaintext Storage of a Password
- Program: midpoint_h1c
- Disclosed At: 2019-06-15T12:47:55.648Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Attacker can read plain text password from log data.

## Steps To Reproduce:

  1. From application dashboard choose Users section, I simultaneously ran process hacker to see the process disk write and read behavior.
  2. change the password of one of the users, and you see in process hacker window the place for log data creation.
  3. Open the file in favorite editor in that place:
%UserProfile%\AppData\Local\Temp\tomcat.1470616378544174392.8080\work\Tomcat\localhost\midpoint 

## Supporting Material/References:
I have uploaded a video for POC.

## Impact

Attacker can read plain text password from log data.

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
