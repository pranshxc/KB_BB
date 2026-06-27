---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '220009'
original_report_id: '220009'
title: Lack of input sanitization in Marketo form leads to execution of HTML in lead
  emails
weakness: Server-Side Request Forgery (SSRF)
team_handle: security
created_at: '2017-04-10T18:01:11.363Z'
disclosed_at: '2017-10-03T17:35:47.477Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Lack of input sanitization in Marketo form leads to execution of HTML in lead emails

## Metadata

- HackerOne Report ID: 220009
- Weakness: Server-Side Request Forgery (SSRF)
- Program: security
- Disclosed At: 2017-10-03T17:35:47.477Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
There is SSRF vulnerability due to img tag injection in "Contact HackerOne Sales" form. Since vulnerability triggers after 18-20 minutes so I am not sure which site it affects. It might affect hackerone or marketo. So I thought it would be better to report it first on hackerone. 

**POC**

1. Navigate to https://www.hackerone.com/product/features.
2. Click on "Get Started".
3. Fill FirstName, LastName, Company and Message by <img src=https://yourserver.com/f onerror=alert(1)>, <img src=https://yourserver.com/l onerror=alert(1)>, <img src=https://yourserver.com/c onerror=alert(1)> and <img src=https://yourserver.com/m onerror=alert(1)>.
4. Fill the remaining details and submit the form.
5. Wait 18-20 minutes and check server logs.

In this case ssrf triggers many times. Please check the screenshots.

Thanks

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
