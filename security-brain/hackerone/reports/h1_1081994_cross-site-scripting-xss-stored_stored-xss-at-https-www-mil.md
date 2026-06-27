---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1081994'
original_report_id: '1081994'
title: Stored XSS at https://www.█████████.mil
weakness: Cross-site Scripting (XSS) - Stored
team_handle: deptofdefense
created_at: '2021-01-20T00:34:36.021Z'
disclosed_at: '2021-02-01T17:48:48.502Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS at https://www.█████████.mil

## Metadata

- HackerOne Report ID: 1081994
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: deptofdefense
- Disclosed At: 2021-02-01T17:48:48.502Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Stored XSS exists at https://www.██████.mil. A user can fill out the form and upload a file containing javascript code to trigger XSS. 

**Description:**
Stored XSS exists at https://www.████.mil. A user can fill out the form and upload a file containing javascript code to trigger XSS. 


## Impact
A user can steal cookies, deface a site, etc. 

## Step-by-step Reproduction Instructions

(1) Go to https://www.██████.mil/jppso/vendor/WFDPMMiscInvoicingDocuments.aspx
(2) Fill out the form, upload a file, and add the file
(3) Once the file is uploaded right click to get to the Developer Tools.
(4) Inspect the page and find the path for the file -- █████\file.txt. For example, the file path for the file I uploaded is as follows: https://www.██████.mil/jppso/vendor/Data/cme1rjjcnjhnvdzhf5lgfbge-01192021-065856_testing-new.html
(5) Observe that XSS is triggered.

## Product, Version, and Configuration (If applicable)
https://www.████████.mil
Tested in Firefox

## Suggested Mitigation/Remediation Actions

## Impact

Stored XSS exists at https://www.█████.mil. A user can fill out the form and upload a file containing javascript code to trigger XSS.

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
