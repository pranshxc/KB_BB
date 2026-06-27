---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '41758'
original_report_id: '41758'
title: Stored XSS in api key of operator wallet
weakness: Cross-site Scripting (XSS) - Generic
team_handle: enter
created_at: '2014-12-23T22:06:00.061Z'
disclosed_at: '2015-04-03T14:00:43.650Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in api key of operator wallet

## Metadata

- HackerOne Report ID: 41758
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: enter
- Disclosed At: 2015-04-03T14:00:43.650Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. Make an operation wallet
2. Open wallet settings
3. Press "New key"
4. In source code remove "maxlength=30" of key's name input tag - no length check on server-side
5. Fill name input with "<a href="example.com">asdf</a>" (PoC)
6. Press "Generate Key" 
7. After that when open wallet settings we got XSS.
8. In case we can share this type of wallet this xss can be used against another user.
Problem is that there is some filter on server side and at this moment i trying to find way to bypass it and fire javascript command.

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
