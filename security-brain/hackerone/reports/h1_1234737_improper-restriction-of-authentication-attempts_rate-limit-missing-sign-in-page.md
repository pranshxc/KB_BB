---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1234737'
original_report_id: '1234737'
title: Rate limit missing sign-in page
weakness: Improper Restriction of Authentication Attempts
team_handle: tennessee-valley-authority
created_at: '2021-07-31T11:16:29.040Z'
disclosed_at: '2023-07-11T19:58:37.558Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 5
asset_identifier: '*.tva.gov'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Rate limit missing sign-in page

## Metadata

- HackerOne Report ID: 1234737
- Weakness: Improper Restriction of Authentication Attempts
- Program: tennessee-valley-authority
- Disclosed At: 2023-07-11T19:58:37.558Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hello there,

A common threat web developers face is a password-guessing attack known as a brute force attack. A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works.

The sign-in page where brute force is enabled and there is no rate limit: **https://metdata.tva.gov/**

I made 1.5k+ requests but still, the server is not blocking my requests.

* F1395048 

##Steps To Reproduce:
* Burp suite to brute forcing on the sign-in page.

## Impact

Attackers are able to access NTID and password.

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
