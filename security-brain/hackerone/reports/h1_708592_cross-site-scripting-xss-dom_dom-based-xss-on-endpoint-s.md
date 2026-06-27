---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '708592'
original_report_id: '708592'
title: '[█████] — DOM-based XSS on endpoint `/?s=`'
weakness: Cross-site Scripting (XSS) - DOM
team_handle: deptofdefense
created_at: '2019-10-06T16:14:32.973Z'
disclosed_at: '2019-12-02T20:02:45.805Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# [█████] — DOM-based XSS on endpoint `/?s=`

## Metadata

- HackerOne Report ID: 708592
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: deptofdefense
- Disclosed At: 2019-12-02T20:02:45.805Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Description

GET parameter `s` is vulnerable to DOM-based XSS on endpoint `/?s=`. XSS affects all users and no authentication or login is required.

## Proof of Concept

Visit the following URL for PoC:

https://██████/?s=%27%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

█████████

## Explanation

This DOM-based XSS vulnerability is due to lack of sanitization on the input fetched via search input field. 

Responsible JS file for this issue is:
`https://██████/wp-content/themes/iase/js/search.js`

On line 12, `var $search = ...` is getting input from the Search field but there is no sanitization for single quote which leads to this XSS vulnerability when it is appended.

█████

## Impact

An attacker can take over an account of an authenticated user by stealing any anti-CSRF tokens and using that token to takeover an account.

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
