---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '419017'
original_report_id: '419017'
title: SQL Injection in ████
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2018-10-04T14:39:44.321Z'
disclosed_at: '2019-08-19T12:22:02.251Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 71
tags:
- hackerone
- sql-injection
---

# SQL Injection in ████

## Metadata

- HackerOne Report ID: 419017
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2019-08-19T12:22:02.251Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

There is an SQL injection vulnerability in the SSN field at https://██████████/████/candidate_app/status_scholarship.aspx

## Impact

An attacker could use this vulnerability to control the content in the database, exfiltrate information, and potentially obtain remote code execution.

## Step-by-step Reproduction Instructions

Follow these steps:
1. Visit https://███/███/candidate_app/status_scholarship.aspx
2. Right click on the SSN field, click Inspect Element, and edit `maxlength="9"` by changing it to `maxlength="9999"` (or something similar, so that a longer payload can be put in)
3. Choose a random birth date, for example, January 1, 1990.
4. Enter in your SQL injection payload into the SSN field. For example, try `' OR '1'='1`.
5. Click "Check Status". Your SQLi payload will execute. If you did the example payload in step 4, assuming someone has the birth date you entered, it will log in as them and check their scholarship status.

Also, I didn't do much testing, but I think the birth date is also vulnerable to SQL injection. After sending the request, in the network tab, Edit and Resend Request after changing the birth day, month, or year to a payload that will cause invalid syntax like `'`. It will give you an HTTP 500 response. If you do a payload that won't cause invalid syntax like `''`, it will give you an HTTP 200.

## Suggested Mitigation/Remediation Actions
Sanitize everything (use prepared statements) and validate the data.

## Impact

An attacker could use this vulnerability to control the content in the database, exfiltrate information, and potentially obtain remote code execution.

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
