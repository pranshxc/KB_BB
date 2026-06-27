---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '55891'
original_report_id: '55891'
title: Self-XSS in Partners Profile
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-06-17T04:41:41.950Z'
disclosed_at: '2016-07-07T23:12:07.513Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Self-XSS in Partners Profile

## Metadata

- HackerOne Report ID: 55891
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-07-07T23:12:07.513Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Hi , I have found an XSS stored vulnerability in the page paterns uber profile edit. the vulnerability in the vat number. Steps to reproduce:
1. Login to partners.uber.com
2. Go to a page https://partners.uber.com/profile/
3. In the vat number enter a payload xss :  "><img src=x onerror=alert(0)> "><img src=x onerror=alert(0)> <script>alert(0)</script>
4. save

thank you, please tell me if the bug has been fixed.

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
