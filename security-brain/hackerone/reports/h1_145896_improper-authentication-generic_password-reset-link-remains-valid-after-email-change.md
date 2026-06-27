---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145896'
original_report_id: '145896'
title: Password reset link remains valid after email change
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2016-06-19T17:40:12.035Z'
disclosed_at: '2016-12-13T16:12:16.461Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-authentication-generic
---

# Password reset link remains valid after email change

## Metadata

- HackerOne Report ID: 145896
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2016-12-13T16:12:16.461Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey!
I found a token miss configuration flaw in Nextcloud 9.0.50 [Latest version], When we reset password for a user a link is sent to the registered email address but incase it remain unused and email is updated by user from control panel then too that old token [reset link] sent at old email address remains valid.

A better explanation
-
1- User use reset feature to get reset link [Email : abc@x.com]
2- User came to know about his old password so remain the link unused and the token not expires 
3- Now User changes his email from control panel [New email : abcd@z.com]
4- But the old reset still remains valid after email change

In-case an attacker able to get access to user's old email account he can hack his Nextcloud account too via that link, so expiring the token at email change will be a better practice

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
