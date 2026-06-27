---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '140705'
original_report_id: '140705'
title: '[my.mail.ru] HTML injection в письмах от myadmin@corp.mail.ru'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2016-05-24T12:49:47.991Z'
disclosed_at: '2016-10-03T11:55:46.251Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [my.mail.ru] HTML injection в письмах от myadmin@corp.mail.ru

## Metadata

- HackerOne Report ID: 140705
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2016-10-03T11:55:46.251Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1) Создаем группу и приглашаем в нее пользователей 
https://my.mail.ru/my/editcommunity

2) Меняем название группы на
`</a><a href="//blackfan.ru"><img src="//blackfan.ru/fk"></a><!--`

3) Устанавливаем пользователям права модератора или смотрителя
https://my.mail.ru/community/blahblahgroup/communityaccess

4) Откатываем права и меняем название назад

В результате пользователи получают уведомление "Вас назначили модератором" от myadmin@corp.mail.ru. В теле письма содержится html инъекция через название группы:

```
Вы назначены модератором группы "[html_inj]"
```

Пример письма в приложении.

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
