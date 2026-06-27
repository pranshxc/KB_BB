---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '775560'
original_report_id: '775560'
title: Testing for arbitrary HTTP methods
weakness: Information Exposure Through an Error Message
team_handle: drive_net_inc
created_at: '2020-01-15T14:42:39.337Z'
disclosed_at: '2020-07-06T12:11:05.320Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
asset_identifier: www.drive2.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-exposure-through-an-error-message
---

# Testing for arbitrary HTTP methods

## Metadata

- HackerOne Report ID: 775560
- Weakness: Information Exposure Through an Error Message
- Program: drive_net_inc
- Disclosed At: 2020-07-06T12:11:05.320Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Test for allowed HTTP methods on the server. Below are the steps to reproduce it.
Step 1. Navigate the url
Step 2. Intercept the GET http request using burp suite 
Step 3. change GET to ABCD as shown in screenshot and forward this request to server
Step 4. Observe the http response from the server, it shows Allow header and http methods enabled on the server

## Impact

There seems to be no major impact If the tester gets a "405 Method not allowed" or "501 Method Unimplemented", but the target application showing what methods are allowed on the server. here in this case there are PUT and DELETE methods are shown. Using this methods attacker can use exploits to get server access or file upload using PUT method.

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
