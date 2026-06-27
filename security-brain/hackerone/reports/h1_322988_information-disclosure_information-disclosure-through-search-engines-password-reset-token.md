---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '322988'
original_report_id: '322988'
title: Information disclosure through search engines (password reset token)
weakness: Information Disclosure
team_handle: upserve
created_at: '2018-03-06T22:22:47.361Z'
disclosed_at: '2018-03-13T18:31:38.883Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
asset_identifier: hq.breadcrumb.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Information disclosure through search engines (password reset token)

## Metadata

- HackerOne Report ID: 322988
- Weakness: Information Disclosure
- Program: upserve
- Disclosed At: 2018-03-13T18:31:38.883Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Search on google for: 
site:"hq.breadcrumb.com"

Or access this link:
https://www.google.com/search?q=site%3A%22hq.breadcrumb.com%22&oq=site%3A%22hq.breadcrumb.com%22&aqs=chrome..69i57j69i58.6216j0j7&sourceid=chrome&ie=UTF-8

Note that this vulnerability can be obtain on other search engines.

## Impact

An attacker can obtain an unused password reset token found using google.com in order to get access to an user account. 

In order to better ensure the security of the application do not allow google indexing of the token/password reset controller.

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
