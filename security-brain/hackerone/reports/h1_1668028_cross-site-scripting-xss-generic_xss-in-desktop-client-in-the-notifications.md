---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1668028'
original_report_id: '1668028'
title: XSS in Desktop Client in the notifications
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2022-08-12T19:00:00.538Z'
disclosed_at: '2022-11-25T11:29:58.569Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 49
asset_identifier: Desktop Client
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in Desktop Client in the notifications

## Metadata

- HackerOne Report ID: 1668028
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2022-11-25T11:29:58.569Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The `Nextcloud Desktop Client` application does not properly neutralize the names of files before using them.

## Steps To Reproduce:

### Server Machine
1. Install the `Nextcloud Server` application
2. Log into your account

### Client Machine
3. Install the `Nextcloud Desktop Client` application onto a machine that is running the `Windows 10` operating system
4. Log into your account

### Server Machine
5. Upload any file to your `Nextcloud Server` instance
6. Rename the file that you uploaded to `<h1><b><i><u>MikeIsAStar`

### Client Machine
7. Wait until a notification appears exclaiming that some files could not synchronized
8. Open the main dialog window of the `Nextcloud Desktop Client` application
9. Observe that the name of the file that you uploaded is treated as `HyperText Markup Language`

## Supporting Material/References:
{F1864812}

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
