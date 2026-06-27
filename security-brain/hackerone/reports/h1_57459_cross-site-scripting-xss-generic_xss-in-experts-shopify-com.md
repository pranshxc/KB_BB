---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '57459'
original_report_id: '57459'
title: XSS in experts.shopify.com
weakness: Cross-site Scripting (XSS) - Generic
team_handle: shopify
created_at: '2015-04-20T12:56:43.159Z'
disclosed_at: '2015-05-19T18:46:17.280Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in experts.shopify.com

## Metadata

- HackerOne Report ID: 57459
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: shopify
- Disclosed At: 2015-05-19T18:46:17.280Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
XSS vulnerability in experts.shopify.com,

Steps to verify:
1. Go  to https://experts.shopify.com
2. Sign up for an `expert`. (Please do note that you must create a new account if you already have, do not use existing account or an account that did not yet apply for an expert) then you will ask to login.
3. Fill up the necessary fields and upload photos.
4. Under `Portfolio Images` put `"><img src=x onerror=alert(document.domain)>` in the `caption` field.
5. Now hit `Save`, you will be redirected to page like this ( http://postimg.org/image/glodr1wj3/ )
6. Click one of the photos where the caption is `"><img src=x onerror=alert(document.domain)>`. XSS now executes.

Proof of concept: http://postimg.org/image/7jrwwaywn/

Please let me know if you need more information about this.

Regards,
Mr. Poo Gay

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
