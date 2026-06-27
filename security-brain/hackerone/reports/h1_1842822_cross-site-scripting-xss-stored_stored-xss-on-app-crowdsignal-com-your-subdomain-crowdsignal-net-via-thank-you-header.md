---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1842822'
original_report_id: '1842822'
title: Stored XSS on app.crowdsignal.com  your-subdomain.crowdsignal.net via Thank
  You Header
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2023-01-22T00:03:41.154Z'
disclosed_at: '2023-02-24T10:33:03.068Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 32
asset_identifier: Crowdsignal
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on app.crowdsignal.com  your-subdomain.crowdsignal.net via Thank You Header

## Metadata

- HackerOne Report ID: 1842822
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2023-02-24T10:33:03.068Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hi, I hope you're having a good day.

I found an Stored XSS at app.crowdsignal.net.

## Platform(s) Affected:
app.crowdsignal.net

## Steps To Reproduce:

  1. Go to https://app.crowdsignal.com/dashboard and create a project
  1. Add any thing to the project and publish the project and intercept the request while publishing.
  1. Edit the Thank You Header with this payload `<a href='javascript:alert(document.domain);'>Click Me</a>`
  1. Open the Project you published and fill the form and click submit you will be redirected to thank you page click at the button and the XSS will fired.

## Supporting Material/References:

████████

## Impact

Stored XSS

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
