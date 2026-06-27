---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '302253'
original_report_id: '302253'
title: Очень жесткая XSS в личных сообщениях m.ok.ru
weakness: Cross-site Scripting (XSS) - Stored
team_handle: ok
created_at: '2018-01-03T22:22:26.486Z'
disclosed_at: '2018-06-30T11:04:05.699Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 40
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Очень жесткая XSS в личных сообщениях m.ok.ru

## Metadata

- HackerOne Report ID: 302253
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: ok
- Disclosed At: 2018-06-30T11:04:05.699Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Приветствую.

Нашел багу в личных сообщениях в мобильной версии
{F251208}

Что нужно, чтоб заюзать:

1. Переходим в группу https://m.ok.ru/group/54904397693159/market
2. Ищем товар единственный на страничке
{F251213}
3. Переходим на него и нажимаем на кнопку "Связаться с продавцом" (https://m.ok.ru/group/54904397693159/market)
{F251215}
4. Видим алерт.
{F251216}


Нет фильтрации служебных символов тут -
<div class="discus_dialogs_topic emphased tx-ellip">"&gt;<img src="x" onerror="alert()"></div>

## Impact

XSS.

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
