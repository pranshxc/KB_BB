---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '342944'
original_report_id: '342944'
title: api.icq.com / возможность написать кому угодно (даже icqsystem)
team_handle: mailru
created_at: '2018-04-24T21:26:35.365Z'
disclosed_at: '2018-04-28T11:25:04.520Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 6
tags:
- hackerone
---

# api.icq.com / возможность написать кому угодно (даже icqsystem)

## Metadata

- HackerOne Report ID: 342944
- Weakness: 
- Program: mailru
- Disclosed At: 2018-04-28T11:25:04.520Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Можно написать на любой uin через api запрос сделав хитрую махинацию 
у нас есть запрос 
``api.icq.net/im/sendIM``
``?t=1``
``&mentions=``
``&message=0``
``&f=``
``&aimsid=003.3533131881.4023885996%3A740645342``

видим параметр ``?t=1`` попробовав отослать на неё сообщение (Увы у нас не получится)
Но если в параметр добавить ``0`` ``?t=01``
то мы сможем отправить наше сообщение (можно отправить даже на несуществующий uin)

В Общем то всё если что приложу скрин каст и скриншоты

## Impact

Отправка сообщения на любой uin обходом параметра цифрой ``0`` перед началом uin

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
