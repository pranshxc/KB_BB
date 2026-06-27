---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '305972'
original_report_id: '305972'
title: Potential infinite loop in gdImageCreateFromGifCtx!
weakness: Uncontrolled Resource Consumption
team_handle: ibb
created_at: '2018-01-17T17:27:50.375Z'
disclosed_at: '2019-11-12T09:18:47.646Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: PHP
asset_type: OTHER
max_severity: none
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Potential infinite loop in gdImageCreateFromGifCtx!

## Metadata

- HackerOne Report ID: 305972
- Weakness: Uncontrolled Resource Consumption
- Program: ibb
- Disclosed At: 2019-11-12T09:18:47.646Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description
-----
It is easy to trigger in web application if the web use GD as its image library.
For example, It can be triggered if a website resize the user-uploaded GIF, and **ALL** PHP version are affected!
　
## Original bug report
-----
- https://bugs.php.net/bug.php?id=75571

　
## Note
-----
- CVE-2018-5711 assigned

　
Thanks :)

## Impact

A malicious GIF can trigger an infinite loop and lead to exhausted the server resource!

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
