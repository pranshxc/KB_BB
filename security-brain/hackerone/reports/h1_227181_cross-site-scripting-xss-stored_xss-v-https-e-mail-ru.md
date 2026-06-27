---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '227181'
original_report_id: '227181'
title: Xss в https://e.mail.ru/
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2017-05-09T09:58:46.522Z'
disclosed_at: '2017-05-25T10:24:00.963Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Xss в https://e.mail.ru/

## Metadata

- HackerOne Report ID: 227181
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2017-05-25T10:24:00.963Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Привет,
Я обнаружил xss на https://e.mail.ru/ , похоже, это self-xss, но  вдруг в будущем планируется возможность расшаривать данную функциональность и это будет не self-xss, также атака csrf logout/csrf login может расширить её функционал. В том числе, это self-xss обходит текущие правила CSP. 

Для воспроизведения нужен ящик без текущих фильтров рассылок, по умолчанию их нет.

Шаги для воспроизведения:
1) создать папку с пейлоадов в названии (ex: qwe"><script>alert()</script>).
2) установить галочку "Архивная" - это важно.
3) перейти по https://e.mail.ru/settings/filters
4) Нажать на "Отфильтровать рассылки".
5)Profit!

Также, лично я вижу тут хороший вариант атаки. У вас есть функция синхронизация, т.е есть 3 почты, одна главная, и со всех адресов почта(и папки) синхронизируется, т.е жертва видит папки атакующего(имеющего доступ к одному из аккаунтов). Атакующий может вставить в название пейлоад, а жертва, при переходе в "Отфильтровать рассылки" вызовет xss, это уже будет не self.

Работает в Chrome и Firefox.

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
