---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226960'
original_report_id: '226960'
title: '[platform.harvestapp.com] Reflected XSS in Error Message via URL parameters'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: harvest
created_at: '2017-05-08T19:37:23.751Z'
disclosed_at: '2017-05-09T15:21:23.311Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [platform.harvestapp.com] Reflected XSS in Error Message via URL parameters

## Metadata

- HackerOne Report ID: 226960
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: harvest
- Disclosed At: 2017-05-09T15:21:23.311Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi @jorgeleria,

I came across a potential reflected XSS vector while exploring **platform.harvestapp.com** functionality. At present, I have been unable to locate a functional payload, so would like to report this as HTML injection.

## Proof of Concept
### Steps to reproduce
1. Visit the below Demonstration URL
2. Select "Start Timer"
3. The "Namespace" error message will present the unsanitised HTML (a marquee)

### Demonstration URL
```
https://platform.harvestapp.com/platform/timer?app_name=TestCompany&closable=false&permalink=http://example.com/1/'"><h1><marquee>Test HTML</marquee></h1>&external_item_id=1&external_item_name=Test - Please click Start Timer
```
### Screenshot
{F182792}

Please let me know if you require any additional details regarding this vulnerability.

Thanks!

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
