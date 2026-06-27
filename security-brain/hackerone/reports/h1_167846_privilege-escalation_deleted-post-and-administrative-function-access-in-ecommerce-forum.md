---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '167846'
original_report_id: '167846'
title: Deleted Post and Administrative Function Access in eCommerce Forum
weakness: Privilege Escalation
team_handle: shopify
created_at: '2016-09-12T20:55:07.923Z'
disclosed_at: '2016-10-05T21:10:10.797Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- privilege-escalation
---

# Deleted Post and Administrative Function Access in eCommerce Forum

## Metadata

- HackerOne Report ID: 167846
- Weakness: Privilege Escalation
- Program: shopify
- Disclosed At: 2016-10-05T21:10:10.797Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I initially queried the following report as a comment in #165048, in which @juanbroullon confirmed the issue appeared valid and requested I open a new Shopify report.

A selection of privileged information is provided upon appending `/edit` to a user profile URL on the eCommerce forum (as an authenticated user).

As such, it appears that I am able to view the user's entire history of posts as an administrator, including those which have been deleted (possibly similar to the case of #135756):

## Proof of Concept URLs

* https://ecommerce.shopify.com/users/1/edit
* https://ecommerce.shopify.com/users/1/posts
* https://ecommerce.shopify.com/users/1/posts?filter=spam

Please let me know if you require any additional details regarding this.

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
