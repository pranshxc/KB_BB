---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223331'
original_report_id: '223331'
title: '[demo.weblate.org] Stored Self-XSS via Editor Link in Profile'
weakness: Cross-site Scripting (XSS) - Stored
team_handle: weblate
created_at: '2017-04-24T09:16:48.255Z'
disclosed_at: '2017-05-17T14:20:03.777Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# [demo.weblate.org] Stored Self-XSS via Editor Link in Profile

## Metadata

- HackerOne Report ID: 223331
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: weblate
- Disclosed At: 2017-05-17T14:20:03.777Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Input validation and/or sanitisation is not currently applied to the "Editor Link" in the user's [Preferences](https://demo.weblate.org/accounts/profile/#preferences). Consequently, it is possible to store a JavaScript payload which is stored and executes in the Weblate instance context.

{F178717}

## Steps to reproduce
1. Visit the above Preferences page and identify the Editor Link field
2. Populate the field with: `javascript:confirm(document.domain)`
3. Visit a [translation page](https://demo.weblate.org/translate/hello/master/zh_CN/?checksum=6412684aaf018e8e) and select a Source String Location
4. The XSS will trigger upon clicking on a Source String (e.g. `main.c`)

{F178716}

Please let me know if you require any additional information regarding this issue.

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
