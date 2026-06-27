---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1962645'
original_report_id: '1962645'
title: '[accounts.reddit.com] Redirect parameter allows for XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: reddit
created_at: '2023-04-26T16:43:39.184Z'
disclosed_at: '2023-05-18T13:46:49.459Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 359
asset_identifier: accounts.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [accounts.reddit.com] Redirect parameter allows for XSS

## Metadata

- HackerOne Report ID: 1962645
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: reddit
- Disclosed At: 2023-05-18T13:46:49.459Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello team! I was tampering with the dest parameter in accounts.reddit.com and found out it is vulnerable to Cross Site Scripting once the victim performs the log in.

## Steps To Reproduce:
  1. Enter to the following link: ```https://accounts.reddit.com/?dest=javascript:alert(document.domain)```
  - If not signed in, the user will be promped to log in and after doing so XSS will excecute

{F2315850}
  - If user is logged into his account, following the link will also make the XSS pop up

{F2315847}

## Impact

An attacker could trick users into executing XSS, executing code and stealing their cookies only by them logging in.

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
