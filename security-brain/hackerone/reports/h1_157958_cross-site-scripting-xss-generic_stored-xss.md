---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '157958'
original_report_id: '157958'
title: Stored XSS
weakness: Cross-site Scripting (XSS) - Generic
team_handle: instacart
created_at: '2016-08-09T20:13:55.861Z'
disclosed_at: '2016-09-09T00:14:59.475Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS

## Metadata

- HackerOne Report ID: 157958
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: instacart
- Disclosed At: 2016-09-09T00:14:59.475Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

First log in account.

We headed to the "lists and recipes" option

https://www.instacart.com/store/demo/lists


create a new list "add list"

Payload
"></script></title><script>alert(document.domain)</script>


URL pwned.

https://www.instacart.com/lists/izy0w6Q?preview=true

attached a screenshot

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
