---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6884'
original_report_id: '6884'
title: Leaking Referrer in Reset Password Link
weakness: Violation of Secure Design Principles
team_handle: irccloud
created_at: '2014-04-10T21:46:26.360Z'
disclosed_at: '2014-04-12T03:46:10.370Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# Leaking Referrer in Reset Password Link

## Metadata

- HackerOne Report ID: 6884
- Weakness: Violation of Secure Design Principles
- Program: irccloud
- Disclosed At: 2014-04-12T03:46:10.370Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I have found that you are leaking via the referrer the reset password link. I am attaching the photo as proof of concept that the site is indeed leaking the reset password link via the referrer.

Thats when someone loads the reset password link and decided to click on external links.

Its the time the referrer is leak ( see attached photo )

Clifford Trigo

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
