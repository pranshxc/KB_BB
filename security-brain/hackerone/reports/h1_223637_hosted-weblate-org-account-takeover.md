---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223637'
original_report_id: '223637'
title: '[hosted.weblate.org]Account Takeover'
team_handle: weblate
created_at: '2017-04-25T03:23:39.968Z'
disclosed_at: '2017-05-17T14:09:10.628Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
---

# [hosted.weblate.org]Account Takeover

## Metadata

- HackerOne Report ID: 223637
- Weakness: 
- Program: weblate
- Disclosed At: 2017-05-17T14:09:10.628Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

**Steps to Reproduce:**

* Go to Login Page
* Reset Your Password by Clicking `Reset it`.
* Put your email and answer the captcha.
* Go to your email and click your reset Link.
* You dont need to Change Your Password because you'll be logged in.

**Scenario**
Victim forgot to logout his/her Email Account on a Cafe/Internet Renting Shops. The Attacker Click the Reset Password link and because that Improper InValidation of Session on Password Reset Links lies in there. Attacker can gain access to Victim's Account.

Let me know if you need more information.

Best Regards,

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
