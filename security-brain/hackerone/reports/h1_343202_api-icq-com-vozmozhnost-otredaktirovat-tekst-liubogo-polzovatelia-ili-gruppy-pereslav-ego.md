---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '343202'
original_report_id: '343202'
title: api.icq.com / возможность отредактировать текст любого пользователя или группы
  переслав его.
team_handle: mailru
created_at: '2018-04-25T23:57:00.779Z'
disclosed_at: '2018-04-28T14:31:08.901Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
---

# api.icq.com / возможность отредактировать текст любого пользователя или группы переслав его.

## Metadata

- HackerOne Report ID: 343202
- Weakness: 
- Program: mailru
- Disclosed At: 2018-04-28T14:31:08.901Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Нашёл лютую дырку дело в том что при пересылке сообщения пользователя (группы)
текст стоит в параметре конечно же я пробовал его отредактировать и послать пакет но никак не выходило и тут я использовал один старый метод, обычно же идёт GET запрос его мы и меняем, но после идёт POST запрос который отправляет все даннные на сервер для проверки. и в тоге всё шло к чёрту и изменённый GET запрос не отправлялся.

и так приступим 
Наш дырявый метод https://api.icq.net/im/sendIM
Вот ``PoC``: В скриншотах так будет понятнее
Тут у нас ``Оригинальный запрос``:
{F290389}
Далее ``идётвирусный запрос`` который будет отправлен.
{F290388}
После я отправил запрос, ``потом сбросил POST запрос и всё``.
``Результат``:
{F290390}
``ПРИКРЕПИЛ СКРИНКАСТ КАК ВОСПРОИЗВЕСТИ УЯЗВИМОСТЬ!``
====================
https://youtu.be/TDKX20heTDM
====================

## Impact

Редактирование чужих сообщений при ответе на них, ``Обход защиты сбросом POST запроса``

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
