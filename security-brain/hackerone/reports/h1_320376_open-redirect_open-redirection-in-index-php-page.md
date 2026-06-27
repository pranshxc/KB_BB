---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '320376'
original_report_id: '320376'
title: Open Redirection in index.php page
weakness: Open Redirect
team_handle: security
created_at: '2018-02-27T17:35:48.568Z'
disclosed_at: '2018-03-07T16:39:13.032Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 52
asset_identifier: www.hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open Redirection in index.php page

## Metadata

- HackerOne Report ID: 320376
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2018-03-07T16:39:13.032Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Redirection is performed by HackerOne website when **index.php** page is visited. The parameter to **index.php** is used in redirection. By manipulating this parameter, an attacker can redirect victim outside www.hackerone.com

**Description:**
When a user visit www.hackerone.com/index.php/xyz, he/she is redirected to www.hackerone.com/xyz. However, when visiting www.hackerone.com/index.php/index.phpxyz, user will be redirected to www.hackerone.comxyz (without a slash between **com** and **xyz**).

Further, when visiting www.hackerone.com/index.php/index.php.hacker0ne.com, user will be redirected to www.hackerone.com.hacker0ne.com, a domain **hacker0ne.com**

### Steps To Reproduce

1. Visit https://www.hackerone.com/index.php/index.php.hacker0ne.com
2. Notice that the site redirects to https://www.hackerone.com.hacker0ne.com/

## Impact

Attacker can phish users

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
