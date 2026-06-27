---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '265749'
original_report_id: '265749'
title: Bypass email verification when register new account
team_handle: legalrobot
created_at: '2017-09-04T09:35:10.047Z'
disclosed_at: '2017-09-04T21:40:40.107Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
asset_identifier: app.legalrobot-test.com
asset_type: URL
max_severity: none
tags:
- hackerone
---

# Bypass email verification when register new account

## Metadata

- HackerOne Report ID: 265749
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-09-04T21:40:40.107Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hi Legalrobot,

I have found a way to ignore Activate your account in my mailbox.
Here is my new acc: masterdzung@gmail.com and the activate link:
https://app.legalrobot-uat.com/email-verify?v=1Y5wiWwcvGcxznjlUsO-TuyEZgFpVbxMmQdfpEKrVTp

I never click on that link and i can still log in at app.legalrobot-uat.com

Here are steps to do:
1 - Register new account, you will get email to verify your email address
2 - Go to https://app.legalrobot-uat.com/sign-in, using Forgot password function
3 - Check your mailbox and you will get the link https://app.legalrobot-uat.com/password-reset/token?v=cFJ4kQuAfBFLqVmtyxuxxbNeudzpm4hZHwTDPcUNZd0
4 - After you changed new password. You can able to login your account without verified your email first

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
