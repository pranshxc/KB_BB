---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '99273'
original_report_id: '99273'
title: '[gitmm.corp.mail.ru] Auth Bypass, Information Disclosure'
weakness: Improper Authentication - Generic
team_handle: mailru
created_at: '2015-11-12T11:51:47.573Z'
disclosed_at: '2017-03-27T13:12:13.998Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- improper-authentication-generic
---

# [gitmm.corp.mail.ru] Auth Bypass, Information Disclosure

## Metadata

- HackerOne Report ID: 99273
- Weakness: Improper Authentication - Generic
- Program: mailru
- Disclosed At: 2017-03-27T13:12:13.998Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Закрылись ото всех .htaccess-ом, но как-то неправильно выставили права. Я подозреваю, что на конкретные файлы. Или тут просто нижележащий .htaccess имеет приоритет над вышележащим.

Ну тем не менее...

Тут админка.

https://gitmm.corp.mail.ru/login

Тут установщик.

https://gitmm.corp.mail.ru/setup
https://gitmm.corp.mail.ru:8443/setup/unlock

И там и там никаких ограничений на брут не наблюдается.

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
