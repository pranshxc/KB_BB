---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '365093'
original_report_id: '365093'
title: XSS https://agent.postamat.tech/ в профиле + дисклоз секретной информации
team_handle: qiwi
created_at: '2018-06-12T21:00:28.702Z'
disclosed_at: '2020-05-25T14:25:02.784Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
tags:
- hackerone
---

# XSS https://agent.postamat.tech/ в профиле + дисклоз секретной информации

## Metadata

- HackerOne Report ID: 365093
- Weakness: 
- Program: qiwi
- Disclosed At: 2020-05-25T14:25:02.784Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте.

Я раскрутил ваш сайт https://agent.postamat.tech/ на интересную XSS + достаточно серьезный баг, который дисклозит некоторую пользовательскую информацию. Хочу заметить что на данном сайте хранятся некоторые личные данные пользователей, следовательно из этой XSS можно извлечь достаточно весомый ипакт.

Что нужно для выполнения данной баги:
1. Нам нужен аккаунт на данном сайте. 
2. И нужен эмайл, который я для вас уже подготивил dfhdfh@o3enzyme.com

Инструкция:

1. Заходим на данный сайт со своего аккаунта;
2. Переходим во вкладку "Профиль";
3. Открываем форму добавления нового контакта и заполняем ее так:
{F308152}
ОБРАТИТЕ ВНИМАНИЕ - В ДАННУЮ ФОРМУ МЫ ВСТАВЛЯЕМ ЭМАЙЛ, ЗАГОТОВЛЕННЫЙ МНОЙ РАННЕЕ 
4. Сохраняем.
5. Срабатывает XSS.

{F308154}

Обратите внимание, что пользователь нигде не вводит в имя-фамилию и т.д. вредоносный скрипт.
Он появляется там сразу, а это является следствием второй баги - дисклоза информации по эмайлу.

Сам вредоносный скрипт - </script><script>alert();</script>

Участок кода, где видна недостаточная фильтрация данных:

{F308155}

Как в реальной жизни мы можем провести атаку:

Предположим, что мы узнали эмайлы, которые в теории владелец аккаунта может добавить к себе в контакты -> мы берем и заранее загоняем в эти аккаунты вредоносные скрипты (делается это очень просто- мы сами берем и через свой аккаунт туда все вписывам).

Также мы можем пройтись по списку и по эмайлам побрутить полезную информацию об их владельцах.

Это не self-xss т.к. пользователь сама нигде не вынужден вводить вредоносный скрипт. Скрипт уже находится в базе сайта. Ввод знакомого эмайла не вызовет подозрений.

Спасибо.

## Impact

XSS + дисклоз приватной информации

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
