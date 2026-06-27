---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '131108'
original_report_id: '131108'
title: Akismet Several CSRF vulnerabilities
weakness: Cross-Site Request Forgery (CSRF)
team_handle: automattic
created_at: '2016-04-15T14:04:26.657Z'
disclosed_at: '2016-05-28T09:32:37.360Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Akismet Several CSRF vulnerabilities

## Metadata

- HackerOne Report ID: 131108
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: automattic
- Disclosed At: 2016-05-28T09:32:37.360Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Summary
-----------

Akismet is vulnerable to CSRF allowing an attacker to cancel accounts of victims, add sites, remove subscriptions, etc.


Steps to reproduce *Account cancelation*
-----------

1. Login to your Akismet account, which has a subscription activated.
2. The following POST request will cancel the subscription and the account:

    `https://akismet.com/api/account/1/cancel`

The `1` can be replaced with any number. The userid was originally there, but I noticed that it actually just gets ignored.


Steps to reproduce other CSRF
--------------------
Basically all actions on Akismet are vulnerable to CSRF. Here are some further examples (`1` can be replaced with 2, 3, etc):

### Adding a site to a subscription:

```
POST /api/activation/create

subscriptionId=1&site_url=foo.bar
```
*foo.bar* is now added to subscription *1*

### Cancel specific subscription:

```POST /api/subscription/1/cancel```
   
Subscription *1* is now canceled.

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
