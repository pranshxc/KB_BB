---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '4808'
original_report_id: '4808'
title: /index.php/dashboard/sitemap/explore/ Cross-site scripting
weakness: Cross-site Scripting (XSS) - Generic
team_handle: concretecms
created_at: '2014-03-26T02:11:09.748Z'
disclosed_at: '2014-06-09T18:27:14.794Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# /index.php/dashboard/sitemap/explore/ Cross-site scripting

## Metadata

- HackerOne Report ID: 4808
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: concretecms
- Disclosed At: 2014-06-09T18:27:14.794Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

When you go to /index.php/dashboard/sitemap/explore/ and press on blog (I had standing Blog there) and then on properties -> Custom Attributes -> tags and insert "><img src=x onerror=alert(4)> a XSS will popup.

Some screens are in the attachment.

Best regards,

Olivier Beg

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
