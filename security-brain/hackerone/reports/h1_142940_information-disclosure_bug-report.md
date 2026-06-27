---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '142940'
original_report_id: '142940'
title: Bug Report
weakness: Information Disclosure
team_handle: drchrono
created_at: '2016-06-03T21:22:22.732Z'
disclosed_at: '2016-07-19T00:45:23.417Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Bug Report

## Metadata

- HackerOne Report ID: 142940
- Weakness: Information Disclosure
- Program: drchrono
- Disclosed At: 2016-07-19T00:45:23.417Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Sir,

I want to report a bug in your web which i have found in few minutes ago :)

I have registered In your website and i have found a upload option i want to upload some php files but its saying only .pdf file allowed so i have just change my (.php) file extension to (.pdf) first its saying not allowed its not a pdf file or file is corrupted... But when i try to upload it using post data i have successfully uploaded corrupted file 

here is my proof:
 
https://85aa27de34e32ac9f9e0-e519cb8a62f48aa14df288cdc83ab719.ssl.cf5.rackcdn.com/hipaa_forms/2016/06/b193e25b-3218-4a09-8b09-b17bea6d5a18.pdf

its a php shell 

if a attacker can change the value and successfully upload .php file using http request it can be risk for your webserver :)


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
