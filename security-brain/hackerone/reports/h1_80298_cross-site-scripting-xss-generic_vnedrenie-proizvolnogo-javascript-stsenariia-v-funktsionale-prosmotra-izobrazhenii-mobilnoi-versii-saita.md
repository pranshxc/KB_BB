---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '80298'
original_report_id: '80298'
title: Внедрение произвольного javascript-сценария в функционале просмотра изображений
  мобильной версии сайта
weakness: Cross-site Scripting (XSS) - Generic
team_handle: vkcom
created_at: '2015-08-03T11:26:58.890Z'
disclosed_at: '2015-10-30T12:10:41.684Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Внедрение произвольного javascript-сценария в функционале просмотра изображений мобильной версии сайта

## Metadata

- HackerOne Report ID: 80298
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: vkcom
- Disclosed At: 2015-10-30T12:10:41.684Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Уязвимость существует из-за недостаточной обработки пользовательских данных, полученных из объекта location (url), который используется в функции photo.fullscreen. Функция выполняется при активации события onclick, который срабатывается при клике на фотографию
В настоящее время существует фильтрация пользовательских данных путем экранирования специальных символов, в том числе потенциально-опасного символа одинарной кавычки, однако, фильтрация не затрагивает сам символ слэша, поэтому пользователь может передать в качестве префикса вектора атаки пару `\'`, пройдя через механизм экранирования, пара примет вид `\\'`, следовательно, одинарная кавычка потеряет статус экранирования, что нарушит логику работы функции и позволит выполнить злоумышленнику произвольный js сценарий.

Пример
https://m.vk.com/feed?z=photo-25557243_375319886%2F#abc'123
`photo.fullscreen('/feed?z=photo-25557243_375319886%2Falbum-25557243_00#abc\'123', event);`
https://m.vk.com/feed?z=photo-25557243_375319886%2F#abc\'123
`photo.fullscreen('/feed?z=photo-25557243_375319886%2Falbum-25557243_00#abc\\'123', event)`

Пример вектора атаки с выполнением всплывающего окна
https://m.vk.com/feed?z=photo-25557243_375319886%2F#\')+alert(document.domain)//

Уязвимость усугубляется тем, что данный вид атаки работает во всех современных браузерах и не детектируется в встроенные в браузер механизм защиты (XSS Auditor). Злоумышленник, в результате эксплуатации данной атаки может подменять содержимое сайта, переслать переписку или выполнять произвольные действия от лица пользователя.

Демонстрация эксплуатации на следующем видео:
https://youtu.be/Y9mm3OcESoU

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
