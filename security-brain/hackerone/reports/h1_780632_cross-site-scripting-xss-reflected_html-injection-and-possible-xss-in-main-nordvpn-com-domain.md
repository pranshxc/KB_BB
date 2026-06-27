---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '780632'
original_report_id: '780632'
title: Html Injection and Possible XSS in main nordvpn.com domain
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: nordsecurity
created_at: '2020-01-22T16:20:26.412Z'
disclosed_at: '2020-02-21T11:28:56.877Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: '*.nordvpn.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Html Injection and Possible XSS in main nordvpn.com domain

## Metadata

- HackerOne Report ID: 780632
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: nordsecurity
- Disclosed At: 2020-02-21T11:28:56.877Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
HTML injection in main domain can allow hackers forward users to any another domain. Also, if anybody can find method to bypass cloudflare filter hackers can steak cookie with with vuln 

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Go to https://nordvpn.com/blog/?1%25%32%32%25%33%65%25%33%63%25%32%66%25%36%31%25%33%65%25%33%63%25%36%31%25%30%63href%25%33%64%25%32%32http://3232235777
  2. Check, that links on the bottom of page goes to 192.168.1.1
   {F692879}

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

The vulnerability allow a malicious user to inject html tags and (possible) execute Javascript which could lead to steal user's session

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
