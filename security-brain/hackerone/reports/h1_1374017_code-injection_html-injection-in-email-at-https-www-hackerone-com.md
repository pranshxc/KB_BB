---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1374017'
original_report_id: '1374017'
title: HTML injection in email at https://www.hackerone.com/
weakness: Code Injection
team_handle: security
created_at: '2021-10-19T08:59:22.662Z'
disclosed_at: '2023-05-12T10:24:53.039Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 36
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- code-injection
---

# HTML injection in email at https://www.hackerone.com/

## Metadata

- HackerOne Report ID: 1374017
- Weakness: Code Injection
- Program: security
- Disclosed At: 2023-05-12T10:24:53.039Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
By filling the firstname and last name with html tags at this form 
https://www.hackerone.com/hackers/pentest-community-application

It is possible to send email via hackerone and add custom html :)


**Description:**

### Steps To Reproduce

1. visit https://www.hackerone.com/hackers/pentest-community-application
2. in first name and last name add html tags ie firstname "><h1>anything etc. 
3. in email section add email of victim . 
4. submit the form 
5. check the email and see the html injected there 

### additional information: 
1.) please check the screenshot to see both the emails ie 1 without payload and one with payload 


### Optional: Your Environment (Browser version, Device, etc)

 * 

### Optional: Supporting Material/References (Screenshots)

 *

## Impact

An attacker can send malicious emails from hackerone , inject html in the email :) 
we all know where it leads to .

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
