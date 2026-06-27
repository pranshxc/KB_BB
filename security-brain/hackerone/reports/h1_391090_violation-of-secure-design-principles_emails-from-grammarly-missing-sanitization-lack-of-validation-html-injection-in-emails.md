---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '391090'
original_report_id: '391090'
title: Emails from Grammarly missing sanitization(lack of validation?) -> HTML injection
  in emails
weakness: Violation of Secure Design Principles
team_handle: grammarly
created_at: '2018-09-03T21:06:28.515Z'
disclosed_at: '2019-04-30T06:09:22.333Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 20
asset_identifier: app.grammarly.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Emails from Grammarly missing sanitization(lack of validation?) -> HTML injection in emails

## Metadata

- HackerOne Report ID: 391090
- Weakness: Violation of Secure Design Principles
- Program: grammarly
- Disclosed At: 2019-04-30T06:09:22.333Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

**Summary:** 
Emails from Grammarly (e.g. "reset password" email) missing HTML sanitization. That leads to content spoofing in emails.

## Steps To Reproduce:

1. Go to "Profile"
2. Find reset password tab (if you're logged in using FB/Google, you won't see this menu)
3. Change email to something like: `user@mail.com` -> `user+<h1>2@mail.com`
4. Find the letter from Grammarly in your inbox, about password reset attempt.
5. `<h1>` tag is noticeable.

## Impact

Currently, the impact is miserable - content spoofing in "reset password" emails (sounds like a joke).
However, it's still a bad behavior. I guess that HTML injection through unsanitized/unvalidated input **could affect other Grammarly's email templates**.

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
