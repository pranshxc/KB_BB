---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1998179'
original_report_id: '1998179'
title: Error Page Content Spoofing or Text Injection
team_handle: pyca
created_at: '2023-05-23T16:33:00.563Z'
disclosed_at: '2023-07-03T22:00:57.887Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.cryptography.io'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Error Page Content Spoofing or Text Injection

## Metadata

- HackerOne Report ID: 1998179
- Weakness: 
- Program: pyca
- Disclosed At: 2023-07-03T22:00:57.887Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Domain : cryptography.io

Description: Content spoofing, also referred to as content injection, "arbitrary text injection" or virtual defacement, is an attack targeting a user made possible by an injection vulnerability in a web application. When an application does not properly handle user-supplied data, an attacker can supply content to a web application, typically via a parameter value, that is reflected back to the user. This presents the user with a modified page under the context of the trusted domain.

Steps to Reproduce:
1 - Go to https://cryptography.io/en/latest/_sources/
2 - Write anything after the slash and it will be printed in the page

POC: https://cryptography.io/en/latest/_sources/%20%20%20%20%20%20%20This%20site%20is%20moved%20to%20attacker.com

Reference: 
https://hackerone.com/reports/498562
https://hackerone.com/reports/327671

Solution:
 Just delete the printed path from the page

## Impact

This attack is typically used as, or in conjunction with social engineering because the attack is exploiting a code-based vulnerability and a user's trust. As a side note, this attack is widely misunderstood as a kind of bug that brings no impact.

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
