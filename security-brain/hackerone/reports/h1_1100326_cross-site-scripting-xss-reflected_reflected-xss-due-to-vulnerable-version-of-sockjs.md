---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1100326'
original_report_id: '1100326'
title: Reflected XSS due to vulnerable version of sockjs
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: automattic
created_at: '2021-02-10T19:29:54.897Z'
disclosed_at: '2022-04-29T17:38:24.702Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: simperium.com
asset_type: URL
max_severity: high
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS due to vulnerable version of sockjs

## Metadata

- HackerOne Report ID: 1100326
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: automattic
- Disclosed At: 2022-04-29T17:38:24.702Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
There is reflected XSS on *.simperium.com. The bug exists due to a vulnerable version of sockjs library.

## Platform(s) Affected:
simperium.com
js.simperium.com

## Steps To Reproduce:
  1. Visit https://simperium.com/sock/1/0/0/0/htmlfile?c=alert('XSS')//
  2. You will see an alert message because of executed JS

## Impact

XSS may be used by an attacker to perform a lot of things, for example, to steal user session

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
