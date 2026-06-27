---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '284346'
original_report_id: '284346'
title: Download attachments with traversal path into any sdcard directory (incomplete
  fix 106097)
weakness: Path Traversal
team_handle: mailru
created_at: '2017-10-30T18:27:07.369Z'
disclosed_at: '2017-12-28T07:39:09.106Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: ru.mail.mailapp
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- path-traversal
---

# Download attachments with traversal path into any sdcard directory (incomplete fix 106097)

## Metadata

- HackerOne Report ID: 284346
- Weakness: Path Traversal
- Program: mailru
- Disclosed At: 2017-12-28T07:39:09.106Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Привет

#106097 был исправлен не полностью, все еще можно скачать вложение в письме мимо downloads директории на  sdcard. 

Если имя файла будет что-от вроде "../file.txt" то такой файл будет скачен мимо /sdcard/download. Для файлов "%2e%2e%2f/file.txt" скачивает правильно. 
Скачать можно только на sdcard, в /data/data/ru.mail.mailapp/  не скачивает, так же если файл был создан, то оно его не перезаписывает, а создает новый

Сценарий для атаки такой:
1. На приложение Mail.ru воздействовать вроде никак не получится, однако допустим найдено некое приложение X которое хранит файлы в "/sdcard/Android/data/<x-package-name>"
2. Вот тогда такое вложение может попасть в  "/sdcard/Android/data/<x-package-name>" и эксплуатировать проблему приложения Х удаленно

Версия Android Mail.Ru Почты: 6.0.0.22977 from October 5, 2017

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
