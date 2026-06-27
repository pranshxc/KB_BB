---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '54321'
original_report_id: '54321'
title: Xss in website's link
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-04-02T00:16:27.171Z'
disclosed_at: '2015-05-13T19:26:39.189Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Xss in website's link

## Metadata

- HackerOne Report ID: 54321
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-05-13T19:26:39.189Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found Xss in my website's link.

Steps:

Go to this page https://app.shopify.com/services/partners/account/edit
In fileld "Website (optional)" add javascript:alert(document.cookie);//http://dgddfgdfgg.ua
and save

Need registration https://experts.shopify.com/signup

After we can see account. Click link website

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
