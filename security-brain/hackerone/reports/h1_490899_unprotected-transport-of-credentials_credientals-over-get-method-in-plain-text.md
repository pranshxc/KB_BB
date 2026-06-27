---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '490899'
original_report_id: '490899'
title: Credientals Over GET method in plain Text
weakness: Unprotected Transport of Credentials
team_handle: ratelimited
created_at: '2019-02-04T08:15:00.270Z'
disclosed_at: '2019-02-17T17:48:57.512Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.ratelimited.me'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- unprotected-transport-of-credentials
---

# Credientals Over GET method in plain Text

## Metadata

- HackerOne Report ID: 490899
- Weakness: Unprotected Transport of Credentials
- Program: ratelimited
- Disclosed At: 2019-02-17T17:48:57.512Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Description 
While I was testing the application i found this bug where the application is sending the credentials over Plain text in URL : https://auth.ratelimited.me/login?username=testqaz%40grr.la&password=D33vanh%40h%40h%40

Vulnerable URl https://auth.ratelimited.me

## Impact

Impact: if the application is sending the credentials over GET request it will be saved in the history of the Browser

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
