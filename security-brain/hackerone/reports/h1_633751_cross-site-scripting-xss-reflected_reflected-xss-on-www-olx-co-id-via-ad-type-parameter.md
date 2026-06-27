---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '633751'
original_report_id: '633751'
title: Reflected XSS on www.olx.co.id via ad_type parameter
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: olx
created_at: '2019-07-02T11:10:17.142Z'
disclosed_at: '2019-11-03T18:33:06.881Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on www.olx.co.id via ad_type parameter

## Metadata

- HackerOne Report ID: 633751
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: olx
- Disclosed At: 2019-11-03T18:33:06.881Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I have identified a Reflected Cross Site Scripting (XSS) vulnerability on the www.olx.co.id website.

Vulnerable URL: https://www.olx.co.id/iklan/sony-xz-ram-3gb-32gb-finger-mulus-preisure-naik-test-air-disini-IDA2UED.html?ad_type=OR"/><script>alert("XSS")</script>

Vulnerable Parameter: skeyword

XSS Payload: OR"/><script>alert("XSS")</script>

Steps to replicate is fairly simple. Just access the URL and the JavaScript gets reflected in response and gets executed on the browser. The Popup screenshot attached.

Let me know if any further help is required from my side.

## Impact

An attacker can inject any arbitrary JavaScripts which can:
1. Redirect user to malicious website like phishing website etc.
2. Rewrite the content of the current HTML page whcuh can result in Brand Abuse.

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
