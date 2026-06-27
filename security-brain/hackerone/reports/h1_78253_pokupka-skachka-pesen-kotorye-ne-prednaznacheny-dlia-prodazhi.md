---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '78253'
original_report_id: '78253'
title: Покупка=>скачка песен, которые не предназначены для продажи
team_handle: ok
created_at: '2015-07-23T23:27:38.786Z'
disclosed_at: '2017-03-20T15:50:21.812Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# Покупка=>скачка песен, которые не предназначены для продажи

## Metadata

- HackerOne Report ID: 78253
- Weakness: 
- Program: ok
- Disclosed At: 2017-03-20T15:50:21.812Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Итак, часть песен в приложении можно купить. Нажимая на кнопку купить, происходит запрос к серверу (обрезано, для удобства):

GET /isDownloaded;jsessionid=DZSUq1yT_UMNFNcYk5-mZ10DGJbUCoNYFHRUcNNwINHoSrDkkkf4gInosiPimoqGaysNvWs7GV7fnOMGgfsbCA.hHaqWq9PyS8b9PmEoYf_cA?tid=90920917758231

В ответ получаем:

{"title":"Ð¨Ð°ÑÐµÑÐµÐ·Ð°Ð´Ð°","trackId":90920917758231,"price":10,"copyrightOwnerName":"Digital Project","isBought":false,"copyrightOwnerId":22,"image":null,"artist":"ÐÐ°ÑÐ°Ð»Ð¸"}

Но, если нажать на любую песню, у которой доступно скачивание, и поменять во время первого запроса параметр tid на значение песни, которую хочется скачать, то система начинает работать с ними. Никакой проверки возможно продажа песни или не возможна - нету. 
Следующей проблемой становиться нулевая цена таких песен - платёжный гейт не может принять нулевую цену и сообщает, что он "в данный момент не работает, попробуйте позже". Но её можно решить подменой приходящих значений (я описывал это в прошлом репорте), В итоге после подмены, мы имеем песню за 1 ОК, покупаем её, и можем скачать.

Не смотря на то, что с точки зрений прибыли - это и кажется "хорошо", но с точки зрения копирайта - могут возникнуть проблемы. 
Предполагаю, что у песен должен быть некий параметр - можно ли её вообще купить или нет.

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
