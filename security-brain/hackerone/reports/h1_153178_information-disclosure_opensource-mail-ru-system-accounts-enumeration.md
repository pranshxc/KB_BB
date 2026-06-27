---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '153178'
original_report_id: '153178'
title: '[opensource.mail.ru] system accounts enumeration'
weakness: Information Disclosure
team_handle: mailru
created_at: '2016-07-22T14:50:39.102Z'
disclosed_at: '2016-08-08T09:03:55.625Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# [opensource.mail.ru] system accounts enumeration

## Metadata

- HackerOne Report ID: 153178
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2016-08-08T09:03:55.625Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Добрый день. Нашел интересную вещь. Надеюсь уязвимость на самом деле существует, и я не параноик.

Если аккаунт существует (cat /etc/passwd | grep %account_name%) то приложение редиректит (302) на /create/%account_name%/home или возвращает 200 как в случай ~nobody. 

https://opensource.mail.ru/~nobody/
https://opensource.mail.ru/~daemon/
https://opensource.mail.ru/~root/
https://opensource.mail.ru/~daemon/
https://opensource.mail.ru/~lp/
https://opensource.mail.ru/~adm/
https://opensource.mail.ru/~shutdown/
https://opensource.mail.ru/~bin/
https://opensource.mail.ru/~sshd/

если аккаунт не существует в системе то приложение возвращает status 500 
https://opensource.mail.ru/~doesntexist/

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
