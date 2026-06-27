---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1438213'
original_report_id: '1438213'
title: No Rate Limit On Forgot Password Page
team_handle: tennessee-valley-authority
created_at: '2021-12-30T15:38:08.620Z'
disclosed_at: '2023-09-11T11:53:09.079Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: '*.tva.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# No Rate Limit On Forgot Password Page

## Metadata

- HackerOne Report ID: 1438213
- Weakness: 
- Program: tennessee-valley-authority
- Disclosed At: 2023-09-11T11:53:09.079Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
About No rate Limiting Vulnerability:-
No rate limit is a flaw that doesn't limit the no. of attempts one makes on a website server to extract data.It is a vulnerability which can prove to be critical when misused by attackers.

## Description:-
I have identified that when using forget password for account, The request has no rate limiting through which i can send multiple request to the server in order to guess the correct username after that in security question also there is no rate limiting set through which i can able to guess the answer as well which can be lead to account takeover.

## Steps To Reproduce:

  1. Step 1-Go To This Link  https://ctr.tva.com/Login.aspx  and click on forget password page.
  2.  Intercept This Request In Burp and send it to intruder. 
  3. add mark on username and set payload and click on start attack.
  4.as you can see i can able to send multiple request to the server in order to guess the correct username.

## Supporting Material/References:
https://www.geeksforgeeks.org/no-rate-limiting-flaw-in-cyber-security

## Impact

As rate limiting is not set in forget password page and security question page i can able to perform brute force attack to enumerate  valid username and correct answer for security question which can lead to breaking of authentication or can even lead to account takeover.

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
