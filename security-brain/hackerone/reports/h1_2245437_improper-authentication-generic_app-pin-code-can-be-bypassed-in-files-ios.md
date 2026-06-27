---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2245437'
original_report_id: '2245437'
title: App PIN code can be bypassed in Files iOS
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2023-11-09T08:35:49.098Z'
disclosed_at: '2023-12-18T08:26:41.519Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 26
asset_identifier: it.twsweb.Nextcloud
asset_type: APPLE_STORE_APP_ID
max_severity: medium
tags:
- hackerone
- improper-authentication-generic
---

# App PIN code can be bypassed in Files iOS

## Metadata

- HackerOne Report ID: 2245437
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2023-12-18T08:26:41.519Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Hope you are doing great.

Note: IoS APP Vs.: 4.9.1

I got a vulnerability in your applications via which an attacker is able to bypass the PIN.
The attacker just need to bruteforce the 4 digit PIN as unlimited tries is accepted by the application, the attacker can simply do a bruteforce and access the application.

PoC:
{F2844276}

## Impact

Authentication Bypass leading to application access

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
