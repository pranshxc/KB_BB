---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '892615'
original_report_id: '892615'
title: '[www.werkenbijbakertilly.nl] Denial of service due to incorrect server return
  can result in total denial of service.'
weakness: Uncontrolled Resource Consumption
team_handle: radancy
created_at: '2020-06-06T08:59:51.488Z'
disclosed_at: '2020-07-10T07:46:37.406Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 67
asset_identifier: www.werkenbijbakertilly.nl
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# [www.werkenbijbakertilly.nl] Denial of service due to incorrect server return can result in total denial of service.

## Metadata

- HackerOne Report ID: 892615
- Weakness: Uncontrolled Resource Consumption
- Program: radancy
- Disclosed At: 2020-07-10T07:46:37.406Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

###Summary
When sending too much data through file upload, the server returns an invalid 500 status code instead of the speed 429 status code, causing an internal denial of service.

###Description
I uploaded a file from the https://www.werkenbijbakertilly.nl/vacatures/solliciteer/senior-hr-consultant-317 page to test the speed limit, bypass, problem, and hit submit to start testing the speed limit did. As a result, while investigating the problem, we found an interesting bug. First, I found that if I send too many requests to the server, a slow response and an internal denial of service occur with 500 status codes instead of 429 status codes.

I knew that this would result in a real denial of service, and I immediately stopped testing. In addition, we found that when denial of service is activated through the 502 status code, some information is exposed. A report on the release of this information was rewritten by #892610.

###Environment
- Browser : Chrome Version 83.0.4103.56 (official build) beta (64-bit)
- Scope: Web Application
- Attack type: Denial of Service
- Maximum user privileges needed to reproduce your issue: no privileges
- Domain : https://www.werkenbijbakertilly.nl/vacatures/solliciteer/senior-hr-consultant-317
- Influence range : https://www.werkenbijbakertilly.nl

###Proof of Concept
██████

###Steps To Reproduce :
1. Go to the https://www.werkenbijbakertilly.nl/vacatures/solliciteer/senior-hr-consultant-317 Page.
2. Basically I need to upload a cv file when uploading the file. This is a normal cv file. Please upload this file ██████
3. Submit a form upload a file, and grap the packet.
4. Now we need to send too many requests to activate the 500 code.
5. Send a lot of data through Burp Suite -> Intruder function.
6. Now, when the 500th code is activated, the internal service denial occurs through the 502 status code.

###Recommendation
If you send too many requests, the server should not have code 500 activated. Reimplement to enable the 429 status code.

## Impact

Internal denial of service leads to total denial of service within the web service https://www.werkenbijbakertilly.nl.

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
