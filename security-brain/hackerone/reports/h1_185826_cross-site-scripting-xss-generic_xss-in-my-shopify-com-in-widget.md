---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '185826'
original_report_id: '185826'
title: XSS in my.shopify.com in  widget
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2016-11-27T14:52:43.172Z'
disclosed_at: '2017-07-21T15:20:57.540Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in my.shopify.com in  widget

## Metadata

- HackerOne Report ID: 185826
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2017-07-21T15:20:57.540Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi security team
I found XSS in the Buy Button in my.shopify.com


Step to reproduce 

1-Go to Product and create Product with these payload <img src="a" onerror="prompt(document.cookie)" />;
See (Step1)

2- Now Go to Embed on a website  and in the buy bouton page chose the third template and XSS will pop up 


Patch it

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
