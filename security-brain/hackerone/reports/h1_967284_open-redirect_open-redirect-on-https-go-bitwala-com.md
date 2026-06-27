---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '967284'
original_report_id: '967284'
title: Open Redirect on https://go.bitwala.com/
weakness: Open Redirect
team_handle: nuri
created_at: '2020-08-26T05:32:39.051Z'
disclosed_at: '2020-10-30T06:27:35.362Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 29
tags:
- hackerone
- open-redirect
---

# Open Redirect on https://go.bitwala.com/

## Metadata

- HackerOne Report ID: 967284
- Weakness: Open Redirect
- Program: nuri
- Disclosed At: 2020-10-30T06:27:35.362Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello 
I found  open redirect bug on https://go.bitwala.com.
I know that domain is not in scope.I just want to inform a bug.

 Steps To Reproduce:

1. go to `https://go.bitwala.com/d4ffbnr?campaign=brand-nov&adgroup=native&creative=link-liquidity%20&fallback=https%3A%2F%2Fwww.bitwala.com%2F%3Futm_source%3Dcryptomonday%26utm_campaign%3Dbrand-nov%26utm_medium%3Dnative%26utm_content%3Dlink-liquidity%20`

2. Change the url like this`https://go.bitwala.com/d4ffbnr?campaign=brand-nov&adgroup=native&creative=link-liquidity%20&fallback=https://www.google.com`

3. It will redirect to `https://www.google.com`

## Impact

An attacker can use this vulnerability to redirect  other malicious,evil websites
.
https://cwe.mitre.org/data/definitions/601.html

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
