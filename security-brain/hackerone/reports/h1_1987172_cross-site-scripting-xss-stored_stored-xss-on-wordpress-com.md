---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1987172'
original_report_id: '1987172'
title: Stored XSS on  wordpress.com
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2023-05-14T00:48:58.281Z'
disclosed_at: '2023-05-19T14:08:50.342Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
asset_identifier: wordpress.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on  wordpress.com

## Metadata

- HackerOne Report ID: 1987172
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2023-05-19T14:08:50.342Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Hi team

I found Stored XSS in wordpress.com via  app.crowdsignal.com


## Platform(s) Affected:
 wordpress.com

## Steps To Reproduce:
1 . Go to https://app.crowdsignal.com/dashboard and create a poll
2 . Put the payload as answer <img src=x onerror=alert(document.cookie)>
3.  Go to Share Your Poll and Copy  the Website Popup
4.Go to https://wordpress.com/posts add new post
5. App Website Popup 
6. Save it
7.Open the page and the XSS will fired

█████████

## Impact

The attacker can use this issue to execute malicious script code in the victim user browser also redirect the victim user to malicious sites

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
