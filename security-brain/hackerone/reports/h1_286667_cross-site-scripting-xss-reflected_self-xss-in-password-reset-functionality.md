---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '286667'
original_report_id: '286667'
title: Self-XSS in password reset functionality
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: shopify
created_at: '2017-11-02T19:56:43.657Z'
disclosed_at: '2017-11-10T14:26:02.755Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 29
asset_identifier: accounts.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Self-XSS in password reset functionality

## Metadata

- HackerOne Report ID: 286667
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: shopify
- Disclosed At: 2017-11-10T14:26:02.755Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
When I opened this domain of yours,
https://accounts.shopify.com/password-reset/new

I just put the following text into email address box,
<h1 style="color:blue;">█████</h1>
it change the colour of the text.

Well my point here is that if you could inject HTML, you might be able to add a <form> tag
to the page.
I also upload the picture as a proof.

Peace.

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
