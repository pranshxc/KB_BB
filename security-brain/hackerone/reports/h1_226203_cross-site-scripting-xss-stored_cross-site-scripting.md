---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '226203'
original_report_id: '226203'
title: Cross-site-Scripting
weakness: Cross-site Scripting (XSS) - Stored
team_handle: paragonie
created_at: '2017-05-04T21:39:30.322Z'
disclosed_at: '2017-05-05T20:50:29.077Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Cross-site-Scripting

## Metadata

- HackerOne Report ID: 226203
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: paragonie
- Disclosed At: 2017-05-05T20:50:29.077Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

step:
1: goto https://bridge.cspr.ng/my/account of your account
2. in "Custom Profile field option" check the box and enter xss payload in "display name" field
       payload: "p<script>alert('xss')</script>"
3. update the information 
4. open the account in INTERNET EXPLORER 11 and xss will executed

note: here server is not sanitize the user input properly,
         payload will not work in firefox,chrome browser due to "content-security-policy"
         But internet explorer does not Support "Content-Security-Policy"  so xss will execut

this is stored xss and the display name will visible to everywhere, so its possible to account takeover of ther user

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
