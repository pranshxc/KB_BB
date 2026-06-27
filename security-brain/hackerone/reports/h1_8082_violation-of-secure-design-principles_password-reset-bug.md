---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8082'
original_report_id: '8082'
title: Password Reset Bug
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2014-04-18T22:41:09.474Z'
disclosed_at: '2014-09-25T22:34:35.437Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- violation-of-secure-design-principles
---

# Password Reset Bug

## Metadata

- HackerOne Report ID: 8082
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2014-09-25T22:34:35.437Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Possible account takeover using the forgot password link even after the email address and password changed.

Steps to Reproduce
===================================

Create an account in hackerone E.g john@example.com
After account verification logout from the account
Reset the password for john@example.com where we get the password reset link but do not use this link.

Now login again and change the email from john@exmaple.com to teena@example.com .

A verification email will be sent to teena. After successful verification we can logout.

Now this hackerone.com account belongs to teena@example.com and now teena can change the password.

But at this point ( after password change ) all the password reset links generated before should no longer be valid but in hackerone its still valid

Now we can try using the forgot password reset link which we have kept in john@exmaple.com and see if we can take over the account.

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
