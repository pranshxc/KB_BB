---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '97191'
original_report_id: '97191'
title: Send AJAX request to external domain
weakness: Cross-site Scripting (XSS) - Generic
team_handle: security
created_at: '2015-11-02T01:07:39.782Z'
disclosed_at: '2015-11-14T14:47:09.895Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Send AJAX request to external domain

## Metadata

- HackerOne Report ID: 97191
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: security
- Disclosed At: 2015-11-14T14:47:09.895Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello!

I would like to report about ability to send AJAX request from `hackerone.com` to external domain.

Here is PoC for the last version of Internet Explorer: https://hackerone.com/bugs?subject=%2Fbigbob.lv%2F1337.php%3Fdata%3D

If You visit it, You can see `Hello! This is custom text from external domain` text which is from JSON here https://bigbob.lv/1337.php

You can check console and see there 3 AJAX requests sent from `hackerone.com` to `bigbob.lv`.

It is possible because there is no filtration of `/` slash in JavaScript when it handles `subject` GET param. So, it allows to send AJAX requests to external domain because of `//`.

This PoC will work in old versions of popular browsers which don't support CSP (http://caniuse.com/#feat=contentsecuritypolicy).

I will try to achieve XSS.

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
