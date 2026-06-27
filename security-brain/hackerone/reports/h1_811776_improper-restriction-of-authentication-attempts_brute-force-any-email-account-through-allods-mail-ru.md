---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '811776'
original_report_id: '811776'
title: Brute-force any email account through allods.mail.ru
weakness: Improper Restriction of Authentication Attempts
team_handle: mailru
created_at: '2020-03-05T23:34:42.721Z'
disclosed_at: '2020-03-13T11:05:20.523Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 7
asset_identifier: Ext. A Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# Brute-force any email account through allods.mail.ru

## Metadata

- HackerOne Report ID: 811776
- Weakness: Improper Restriction of Authentication Attempts
- Program: mailru
- Disclosed At: 2020-03-13T11:05:20.523Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

!!! Полная версия отчета со скриншотами находится __во вложенном PDF-файле__.

Vulnerability Technical description
=========================
По адресу **https://allods.mail.ru/account.php** находится форма регистрации нового
пользователя в игре. В процессе заполнения формы, посылается Ajax POST-запрос в
параметрах которого передаются пара логин-пароль на
URL __https://allods.mail.ru/ajaxreg.php__

В теле POST-запроса передается функция __verifyMruEmailPass__, из названия которой очевидно, что функция имеет отношение к верификации, а в совокупности с передаваемыми логином и паролем - к процессу аутентификации.

```shell
POST /ajaxreg.php HTTP/1.1
Host: allods.mail.ru
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referrer: https://allods.mail.ru/account.php
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest

do=verifyMruEmailPass=&password=SuperMegaPass&email=bug.bounty@list.ru
```
- При успешной аутентификации пользователю возвращается:
{
"Valid":"1",
"Error":""
}
- При неудачной:
{
"valid": "",
"error": "Неверно указан пароль от почты Mail.Ru!"
}

В первую же очередь уязвимость была проверена средствами Intruder, где за
основу был взят словарь в ~100 срок, в разные участки которого было вставлено пять
валидных паролей от учетной записи bug.bounty@list.ru. (passwd - hammer50!!)
Из результата выполнения запросов видно, что запросы __12, 37, 80, 93, 104__ -
вернули в теле респонса __{ "Valid" : "1", "Error" : ""}__.

Vulnerability Exploitation
==================
Для автоматизации Bruteforce-атаки, был разработан PoC shell-скрипт, который
выполняет ряд следующих действий:
+ Отображает старт скрипта
+ Подгружает с Github небольшой словарь для атаки
+ Построчно читает словарь
+ Выполняет в цикле POST-запрос используя curl
+ Отображает процесс выполнения запросов и их количество
+ Парсит результат выполнения и выводит его в случае успешной атаки
+ Отображает завершение скрипта и количество выполненных запросов

Скрипт запускается в терминале и в качестве аргумента передается атакуемый
емейл, например:
__user@linux:$ ./bruteforce_poc.sh bug.bounty@list.ru__

Далее, на емейле bug.bounty@list.ru был изменен пароль из словаря (выбрав
рандомно из середины) и был запущен скрипт на подбор пароля, статус и результат
выполнения отображены ниже

 Можно увидеть, что выполнение скрипта составило ~1 минуту и
количество запросов составило 76, при однопоточном режиме. Исходя из этой
информации - можно сделать простые расчеты по скорости выполнения атаки как в
однопоточном, так и многопоточных режимах с распределенной атакой.

Также следует отметить, что во время проведения атаки при успешной
аутентификации через сервис allods.mail.ru, пользователь не получает каких-либо
нотификаций и уведомлений о том, что был произведён логон под данным емейлом.

Step to Reproduce
==============
1. Скачать скрипт bruteforce_poc.sh (из вложения или отчета) и установить права
выполнения при необходимости (chmod +x).
2. Открыть настройки почты по смене пароля.
3. Открыть словарь
https://raw.githubusercontent.com/xajkep/wordlists/master/discovery/user_field_names.txt и выбрать любой пароль из списка.
4. Установить выбранный пароль из словаря в качестве нового пароля для почтового
ящика.
5. Запустить скрипт ./bruteforce_poc.sh username@mail.ru.
6. Наблюдать за процессом брутфорса до получения ожидаемого результата.

## Impact

Импакт брутфорс-атаки при отсутствии каких-либо превентивных мер - очевиден. 
Атакованы могут быть как таргетированные аккаунты, так и массовые проверки.

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
