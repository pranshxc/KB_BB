---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '143669'
original_report_id: '143669'
title: Получение оригинала скрытого изображения
weakness: Information Disclosure
team_handle: bumble
created_at: '2016-06-08T11:48:54.104Z'
disclosed_at: '2016-06-09T19:39:57.359Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Получение оригинала скрытого изображения

## Metadata

- HackerOne Report ID: 143669
- Weakness: Information Disclosure
- Program: bumble
- Disclosed At: 2016-06-09T19:39:57.359Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте!
В вашем сервисе есть фотографии сильно низкого качества, чтобы было невозможно разобрать кто на нем изображен. (например  разделе "Кому вы нравитесь?"  ) 
Наше способ получить оригинал.
Берем адрес скрытой картинки:
https://pcache-pv-eu1.badoocdn.com/p76/hidden?euri=CD7SrePxVBgqQI6NZlSecpEED0VHR8HQsai3k4ChKXuBzuG9amb01yjMHKK12cPtpVOm2LUb0DXtv.wOaGyaHsKRyUMIHzgE1oEKsIAMFVl4315WdppTSP-D2jL1bI3oyRU4o-HvAtBwyJ4H0XgUWVSB7J4LTXmh&size=__size__

Дописываем  в конец "?"
Получили оригинал:
https://pcache-pv-eu1.badoocdn.com/p76/hidden?euri=CD7SrePxVBgqQI6NZlSecpEED0VHR8HQsai3k4ChKXuBzuG9amb01yjMHKK12cPtpVOm2LUb0DXtv.wOaGyaHsKRyUMIHzgE1oEKsIAMFVl4315WdppTSP-D2jL1bI3oyRU4o-HvAtBwyJ4H0XgUWVSB7J4LTXmh&size=__size__?

Хорошего дня!

С Уважением, 
Сергей Никитченко

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
