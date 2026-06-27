---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1707977'
original_report_id: '1707977'
title: XSS in Desktop Client via user status and information
weakness: Resource Injection
team_handle: nextcloud
created_at: '2022-09-21T22:00:01.788Z'
disclosed_at: '2022-11-25T15:44:06.581Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: Desktop Client
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- resource-injection
---

# XSS in Desktop Client via user status and information

## Metadata

- HackerOne Report ID: 1707977
- Weakness: Resource Injection
- Program: nextcloud
- Disclosed At: 2022-11-25T15:44:06.581Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The `Nextcloud Desktop Client` application does not properly neutralize the `Full Name` and `Status Message` of users before using them.

## Steps To Reproduce:

### Server Machine:
1. Install the `Nextcloud Server` application
2. Log into your account
3. Navigate to your profile page
4. Set the `Full Name` of your user to `<img src="https://avatars.githubusercontent.com/u/99037623">`
5. Set the `Status Message` of your user to `<img src="https://avatars.githubusercontent.com/u/99037623">`

### Client Machine:
6. Install the `Nextcloud Desktop Client` application onto a machine that is running the `Windows 10` operating system
7. Log into your account
8. Open the main dialog window of the `Nextcloud Desktop Client` application
9. Observe that the `Full Name` and `Status Message` of your user are treated as `HyperText Markup Language`

## Supporting Material/References:
{F1945608}

## Impact

An attacker can inject arbitrary `HyperText Markup Language` into the `Nextcloud Desktop Client` application.

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
