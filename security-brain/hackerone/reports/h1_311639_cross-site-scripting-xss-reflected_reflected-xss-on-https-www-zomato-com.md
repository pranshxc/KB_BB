---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '311639'
original_report_id: '311639'
title: Reflected XSS on https://www.zomato.com
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: zomato
created_at: '2018-02-02T12:39:58.735Z'
disclosed_at: '2018-04-07T07:07:31.208Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on https://www.zomato.com

## Metadata

- HackerOne Report ID: 311639
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: zomato
- Disclosed At: 2018-04-07T07:07:31.208Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,

I found an XSS issue due to the incorrect handling of the \ character in a <script> context, the following link works as a PoC that alerts the location of the document:

https://www.zomato.com/googleOAuth2Callback?)}(alert)(location);{%3C!--&state=\

The issue exists because, given that the \ character supplied as the `state` parameter value is not well escaped and reflected into the page, we are able to use it to escape the " and then inject our own JS code to execute it on the page.

Note: This only works when the page is opened by an authenticated user

## Impact

This allows an attacker to inject custom Javascript codes that can be used to steal information from Zomato's user base and lure them to malicious websites on the internet on behalf of Zomato's website.

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
