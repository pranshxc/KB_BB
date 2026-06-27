---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1711847'
original_report_id: '1711847'
title: XSS in Desktop Client in call notification popup
weakness: Resource Injection
team_handle: nextcloud
created_at: '2022-09-25T21:00:06.166Z'
disclosed_at: '2022-11-25T15:45:02.479Z'
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

# XSS in Desktop Client in call notification popup

## Metadata

- HackerOne Report ID: 1711847
- Weakness: Resource Injection
- Program: nextcloud
- Disclosed At: 2022-11-25T15:45:02.479Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The `Nextcloud Desktop Client` application does not properly neutralize the name of a group conversation before using it.

## Steps To Reproduce:
### Server Machine:
1. Install the `Nextcloud Server` application
2. Create an administrator account
3. Create a user account

### Client Machine:
4. Install the `Nextcloud Desktop Client` application on a machine that is running the `Windows 10` operating system
5. Log in to the user account

### Server Machine:
6. Log in to the administrator account
7. Install the `Nextcloud Talk` application
8. Open the `Nextcloud Talk` application
9. Create a group conversation with the name `<img src="https://avatars.githubusercontent.com/u/99037623">`
10. Add the user to the group conversation
11. Start a call in the group conversation

### Client Machine:
12. Observe that the name of the group conversation is treated as `HyperText Markup Language`

Please do note that group conversation messages are also treated as `HyperText Markup Language`.

## Supporting Material/References:
{F1953705}
{F1953706}
{F1953851}

## Impact

An attacker can inject arbitrary `HyperText Markup Language` in to the `Nextcloud Desktop Client` application.

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
