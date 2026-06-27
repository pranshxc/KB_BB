---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1061736'
original_report_id: '1061736'
title: Unauthorized access to PII leads to MASS account Takeover
weakness: Business Logic Errors
team_handle: deptofdefense
created_at: '2020-12-18T16:52:24.822Z'
disclosed_at: '2022-02-14T21:15:46.985Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- business-logic-errors
---

# Unauthorized access to PII leads to MASS account Takeover

## Metadata

- HackerOne Report ID: 1061736
- Weakness: Business Logic Errors
- Program: deptofdefense
- Disclosed At: 2022-02-14T21:15:46.985Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi, I hope you doing well
I found a critical endpoint which disclosed the personal information which can use to takeover any account present on https://██████████
#Steps:
1. Visit the link https://www.████████/███████    you will get my details,  including first name and last name, mobile number and email_address related to the account.
2. Go to the forgot password link present at https://www.███████/ click on it.
3. Enter the mail address later you will be taken to another page which will ask you to enter mail address and pin
4. After entering mail address enter the pin as "████" as █████████ is at the endpoint.
5. It will validate and will ask you to change the password of that account.

###Note:  To get email list and pin list just decrease the number at the endpoint 
for example https://www.████████/███will give you another mail_address and pin will be ██████████

## Impact

An attacker can able to takeover any account that is present on that side.

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
