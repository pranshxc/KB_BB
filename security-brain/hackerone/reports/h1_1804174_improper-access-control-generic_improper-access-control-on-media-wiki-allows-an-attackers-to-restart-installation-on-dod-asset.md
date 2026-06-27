---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1804174'
original_report_id: '1804174'
title: Improper Access Control on Media Wiki allows an attackers to restart installation
  on DoD asset
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2022-12-14T11:43:28.451Z'
disclosed_at: '2023-03-24T17:33:54.173Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-access-control-generic
---

# Improper Access Control on Media Wiki allows an attackers to restart installation on DoD asset

## Metadata

- HackerOne Report ID: 1804174
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2023-03-24T17:33:54.173Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I notice that is possible to restart installation on this media wiki website due to the fact that /mw-config/index.php is available without authentication

Poc:
https://█████████/mw-config/index.php

Regards

## Impact

Attackers can restart the application.

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Go directly to https://██████████/mw-config/index.php and you should see the restart installation button.

## Suggested Mitigation/Remediation Actions
Block all access to your mw-config folder.

We fixed this by adding:

RedirectMatch 404 /\mw-config

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
