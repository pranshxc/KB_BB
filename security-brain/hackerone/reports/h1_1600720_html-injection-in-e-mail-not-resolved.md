---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1600720'
original_report_id: '1600720'
title: HTML Injection in E-mail Not Resolved ()
team_handle: acronis
created_at: '2022-06-14T17:22:20.169Z'
disclosed_at: '2022-07-19T09:11:30.236Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 23
asset_identifier: '*.acronis.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# HTML Injection in E-mail Not Resolved ()

## Metadata

- HackerOne Report ID: 1600720
- Weakness: 
- Program: acronis
- Disclosed At: 2022-07-19T09:11:30.236Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary
On this report  " https://hackerone.com/reports/1536899  "  You closed the report and changed the status to Resolved.
But it's Not Resolved The Bug  It's Still there 

## Steps To Reproduce

    1.Please register at https://www.acronis.com/en-us/products/cyber-protect/trial/#registration with the victim's email.
    2. Inject "First Name" field with HTML tags, for example:    "/><img src="x"><a href="https://evil.com">login</a>.
    3.Check the email inbox, HTML tags will be executed. "Your Acronis Cyber Protect trial starts today!" 

Proof of Concept: 
                                         F1774045

## Impact

HTML injection into emails is dangerous!

* Your users are at risk when a hacker is able to take control of the emails that your applications send, but what's especially dangerous is that the emails       will be coming from your company email address.

*  When a malicious email comes from your company email, it looks a lot more legitimate.

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
