---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223846'
original_report_id: '223846'
title: Access to completion page without performing any action
weakness: Improper Access Control - Generic
team_handle: weblate
created_at: '2017-04-25T17:39:21.722Z'
disclosed_at: '2017-05-18T07:58:24.157Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-access-control-generic
---

# Access to completion page without performing any action

## Metadata

- HackerOne Report ID: 223846
- Weakness: Improper Access Control - Generic
- Program: weblate
- Disclosed At: 2017-05-18T07:58:24.157Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi!,

This is much of a best practice as it doesn't have much impact on the user. But I believe you may want to know.

After making a registration or on finalizing a password reset, one is redirected to a page, https://demo.weblate.org/accounts/email-sent/. I noticed that even without making any of the two actions stated above, the page is still accessible.

Regards,
Shuaib

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
