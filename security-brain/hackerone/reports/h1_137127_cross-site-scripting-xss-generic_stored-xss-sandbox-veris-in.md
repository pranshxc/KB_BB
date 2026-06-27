---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '137127'
original_report_id: '137127'
title: '[Stored XSS] sandbox.veris.in'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: veris
created_at: '2016-05-08T15:42:26.117Z'
disclosed_at: '2016-05-26T15:04:55.181Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [Stored XSS] sandbox.veris.in

## Metadata

- HackerOne Report ID: 137127
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: veris
- Disclosed At: 2016-05-26T15:04:55.181Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello I want to report you another xss... but it's stored 

Steps to reproduce it :

1 . First create a group .
2. Go to https://sandbox.veris.in/portal/members/ and add a member with name "><img src=x onerror=alert(1)> .
3.  Add this member in a group ( created in step 1 .. ) .
4. Go to https://sandbox.veris.in/portal/assets/ and create a badge  with 
Badge name -> "><img src=x onerror=alert(1)>
Badge description -> "><img src=x onerror=alert(1)>
Select organization 
- Add a new key :
Key display name -> "><img src=x onerror=alert(1)>
Editable by : User and organization 
Key type : Name
Input type : Text only 
Submit.
5. Go to members ( https://sandbox.veris.in/portal/members/ )  in Action click ,, Assign a new badge '' , select badge 

In key input write : "><img src=x onerror=alert(1)>

Submit.

Alert was executed , stored xss.

The xss appear cause when member name get a xss payload name.

Thank you

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
