---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1406598'
original_report_id: '1406598'
title: Rxss on █████████ via logout?service=javascript:alert(1)
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-11-21T20:11:26.304Z'
disclosed_at: '2021-12-22T16:21:43.142Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Rxss on █████████ via logout?service=javascript:alert(1)

## Metadata

- HackerOne Report ID: 1406598
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-12-22T16:21:43.142Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
I found open redirect and xss (Rxss) at the ██████████ logout page, https://████/██████████/logout?service=https://google.com It also allows javascript URIs, leading to Xss

## Impact

Attacker can trick users to visit malicious websites or can lead to phishing and many other type of attacks, and can steal user token, IP & etc. with xss

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Take this URL: https://███████/█████████/logout?service=https://google.com
  1. Change "https://google.com" to whatever URL you want to redirect to.
  1. Visit the URL and click on back button and you will be redirected to that site
  1. for xss replace https://www.google.com with you xss payload ex: https://██████████/██████/logout?service=javascript:alert(1)

## Suggested Mitigation/Remediation Actions

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
