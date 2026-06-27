---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '42403'
original_report_id: '42403'
title: Account Deleted without any confirmation
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2015-01-03T13:54:34.363Z'
disclosed_at: '2015-02-05T04:18:57.902Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Account Deleted without any confirmation

## Metadata

- HackerOne Report ID: 42403
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2015-02-05T04:18:57.902Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi

i don't know why this issue is not currently reported because its a big issue in mopub app here account is deleted without any confirmation 

Steps to reproduce
1. Login your account Admin A
2. know add any user as admin access AdminB
3. using invited link create new account which is AdminB
4. Create many inventory using account AdminA
5. Know remove adminA from adminB
6. Know you see account AdminA is deleted from app

account A lost all their inventory and other data 
here why account is deleted 

know go to Login account A which is Deleted web app shows "This user has no accounts"
know go register new account with same email web app shows  "This email address is already registered to another person"

the only one option is to live account again is  when someone invited you

when someone invited you , after clicking on confirmation link account is activated automatically 

when you reset the password , you receive password reset link , its reset the password but again same problem, during login same error =This user has no accounts

Account A have no any option to live again account until somone invite

why another account is able to do that?

hope you guys understand

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
