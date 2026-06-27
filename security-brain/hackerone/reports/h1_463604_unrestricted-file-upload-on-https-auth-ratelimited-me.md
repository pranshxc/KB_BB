---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '463604'
original_report_id: '463604'
title: Unrestricted File Upload on https://auth.ratelimited.me
team_handle: ratelimited
created_at: '2018-12-17T01:13:14.056Z'
disclosed_at: '2019-05-18T15:27:21.078Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
asset_identifier: '*.ratelimited.me'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Unrestricted File Upload on https://auth.ratelimited.me

## Metadata

- HackerOne Report ID: 463604
- Weakness: 
- Program: ratelimited
- Disclosed At: 2019-05-18T15:27:21.078Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello security team,

Have found a way to upload files that aren't images on https://auth.ratelimited.me/

Steps to reproduce:

1. Login at https://auth.ratelimited.me/
2. Click "change photo" and intercept with a tool (used burpsuite)
3. Choose "gravatar" option and change the 'url' parameter to anything you would like
4. Done
Ps: The same occurs when you intercept "no photo" option

Ps2: I could not execute code through this, but i thought it was a valid report because i tried to upload .txt files in "upload photo" options and it was not allowed.

If you need further information, please contact me
Best Regards,
Daniel

## Impact

possibility of uploading anything rather than images

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
