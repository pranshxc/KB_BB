---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '411337'
original_report_id: '411337'
title: Forget password link not expiring after email change.
weakness: Improper Authorization
team_handle: chaturbate
created_at: '2018-09-19T05:13:33.396Z'
disclosed_at: '2018-09-20T06:42:43.088Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authorization
---

# Forget password link not expiring after email change.

## Metadata

- HackerOne Report ID: 411337
- Weakness: Improper Authorization
- Program: chaturbate
- Disclosed At: 2018-09-20T06:42:43.088Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I found a token miss configuration flaw in chaturbate.com, When we reset password for a user a link is sent to the registered email address but incase it remain unused and email is updated by user from setting panel then too that old token [reset link] sent at old email address remains valid.

#A better explanation

1- User use reset feature to get reset link [Email : etc@x.com]
2- User came to know about his old password so remain the link unused and the token not expires 
3- Now User changes his email from control panel [New email : etc11@z.com]
4- But the old reset still remains valid after email change

In-case an attacker able to get access to user's old email account he can hack his chaturbate account too via that link, so expiring the token at email change will be a better practice

## Impact

The attacker can still change the password if victim thinks his/her account is compromised and decided to chnage his email

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
