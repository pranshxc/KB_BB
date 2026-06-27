---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '65330'
original_report_id: '65330'
title: Не достаточная проверка логина скайп
weakness: Command Injection - Generic
team_handle: vkcom
created_at: '2015-06-01T22:34:48.127Z'
disclosed_at: '2015-10-30T11:34:43.884Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- command-injection-generic
---

# Не достаточная проверка логина скайп

## Metadata

- HackerOne Report ID: 65330
- Weakness: Command Injection - Generic
- Program: vkcom
- Disclosed At: 2015-10-30T11:34:43.884Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Существует не достаточная проверка в поле ввода логина skype.
В частности не фильтруются некоторые символы, например "?".
Что позволяет в вписывать некоторые команды скайпу, которые могут ввести пользователя в замешательство, а зачастую пользователь может "случайно" отправить злоумышленнику свои файлы.

Для воспроизведения проблемы вписываем в поле скайп следующее: 
abr1k0s-helm?sendfile&amp;

Теперь у любого, кто кликнет по логину скайпа на моей странице высветится диалог выбора файла. Если файл будет выбран (например случайно, либо по ошибке) - он тут же отправится мне (в данном случае выступающему в качестве злоумышленника) в скайп.

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
