---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '898841'
original_report_id: '898841'
title: Password reset link not expired at Stocky App
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2020-06-15T18:09:41.270Z'
disclosed_at: '2020-08-18T22:53:55.541Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: Shopify Developed Apps
asset_type: OTHER
max_severity: medium
tags:
- hackerone
- improper-access-control-generic
---

# Password reset link not expired at Stocky App

## Metadata

- HackerOne Report ID: 898841
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2020-08-18T22:53:55.541Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

You can use password reset link to reset password multiple times.

Steps:

1. Go to `https://stocky.shopifyapps.com/users/forgotten_password` and Send the password reset link to your email.
(if this page doesn't  appear you should add login details via this `https://stocky.shopifyapps.com/preferences/users` )
{F869115}
2. Go to your email inbox you see reset token like this `https://stocky.shopifyapps.com/users/new_password?reset_token=your-reset-token`and click the link to change password. you can use this link many times to reset password

## Impact

Password Reset Link not expiring after changing password

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
