---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1601140'
original_report_id: '1601140'
title: reflected XSS on panther.com
weakness: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic
  XSS)
team_handle: panther_labs
created_at: '2022-06-15T00:40:21.381Z'
disclosed_at: '2022-07-23T05:19:50.943Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 62
asset_identifier: '*.runpanther.io'
asset_type: WILDCARD
max_severity: high
tags:
- hackerone
- improper-neutralization-of-script-related-html-tags-in-a-web-page-basic-xss
---

# reflected XSS on panther.com

## Metadata

- HackerOne Report ID: 1601140
- Weakness: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)
- Program: panther_labs
- Disclosed At: 2022-07-23T05:19:50.943Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
When visiting  runpanther.io I got redirected to panther.com and the application failed to sanitise user's input resulting into HTML injection and possible XSS.

## Steps To Reproduce:

{F1774502}
  1. Go to https://panther.com/search/Users%3Ch1%3EHello,%20I%20am%3C/h1%3E%3Cfont%20color=red%3E%20Ibrahimatix0x01%3C/font%3E
  1. You will notice that HTML codes in the search form are executed by the browser.
  

## Supporting Material/References:
{F1774497}

## Impact

The vulnerability allow a malicious user to inject html tags and could possibly execute Javascript (if WAF is successfully bypassed)which could lead to steal user's session

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
