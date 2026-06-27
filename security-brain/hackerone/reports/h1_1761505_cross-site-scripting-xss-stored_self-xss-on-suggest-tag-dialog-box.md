---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1761505'
original_report_id: '1761505'
title: Self-XSS on Suggest Tag dialog box
weakness: Cross-site Scripting (XSS) - Stored
team_handle: xvideos
created_at: '2022-11-03T18:18:34.825Z'
disclosed_at: '2022-11-08T19:19:44.120Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: www.xvideos.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Self-XSS on Suggest Tag dialog box

## Metadata

- HackerOne Report ID: 1761505
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: xvideos
- Disclosed At: 2022-11-08T19:19:44.120Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Stored cross-site scripting  arises when an application receives data from an untrusted source and includes that data within its later HTTP responses in an unsafe way.

vulnerable URL : https://www.xvideos.com/video57921571/friend_b._if_d.

Vulnerability Description : Application have a add tag functionality when i put java script like <script>alert(1)</script> after that stored XSS vulnerability arise.

Step to Reproduce : 
Step 1 : Go to following URL https://www.xvideos.com/video53284603/b.
Note : you don't need an account to do this
Step 2 : There is a add tag functionality insert the following information : <script>alert(1)</script>
Step 3 : Click the add button 
Step 4 : you will see a java script popup box showing your domain

Check the attached Video POC to see the actual XSS vulnerability

## Impact

If an attacker can control a script that is executed in the victim's browser, then they can typically fully compromise that user.
When the victim accesses the page containing the JavaScript payload, their browser will make a HTTP request to the attacker’s server

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
