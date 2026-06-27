---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '856981'
original_report_id: '856981'
title: CSRF - Modify Company Info
weakness: Cross-Site Request Forgery (CSRF)
team_handle: deptofdefense
created_at: '2020-04-23T09:27:13.686Z'
disclosed_at: '2020-06-11T18:18:12.359Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF - Modify Company Info

## Metadata

- HackerOne Report ID: 856981
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: deptofdefense
- Disclosed At: 2020-06-11T18:18:12.359Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Target Url**
███/services/user/manageAccountCompany

**Summary:**
Similar to███████, but on different endpoint. 
The application is missing CSRF Token on Editing company info endpoint. This lead to CSRF attack.

**Bypassing Content-Type**
The application is just accepting Content-Type as application/json.
This can be bypassed in several ways.
One of the ways is to Forge Content-Type header with flash. You need a flash file capable of sending cross-domain requests and a 307 redirector page.
For more info please see: https://blog.cm2.pw/forging-content-type-header-with-flash/

## Step-by-step Reproduction Instructions

1. Edit your company info and intercept its request.
2. Get the HTML code format from burp suite -> Engagement Tools -> Generate CSRF POC.
3. Click Test in Browser button, and on another browser/tab accessed by the victim account, paste the link.
4. Now hit on the button and intercept its request.
5. Modify the request header of Content-Type to: application/json.
6. Forward the request and CSRF exploited successfully and the info changed successfully.

## Suggested Mitigation/Remediation Actions
Add a csrf-token in the header or in an hidden input to check if the user that is doing this action authorized or not.

## Impact

This action is critical and sensitive. Attacker can upload this file to a url. Sends it to the victims. And when the authenticated victims navigate to the url their profile info will be modified.

**Regards.**

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
