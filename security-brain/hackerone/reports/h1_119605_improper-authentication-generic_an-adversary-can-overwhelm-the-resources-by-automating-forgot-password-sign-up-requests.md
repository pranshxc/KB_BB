---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '119605'
original_report_id: '119605'
title: An adversary can overwhelm the resources by automating Forgot password/Sign
  Up requests
weakness: Improper Authentication - Generic
team_handle: coinbase
created_at: '2016-03-01T01:27:39.001Z'
disclosed_at: '2016-07-24T03:40:20.949Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
tags:
- hackerone
- improper-authentication-generic
---

# An adversary can overwhelm the resources by automating Forgot password/Sign Up requests

## Metadata

- HackerOne Report ID: 119605
- Weakness: Improper Authentication - Generic
- Program: coinbase
- Disclosed At: 2016-07-24T03:40:20.949Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

As Coinbase doesn't use CAPTCHA on publicly available forms such as 'Forgot Password' & 'Sign Up' , the requests can be automated to overwhelm the resources to result in denial of service for CoinBase or mail flooding of customers.

The steps to reproduce the issue are as follows.

Step 1: Browse to https://www.coinbase.com/password_resets/new
Step 2: Enter a valid user email ID and click on Reset Password
Step 3: Capture the request in burp and send the request to repeater. Repeat the request several times.
Step 4: Open the mail client and check the inbox. It can be observed that the several password reset emails are present in the inbox.

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
