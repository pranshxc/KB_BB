---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '108645'
original_report_id: '108645'
title: Harden resend throttling
weakness: Violation of Secure Design Principles
team_handle: gratipay
created_at: '2016-01-06T01:39:03.525Z'
disclosed_at: '2017-04-16T17:42:44.511Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Harden resend throttling

## Metadata

- HackerOne Report ID: 108645
- Weakness: Violation of Secure Design Principles
- Program: gratipay
- Disclosed At: 2017-04-16T17:42:44.511Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Over in #87531, we're about to roll out a protection against using our "resend email verification" feature to mail-bomb a third party. However, chad+foo@zetaweb.com and chad+bar@zetaweb.com are not unlikely to fold down to the same address. In order to close that loophole, I suppose we'd need to either implement email address parsing—but what folding rules are we going to observer?—or throttle based on the authenticated user and not the `to` field, as @rohitpaulk suggested over on #87531 for other reasons.

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
