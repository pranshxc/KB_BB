---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99262'
original_report_id: '99262'
title: '[otus.p.mail.ru] Full Path Disclosure'
weakness: Information Disclosure
team_handle: mailru
created_at: '2015-11-12T11:20:00.348Z'
disclosed_at: '2017-03-27T13:10:13.556Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- information-disclosure
---

# [otus.p.mail.ru] Full Path Disclosure

## Metadata

- HackerOne Report ID: 99262
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2017-03-27T13:10:13.556Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Не факт, что вам удастся это исправить, так как проблема в стороннем ПО - "brat rapid annotation tool"

Который доступен по ссылке

otus.p.mail.ru/brat

Стоит немного погулять по директориям и увидим раскрытие путей:

Could not write statistics cache file to directory /home/sites/ling.go.mail.ru/brat/server/src/../../data/tutorials/bio/: [Errno 13] 

Permission denied: u'/home/sites/ling.go.mail.ru/brat/server/src/../../data/tutorials/bio/.stats_cache'

Скрин прикладываю.

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
