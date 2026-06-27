---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '225777'
original_report_id: '225777'
title: DOMPurify 0.8.9 released
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2017-05-03T08:12:33.951Z'
disclosed_at: '2020-03-01T14:05:56.195Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# DOMPurify 0.8.9 released

## Metadata

- HackerOne Report ID: 225777
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2020-03-01T14:05:56.195Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Got the following via the [DOMPurify-Security mailing list](https://lists.ruhr-uni-bochum.de/mailman/listinfo/dompurify-security):

```
*Intro*

A new version of DOMPurify was released today: DOMPurify 0.8.9

*Background*

DOMPurify showed weaknesses when handling both the recent Safari
DOMParser XSS and a Firefox mXSS when working with document.write().

Caused by a broken logical check, not all browser bugs were being worked
around correctly.

*Fix*

DOMPurify now performs better checks to mitigate both the Safari
DOMParser XSS and a Firefox mXSS when using document.write().

*Packages*

Updated packages are available here:
https://github.com/cure53/DOMPurify/releases/tag/0.8.9

EOF
```

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
