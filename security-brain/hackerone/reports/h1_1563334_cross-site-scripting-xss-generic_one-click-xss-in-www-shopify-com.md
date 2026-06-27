---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1563334'
original_report_id: '1563334'
title: One Click XSS in [www.shopify.com]
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2022-05-09T10:15:55.302Z'
disclosed_at: '2022-07-13T06:13:14.473Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
asset_identifier: '*.shopify.com'
asset_type: WILDCARD
max_severity: medium
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# One Click XSS in [www.shopify.com]

## Metadata

- HackerOne Report ID: 1563334
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2022-07-13T06:13:14.473Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Steps To Reproduce:

  1. You need a web server, put {F1722320} to www
  2. visit it: http://<host>:<port>/poc.html?x=${alert(1)}
3. click it
4. you will see the alert

## Supporting Material:

{F1722333}

## Impact

Cookie Stealing - A malicious user can steal cookies and use them to gain access to the application.
Arbitrary requests - An attacker can use XSS to send requests that appear to be from the victim to the web server.
Malware download - XSS can prompt the user to download malware. Since the prompt looks like a legitimate request from the
site, the user may be more likely to trust the request and actually install the malware.
Defacement - attacker can deface the website usig javascript code.

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
