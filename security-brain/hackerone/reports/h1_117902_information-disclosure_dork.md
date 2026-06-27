---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '117902'
original_report_id: '117902'
title: Дорк
weakness: Information Disclosure
team_handle: vkcom
created_at: '2016-02-22T05:43:38.862Z'
disclosed_at: '2016-11-18T15:29:47.730Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- information-disclosure
---

# Дорк

## Metadata

- HackerOne Report ID: 117902
- Weakness: Information Disclosure
- Program: vkcom
- Disclosed At: 2016-11-18T15:29:47.730Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Привет команда ВК 

вводим в гугл site:api.vk.com

получаем список ссылок 

сужаем запрос site:api.vk.com access_token 

Получаем ссылки с access_token  

https://api.vk.com/method/audio.getPopular.xml?access_token=73e0a5e18bb491249705e60ff352df91bd34a55ee634c9448b187feee9a8bcffde7eefb9000ea03d845a2&sort=&count=11&only_eng=0

Получаем список друзей 

https://api.vk.com/method/friends.get.xml?&access_token=73e0a5e18bb491249705e60ff352df91bd34a55ee634c9448b187feee9a8bcffde7eefb9000ea03d845a2&sort=&count=11&only_eng=0

Дальше экспериментировать не стал.

Спасибо заранее

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
