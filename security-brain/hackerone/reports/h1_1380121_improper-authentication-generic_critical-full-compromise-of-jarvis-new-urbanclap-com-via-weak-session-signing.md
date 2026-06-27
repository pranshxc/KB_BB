---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1380121'
original_report_id: '1380121'
title: Critical full compromise of jarvis-new.urbanclap.com via weak session signing
weakness: Improper Authentication - Generic
team_handle: urbancompany
created_at: '2021-10-25T11:50:21.513Z'
disclosed_at: '2022-01-30T20:03:00.574Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 120
asset_identifier: www.urbancompany.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Critical full compromise of jarvis-new.urbanclap.com via weak session signing

## Metadata

- HackerOne Report ID: 1380121
- Weakness: Improper Authentication - Generic
- Program: urbancompany
- Disclosed At: 2022-01-30T20:03:00.574Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
Hi there, I discovered that jarvis-new.urbanclap.com uses a weak Flask session key. Because Flask sessions are signed with a static secret, if this secret is known to an attacker then they can modify the session state. In this case, we can modify the Redash `user_id` for the session and log in as any user. **This results in a full compromise of the instance.** I have attached a screenshot showing that I logged into `█████████@urbancompany.com` and have full admin permissions:

██████████
████
██████████
███████

## How to fix
Change the `REDASH_COOKIE_SECRET` and `REDASH_SECRET_KEY` to a random value immediately.

## PoC
For simplicity, it is easiest to forge a password reset link for Redash. We can do this with a bit of Python. To get the reset link for user ID 1, we simply run:
```
>>> from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
>>> serializer = URLSafeTimedSerializer("███")
>>> serializer.dumps(str("1"))
'███'
```

Then, we can browse to `https://jarvis-new.urbanclap.com/reset/█████` and choose a new password for user ID 1. This then logs us into their account.

## Impact

Since this is connected to all of your databases, this is likely a significant leak of PII and other sensitive information. This is easily a critical issue.

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
