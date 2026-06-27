---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '187602'
original_report_id: '187602'
title: '[element.mail.ru] /.svn/entries'
weakness: Information Disclosure
team_handle: mailru
created_at: '2016-12-02T06:25:26.915Z'
disclosed_at: '2017-03-02T13:17:47.978Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- information-disclosure
---

# [element.mail.ru] /.svn/entries

## Metadata

- HackerOne Report ID: 187602
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2017-03-02T13:17:47.978Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

В веб директории сайта содержится папка от Subversion.
Теоретически это дает раскрытие исходных кодов, но в данном случае файлы с расширением .php.svn-base тоже исполняются веб-сервером.

**Пример:**
```
https://element.mail.ru/.svn/entries
``` 

```
10

dir
14
https://office.raketa.center/svn/element-web-results/trunk/el5_gmr
https://office.raketa.center/svn/element-web-results



2016-11-30T16:15:54.841876Z
14
web














6086c3a0-2f5c-4305-a42f-7d1c32d336dd

Cache
dir

Config
dir

static
dir

cdn_check.php
file




2016-11-30T12:48:44.732739Z
e36b53b466ee98d7072459b056525708
2016-10-13T14:07:44.113442Z
11
web
```

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
