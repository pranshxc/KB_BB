---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '190870'
original_report_id: '190870'
title: Stored XSS on new Calling plugin (spreed)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2016-12-13T16:47:24.296Z'
disclosed_at: '2016-12-13T21:08:22.342Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS on new Calling plugin (spreed)

## Metadata

- HackerOne Report ID: 190870
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2016-12-13T21:08:22.342Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

There's a stored xss vulnerability ....

Proof Of Concept :
===============
1. Set `name` as an xss payload like `"x><img src=a onerror=alert(1)>`.
{F143238}
2. Invite people to single call room.
3. Xss will execute in IE. (It doesn't support CSP)
{F143237}

Impact :
========
Admin user can be xssed via this method if admin uses browsers like IE.

Let me know if you need help in reproducing

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
