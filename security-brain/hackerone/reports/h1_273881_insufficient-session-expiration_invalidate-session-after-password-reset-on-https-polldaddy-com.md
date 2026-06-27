---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '273881'
original_report_id: '273881'
title: Invalidate session after password reset on https://polldaddy.com
weakness: Insufficient Session Expiration
team_handle: automattic
created_at: '2017-10-02T21:36:04.609Z'
disclosed_at: '2017-11-09T13:11:40.371Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 11
tags:
- hackerone
- insufficient-session-expiration
---

# Invalidate session after password reset on https://polldaddy.com

## Metadata

- HackerOne Report ID: 273881
- Weakness: Insufficient Session Expiration
- Program: automattic
- Disclosed At: 2017-11-09T13:11:40.371Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi there,
I found broken session bug on your website.Your website is unable to validate the session.That may lead takeover victims account.

Reproduce:
1.Go to https://polldaddy.com and log into your account from two different browsers.
2.Now change password from any browser you already logged in
3.You will be still logged into another browser.

Kindly fix this issue.
Thx,

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
