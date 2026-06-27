---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1272095'
original_report_id: '1272095'
title: System Error Reveals  SQL Information
weakness: Information Exposure Through Debug Information
team_handle: deptofdefense
created_at: '2021-07-21T12:57:40.118Z'
disclosed_at: '2021-09-09T19:59:23.377Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-exposure-through-debug-information
---

# System Error Reveals  SQL Information

## Metadata

- HackerOne Report ID: 1272095
- Weakness: Information Exposure Through Debug Information
- Program: deptofdefense
- Disclosed At: 2021-09-09T19:59:23.377Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

While testing your program i came across an endpoint that is leaking sql errors and queries from on of your websites.

I use the following google dork to detect this:

site:████████ "sql error"

Endpoints leaking data:
https://www.██████/██████████
https://www.███████/███

Some of the errors found on https://www.███/█████:
SQLSTATE	  █████████
DATASOURCE	  ███
VENDORERRORCODE	  ███
SQL	   SELECT █████████, █████', '█████████, ██████, ████, ███████, ███████, ████████
(..)
██████████-████████: ██████" ████"
███
████
██████████
████
█████
(..)


Some of the errors found on https://www.███████/████:
SQLSTATE	  █████████
DATASOURCE	  █████
VENDORERRORCODE	  ███
SQL	   SELECT ██████████ ███████ ███████, ██████, ██████, █████, █████, ████████
(...)
█████████-███: ███████" █████"
██████
███████
████
█████
██████████
(...)

Best Regards
Miguel Santareno

## Impact

Attacker can use the error messages to gain further knowledge of the SQL system to launch future attacks.

## System Host(s)
www.███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Open the following endpoints https://www.██████████/█████ and https://www.█████████/███████ and you should be able to see the information above mentioned.

## Suggested Mitigation/Remediation Actions
Remove any mention of the SQL database calls in the stack trace error.

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
