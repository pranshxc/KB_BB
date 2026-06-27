---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '65013'
original_report_id: '65013'
title: HTML Injection на e.mail.ru
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-05-31T09:54:35.153Z'
disclosed_at: '2016-07-20T16:11:51.422Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HTML Injection на e.mail.ru

## Metadata

- HackerOne Report ID: 65013
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2016-07-20T16:11:51.422Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте,
Я обнаружил HTML инъекцию на e.mail.ru с помощью текстовых файлов формата .txt

Proof of concept:
>Создаем HTML файл с правильными тегами, то есть html head body... должны присутствовать. Иначе файл не будет воспроизведен как HTML
Меняем конец файла на .txt
Далее сжимаем этот файл при помощи RAR и прикрепляем к письму.

При онлайн воспроизведении файла со стороны отправителя и получателя текстовый файл воспроизводится как HTML

После просмотра видео, вам будет все ясно.

С уважением,
Джейхун Джафаров (c37hun)
Специалист по кибербезопасности
c37hun@mail.ru

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
