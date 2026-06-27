---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '583710'
original_report_id: '583710'
title: BUG XSS IN "ADD IMAGES"
weakness: Cross-site Scripting (XSS) - Stored
team_handle: imgur
created_at: '2019-05-17T17:53:33.282Z'
disclosed_at: '2019-07-18T16:44:48.075Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 18
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# BUG XSS IN "ADD IMAGES"

## Metadata

- HackerOne Report ID: 583710
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: imgur
- Disclosed At: 2019-07-18T16:44:48.075Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I want to report bug XSS in "ADD IMAGES" 

How To Produce it : 
1. Login to your Account
2. Then Add Images With XSS Payload In filename (example : "><img src=x onerror=prompt(document.domain)>.png)
3. Click on Image that you upload
4. in the name of picture XSS will fired

## Impact

https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)

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
