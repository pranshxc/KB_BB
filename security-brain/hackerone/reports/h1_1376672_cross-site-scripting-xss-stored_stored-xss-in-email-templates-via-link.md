---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1376672'
original_report_id: '1376672'
title: Stored XSS in Email Templates via link
weakness: Cross-site Scripting (XSS) - Stored
team_handle: judgeme
created_at: '2021-10-20T22:12:22.444Z'
disclosed_at: '2021-11-18T06:05:44.136Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 79
asset_identifier: judge.me
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in Email Templates via link

## Metadata

- HackerOne Report ID: 1376672
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: judgeme
- Disclosed At: 2021-11-18T06:05:44.136Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Stored cross-site scripting (also known as second-order or persistent XSS) arises when an application receives data from an untrusted source and includes that data within its later HTTP responses in an unsafe way.

## FYI:
I Install judge.me in Shopify E-Commerce

## Steps To Reproduce:

  1.  Go to `Requests > Email Templates`

{F1488407}

  2. Click `New Templates`

{F1488408}

3. Edit this block 

{F1488410}

4. Insert Link with XSS payload (See image below)

{F1488413}

5. Then save email
6. To trigger the XSS, you can click `Click Here` text

{F1488415}

## Impact

Session Hijacking, Cookie Stealing

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
