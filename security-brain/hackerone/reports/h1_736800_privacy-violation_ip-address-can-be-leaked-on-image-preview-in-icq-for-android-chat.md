---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '736800'
original_report_id: '736800'
title: IP address can be leaked on Image preview in ICQ for Android chat
weakness: Privacy Violation
team_handle: mailru
created_at: '2019-11-13T12:07:33.501Z'
disclosed_at: '2020-02-14T19:20:36.371Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
asset_identifier: ICQ
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# IP address can be leaked on Image preview in ICQ for Android chat

## Metadata

- HackerOne Report ID: 736800
- Weakness: Privacy Violation
- Program: mailru
- Disclosed At: 2020-02-14T19:20:36.371Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Описание:
При отправке пользователю изображения, в android версии (в web и mac версии клиента этой проблемы не наблюдаю) со внешнего ресурса, при открытии превью изображения "жертвой", отправляется запрос на внешний сервер с IP адреса клиента.

## Воспроизведение: 
  1. Отправляем пользователю сообщение со ссылкой на внешнее JPG изображение (с GIF не работает, для PNG нужно больше действий от пользователя). Например: 
https://envatotools.com/hornet/messages-ip/?f=jpg&z=image.jpg
  1. "Жертва" открывает чат с данным пользователем и открывает изображение на весь экран: 
{F633223}
  1. Получаем запрос на сервер, с IP адресом пользователя: █████████

## Impact

Раскрытие IP-адресов пользователей

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
