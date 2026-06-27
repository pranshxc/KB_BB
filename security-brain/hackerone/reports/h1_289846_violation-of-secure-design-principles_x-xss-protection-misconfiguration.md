---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '289846'
original_report_id: '289846'
title: X-XSS-Protection -> Misconfiguration
weakness: Violation of Secure Design Principles
team_handle: deptofdefense
created_at: '2017-11-13T13:44:40.009Z'
disclosed_at: '2017-12-15T21:25:10.544Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- violation-of-secure-design-principles
---

# X-XSS-Protection -> Misconfiguration

## Metadata

- HackerOne Report ID: 289846
- Weakness: Violation of Secure Design Principles
- Program: deptofdefense
- Disclosed At: 2017-12-15T21:25:10.544Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there,

**URL:** https://www.sfl-tap.army.mil/
I have seen that the website is using the X-XSS-Protection Header.

But it has a strange configuration.
When I take a look at securityheaders, I've seen that you guys use this as configuration.

**X-XSS-Protection:** DENY

DENY is used for the X-Frame Option instead of the X-XSS-Protection. The good configuration should be:

**XSS-XSS-Protection:** 1; mode=block

And not DENY. This is used for the X-Frame Option.

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
