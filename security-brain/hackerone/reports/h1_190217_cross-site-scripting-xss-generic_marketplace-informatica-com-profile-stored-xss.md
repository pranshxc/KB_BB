---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '190217'
original_report_id: '190217'
title: '[marketplace.informatica.com] Profile stored XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2016-12-10T22:21:44.175Z'
disclosed_at: '2017-04-19T17:39:07.985Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [marketplace.informatica.com] Profile stored XSS

## Metadata

- HackerOne Report ID: 190217
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2017-04-19T17:39:07.985Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The user name and lastname are inserted into JS with quotes non-escaped:

```javascript
var pageNameDTM = "%name% %lastname%".replace(/[^a-zA-Z0-9 ]/g, "").replace(/  +/g, " ");
```

**PoC:**

1. Log into your account
2. Set your name and lastname to **"-alert(document.domain)-"**
3. Open your profile page https://marketplace.informatica.com/people/%email% from another account

The script will be executed:

{F142515}

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
