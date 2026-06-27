---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '13314'
original_report_id: '13314'
title: CRLF Injection
weakness: Cross-Site Request Forgery (CSRF)
team_handle: khanacademy
created_at: '2014-05-25T16:42:06.922Z'
disclosed_at: '2014-08-07T14:13:27.746Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CRLF Injection

## Metadata

- HackerOne Report ID: 13314
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: khanacademy
- Disclosed At: 2014-08-07T14:13:27.746Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Is it possible for a remote attacker to inject custom HTTP headers. For example, an attacker can inject session cookies or HTML code. This may conduct to vulnerabilities like XSS (cross-site scripting) or session fixation.

PoC
https://crowdin.khanacademy.org/page/in-context-localization?email=%0d%0a%20InjectedBy:BigBear

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
