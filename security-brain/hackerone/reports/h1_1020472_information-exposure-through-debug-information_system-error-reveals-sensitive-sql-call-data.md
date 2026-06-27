---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1020472'
original_report_id: '1020472'
title: System Error Reveals Sensitive SQL Call Data
weakness: Information Exposure Through Debug Information
team_handle: deptofdefense
created_at: '2020-10-28T05:17:19.723Z'
disclosed_at: '2021-01-12T21:50:38.950Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-exposure-through-debug-information
---

# System Error Reveals Sensitive SQL Call Data

## Metadata

- HackerOne Report ID: 1020472
- Weakness: Information Exposure Through Debug Information
- Program: deptofdefense
- Disclosed At: 2021-01-12T21:50:38.950Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
If you attempt to login at https://███.mil/sso/LoginRequest.do using a very long username, the application will respond showing a stack trace information with sensitive SQL data call information. This reveals too much information about SQL calls to the database. Please see the attached PoC video. 

**Description:**
Login at https://██████████.mil/sso/LoginRequest.do using a very long username and the application will respond showing a stack trace information with sensitive SQL data call information.

## Step-by-step Reproduction Instructions

(1) Go to https://██████.mil/sso/LoginRequest.do
(2) Enter in any username and password and Intercept the request with Burp Suite.
(3) Generate a long string of characters such as 100,000 characters and enter that into the "username" field  and send the request. 
(4) Observe the stack trace error and observe the following information below showing sensitive SQL data:
Internal Exception: java.sql.SQLException: ORA-01460: unimplemented or unreasonable conversion requested
Error Code: 1460
██████████

████████

█████████

## Suggested Mitigation/Remediation Actions:
Remove any mention of the SQL database calls in the stack trace error. 

##References:
https://owasp.org/www-community/Improper_Error_Handling

## Impact

Attacker can use the error messages to gain further knowledge of the SQL system to launch future attacks.

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
