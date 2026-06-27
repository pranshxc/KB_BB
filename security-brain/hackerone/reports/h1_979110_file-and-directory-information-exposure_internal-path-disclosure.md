---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '979110'
original_report_id: '979110'
title: Internal Path Disclosure
weakness: File and Directory Information Exposure
team_handle: cs_money
created_at: '2020-09-11T03:33:30.375Z'
disclosed_at: '2020-09-11T16:12:21.778Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: support.cs.money
asset_type: URL
max_severity: critical
tags:
- hackerone
- file-and-directory-information-exposure
---

# Internal Path Disclosure

## Metadata

- HackerOne Report ID: 979110
- Weakness: File and Directory Information Exposure
- Program: cs_money
- Disclosed At: 2020-09-11T16:12:21.778Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,
       I would like to report internal path disclosure in response. I was trying for Stored XSS but got no luck in that process. I observed the responses, one of the responses showing file path with 500 Internal Server Error. 

## Steps To Reproduce:

1. Go to cs.money and sign in through steam account.
2. Now click on chat support icon
3.  Now try to upload file while uploading capture the request in burp and send it to the repeater.
4.  Edit the request as shown in below. 

------------------------------------------------------------------------------------------------
Content-Disposition: form-data; name="file"; filename="/../../../../../.html"
Content-Type: image   text/html
Content-Type: text/html

-------------------------------------------------------------------------------------------------
 "5. After editing forward the request and observe the response.
   "6. Response is 500 Internal Server Error with these two path in the response.

## Supporting Material/References:
1. Image █████ shows edited part of the request.
2. Image █████ shows the response.
3. Image ███████ shows response in the browser.

## Impact

This issue is not a major threat to security, but this information usually contains sensitive information.

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
