---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '229619'
original_report_id: '229619'
title: Ability to verify any email address you don't own - accounts.shopify.com
weakness: Violation of Secure Design Principles
team_handle: shopify
created_at: '2017-05-18T13:26:49.722Z'
disclosed_at: '2019-11-08T11:03:38.432Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 73
tags:
- hackerone
- violation-of-secure-design-principles
---

# Ability to verify any email address you don't own - accounts.shopify.com

## Metadata

- HackerOne Report ID: 229619
- Weakness: Violation of Secure Design Principles
- Program: shopify
- Disclosed At: 2019-11-08T11:03:38.432Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary: 
During testing it's been found that in `accounts.shopify.com` it's possible to change your email address to any email address that you don't own and confirm that email due to the confirmation token being leaked.

## Steps to reproduce: 
1. Login to `https://accounts.shopify.com/account`
2. Click **Change** Next to email
3. Enter any new email address
4. You'll see a message saying:
 
```
Verification email sent
We sent you an email to verify that you own "email@example.com". We'll change your email once you verify that you own it.
```
with a link to resend the verification email or cancel the change.
5.- Copy the resend link, it will look like this: `https://accounts.shopify.com/email-change/<Confirmation-TOKEN>/resend`
6.- Go to `https://accounts.shopify.com/email-change/<Confirmation-TOKEN>/` and the email will be verified even though you don't own it.

Thanks!

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
