---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1382570'
original_report_id: '1382570'
title: Deliviry Club Courier app (v. 3.9.25.0); Disclosure phone number of client.
weakness: Information Disclosure
team_handle: mailru
created_at: '2021-10-26T22:53:22.818Z'
disclosed_at: '2022-02-23T13:01:31.631Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: Delivery Club
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Deliviry Club Courier app (v. 3.9.25.0); Disclosure phone number of client.

## Metadata

- HackerOne Report ID: 1382570
- Weakness: Information Disclosure
- Program: mailru
- Disclosed At: 2022-02-23T13:01:31.631Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте. Я нашёл баг в приложениидля курьеров, позволяющий получить реальный номер телефона клиента. 
Обычно, когда курьеру необходимо позвонить клиенту для уточнения какого-либо  вопроса, курьер нажимает "Позвонить клиенту", и после этого совершается звонок не на номер клиента, а через  Delivery  Club, тем самым не раскрывая номер клиента курьеру. 

Как  воспроизвести:
1) Во время активного заказа включить режим полёта
2) Где "Позвонить клиенту" нажать на значок "?" и увидеть номер клиента
(так же можно) просто в режиме полёта нажать "Позвонить клиенту". Однако номер показан не будет, а посмотреть его можно будет только в истории звонков. 

Прикрепляю видео (PoC.mp4), в котором демонстрируется возможность получить номер клиента:

## Impact

Information disclosure.

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
