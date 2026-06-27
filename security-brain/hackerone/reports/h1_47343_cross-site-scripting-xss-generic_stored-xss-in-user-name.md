---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47343'
original_report_id: '47343'
title: Stored xss in user name
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mobilevikings
created_at: '2015-02-10T18:00:41.808Z'
disclosed_at: '2015-03-04T14:20:01.118Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored xss in user name

## Metadata

- HackerOne Report ID: 47343
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mobilevikings
- Disclosed At: 2015-03-04T14:20:01.118Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

In prev report i showed xss in user name thru cookie, there is another place where this name shows and fired xss.
After send auth request open https://mobilevikings.be/en/account/authorization/overview/ in account who send request and press "Remove authorization" and got another way to fire xss payload.
param x:authorization-to-first-name is properly sanitized but probably when it goes to modal window it unsanitize.

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
