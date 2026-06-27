---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '156542'
original_report_id: '156542'
title: Avoid "resend verification email" confusion
weakness: Cross-Site Request Forgery (CSRF)
team_handle: gratipay
created_at: '2016-08-04T17:04:33.865Z'
disclosed_at: '2017-03-20T17:07:44.516Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Avoid "resend verification email" confusion

## Metadata

- HackerOne Report ID: 156542
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: gratipay
- Disclosed At: 2017-03-20T17:07:44.516Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Let's assume Alice has a Gratipay account https://gratipay.com/~alice and an alice@foo.com email

1. Mallory creates an a‎**1**‎ice@foo\.com email address, base64-encodes it, and sends Alice a link https://gratipay.com/~alice/emails/verify.html?email2=YTFpY2VAZm9vLmNvbQ~~&nonce=x
2. When Alice opens the link, she sees a notification "The verification code for a1ice@foo.com is bad. Resend verification email"
3. If she clicks the "Resend verification email" button, that fake a‎**1**‎ice@foo\.com email will be automatically associated with her account, and a valid verification link will be sent there.
4. Mallory opens her a‎**1**‎ice@foo\.com inbox, gets the verification link, and sends it to Alice.
5. After Alice opens it, the email will be successfully verified, so Mallory will receive all Alice's notifications.

**The way to fix:**

You shouldn't give Alice a chance to accidentally add any emails to her account, without knowing that: on step 3 a verification link should be sent only if the email is already associated with the Alice's account. If no, there should be just an error message with no "Resend verification email" button.

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
