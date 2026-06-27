---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '870703'
original_report_id: '870703'
title: Stored XSS in assets.txmblr.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2020-05-11T11:15:09.682Z'
disclosed_at: '2020-05-11T17:39:23.673Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 10
asset_identifier: '*.txmblr.com'
asset_type: WILDCARD
max_severity: none
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in assets.txmblr.com

## Metadata

- HackerOne Report ID: 870703
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2020-05-11T17:39:23.673Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

# Description

Hi, i would like to report a issue that i think is legitimate. to get this XSS we need to create a Post in the attacker account with a payload, after this, it's necessary that a victim reblog this post and so, enter in the edit mode of their own blog, after this the victim will see a button with "CLICK ME" value, so, when the victim click in "CLICK ME" the XSS will be triggerd.

PoC payload:
```
<form>
<input type=submit formaction=javascript:alert(document.domain)>
</form>
```

# Steps to reproduce
1. go to your account
2. create a post with the payload mentioned before
3. victim reblog the post
4. victim enter in the edit mode of their own blog
5. victim click in "CLICK ME" button
6. XSS will be triggerd

## Impact

it is possible to perform malicious actions on the victim's account

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
