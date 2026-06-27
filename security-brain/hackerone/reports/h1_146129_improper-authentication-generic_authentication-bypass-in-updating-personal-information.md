---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146129'
original_report_id: '146129'
title: Authentication Bypass in Updating Personal Information
weakness: Improper Authentication - Generic
team_handle: instacart
created_at: '2016-06-20T22:20:44.337Z'
disclosed_at: '2017-01-17T17:57:05.310Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
tags:
- hackerone
- improper-authentication-generic
---

# Authentication Bypass in Updating Personal Information

## Metadata

- HackerOne Report ID: 146129
- Weakness: Improper Authentication - Generic
- Program: instacart
- Disclosed At: 2017-01-17T17:57:05.310Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Instacart,

Firstly, I would like to remind you that I made this report by mail 2 days ago, Sat, 16-08-2016 before I got the invite here. 

Although a user is expected to input password before updating their personal information. This is not so anyway as I have found that one could actually update "Personal Information​"​ without filling the "Current Password" field.

Steps to Reproduce:
1. Login your instacart account.
2. Go to account or https://www.instacart.com/store/account
3. In the personal information, Click Change
4. Fill new information leaving "Current Password" blank
5. Click "Save Account Information"
6. The ​​"Personal Information" will be updated.

This is a flaw as I could update my Personal Information without password although there is a field to input the password,hence, Authentication Bypass.

I hope I get a response from you soon.

​Looking Forward,
Shuaib Oladigbolu

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
