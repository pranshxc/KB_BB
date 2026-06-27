---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '151827'
original_report_id: '151827'
title: The contribution save option seem to be vulnerable to CSRF
weakness: Cross-Site Request Forgery (CSRF)
team_handle: gratipay
created_at: '2016-07-16T21:57:46.306Z'
disclosed_at: '2016-07-17T15:14:38.881Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# The contribution save option seem to be vulnerable to CSRF

## Metadata

- HackerOne Report ID: 151827
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: gratipay
- Disclosed At: 2016-07-17T15:14:38.881Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

The application is vulnerable to Cross Site Request Forgery
====================

Description
---------------------
The option in the application to save weekly contribution for a project is vulnerable to Cross Site Request forgery. 
**Note:** I am unable to perform the action itself normally. But it is obvious that the application uses no protection against CSRF and the token named **csrf_token** is being passed in the cookie instead of a post parameter or HTTP header. 

Detailed Steps:
---------------------
**Step 1:** Open a project and modify the weekly contribution for the same. 
{F105367}
**Step 2:** Send the request to save the modified value.
{F105368}
**Step 3:** It can be observed that no kind of CSRF protection is employed and the request can be recreated in the following URL format. If anyone clicks on the link in a browser where they are already logged in to gratipay, the amount will be automatically updated.
https://gratipay.com/<project>/payment-instruction.json?amount=<amount>

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
