---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '105953'
original_report_id: '105953'
title: Parameter pollution in social sharing buttons
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2015-12-18T17:40:44.453Z'
disclosed_at: '2015-12-19T02:02:54.132Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 55
tags:
- hackerone
- violation-of-secure-design-principles
---

# Parameter pollution in social sharing buttons

## Metadata

- HackerOne Report ID: 105953
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2015-12-19T02:02:54.132Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello! For example we have a link `https://hackerone.com/blog/introducing-signal-and-impact`, and we will change it to `https://hackerone.com/blog/introducing-signal-and-impact?&u=https://vk.com/durov`. If you send a link to the user and he wants to share a link to facebook, the content will change.
`https://www.facebook.com/sharer.php?u=https://hackerone.com/blog/introducing-signal-and-impact?&u=https://vk.com/durov`

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
