---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '737042'
original_report_id: '737042'
title: Password token leak via Host header
weakness: Violation of Secure Design Principles
team_handle: stripo
created_at: '2019-11-13T18:56:19.002Z'
disclosed_at: '2019-12-19T13:01:38.710Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: my.stripo.email
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Password token leak via Host header

## Metadata

- HackerOne Report ID: 737042
- Weakness: Violation of Secure Design Principles
- Program: stripo
- Disclosed At: 2019-12-19T13:01:38.710Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Password token leak via Host header
--------------

##Vulnerability Description:
Token will be leaked by the Server to that third party site and that token can be used by third parties to reset the password and take over the account & directly login in your account

##Steps To Reproduce:

1) Send reset password link to your email address.
2)Now go to email, turn burp suite intercept on and click on reset password link. Check for the requests having the token in referrer and host as third party website. And copy the link
3)Now turn intercept off and reset the password.(with that link)
4)Now reset the password.

#POC:
Images Uploaded

## Impact

#Impact

It allows the person who has control of particular site to change the user's password (CSRF attack), because this person knows reset password token of the user.

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
