---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '341884'
original_report_id: '341884'
title: api.icq.com / возможность присоединиться к любому чату (даже закрытому).
team_handle: mailru
created_at: '2018-04-23T01:10:12.053Z'
disclosed_at: '2018-06-17T14:27:09.328Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
---

# api.icq.com / возможность присоединиться к любому чату (даже закрытому).

## Metadata

- HackerOne Report ID: 341884
- Weakness: 
- Program: mailru
- Disclosed At: 2018-06-17T14:27:09.328Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Получаем ссылку с АПИ на подключение к чату
в моём случае она вот такая
``https://api.icq.net/mchat/AddChat?aimsid=002.0516319051.0828645279:740645342&c=WebIM.jscb_tmp_c12813&chat_id=680009979@chat.agent&members=740645342``
видим параметр 
``&chat_id=680009979@chat.agent``
просто меняем цифровое значение и всё мы подсоединились к чату
прикрепил скриншот того как я подключился к закрытому чату.

## Impact

уязвимость в доступе метода API на подключению к чатам.

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
