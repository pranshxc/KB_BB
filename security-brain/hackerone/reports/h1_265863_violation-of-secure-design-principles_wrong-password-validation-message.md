---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '265863'
original_report_id: '265863'
title: Wrong password validation message
weakness: Violation of Secure Design Principles
team_handle: legalrobot
created_at: '2017-09-04T18:46:45.641Z'
disclosed_at: '2017-10-04T20:44:54.742Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: app.legalrobot-test.com
asset_type: URL
max_severity: none
tags:
- hackerone
- violation-of-secure-design-principles
---

# Wrong password validation message

## Metadata

- HackerOne Report ID: 265863
- Weakness: Violation of Secure Design Principles
- Program: legalrobot
- Disclosed At: 2017-10-04T20:44:54.742Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

Your password validation message seems to be contradicting with the server side validation of password field during new account sign up at `https://app.legalrobot.com/sign-in`.

When you start typing in password field, it says `Passwords must be more than 8 characters` but when you type more than 8 characters with valid combinations of letters, numbers, symbols etc, still it doesn't validate properly and it says, `Please fix this field.` even when  complexity is fair enough.

When you type in 11 characters, then only it takes password as valid.

I think you should either change the message or validate the password field properly.

Also, same problem when login !

Thanks
Ashish

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
