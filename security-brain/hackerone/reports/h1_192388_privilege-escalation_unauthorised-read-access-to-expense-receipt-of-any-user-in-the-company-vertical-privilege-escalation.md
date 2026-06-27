---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '192388'
original_report_id: '192388'
title: Unauthorised read Access to Expense Receipt of any user in the company(Vertical
  Privilege escalation)
weakness: Privilege Escalation
team_handle: harvest
created_at: '2016-12-19T11:34:34.176Z'
disclosed_at: '2017-04-12T06:23:44.441Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- privilege-escalation
---

# Unauthorised read Access to Expense Receipt of any user in the company(Vertical Privilege escalation)

## Metadata

- HackerOne Report ID: 192388
- Weakness: Privilege Escalation
- Program: harvest
- Disclosed At: 2017-04-12T06:23:44.441Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,

Description : In Timesheet you have option for submitting your expense for the projects you are assigned. But Only Admin can view other user's Expenses and related receipts. But there is a request which gives a full size of expense receipt attached to the expenses. This request is vulnerable to IDOR attack and any user can view any other user's receipts by changing the ID.

POC : 
Vulnerable link :
https://[Company_username].harvestapp.com/expenses/[Receipt_ID]/receipt

Change the receipt ID which exist in the company and you will be able to see the expense receipt submitted by any user in the company.

Let me know if you need any other help from my side.

Best Regards !
Vijay Kumar

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
