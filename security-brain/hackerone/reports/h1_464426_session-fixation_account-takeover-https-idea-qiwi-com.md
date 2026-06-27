---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '464426'
original_report_id: '464426'
title: account takeover https://idea.qiwi.com/
weakness: Session Fixation
team_handle: qiwi
created_at: '2018-12-17T22:10:18.379Z'
disclosed_at: '2019-08-28T08:18:21.086Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 87
tags:
- hackerone
- session-fixation
---

# account takeover https://idea.qiwi.com/

## Metadata

- HackerOne Report ID: 464426
- Weakness: Session Fixation
- Program: qiwi
- Disclosed At: 2019-08-28T08:18:21.086Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте. Обнаружил account takeover на данном сайте. С воспроизведением придется поднапрячься, но это стоит того. Учитывая то, что на сайте есть админский аккаунт, в теории можно натворить делов.

Скажу сразу, что мне не удалось полностью понять механизм работы данного тейковера и я буду очень сильно дволен, если после фикса вы расскажете из-за чего он все таки существовал.

Как я понял проблема возникает из-за того, что сессии при логине примерно в одно и то-же время 
каким-то образом могут дублироваться.

Мой способ воспроизведения, который работает примерно в 70% случаев:

1. Удаляем куки в своем браузере;
2. Удаляем куки в браузере друга; 
3. Заходим на https://idea.qiwi.com/, попутно включая интрудер в бурпе -> мотаем запросы до того момента, пока не увидим этот запрос
{F391861}
4. Просим друга залогиниться на сайте через ВКонтакте и сразу после того, как он залогинился отправляем данный запрос.
5. Мы вместо своего аккаунта попадаем в аккаунт к ДРУГУ.

Если не работает сразу, чистите куки и повторяйте. Мне было очень сложно понять как именно придти к более-менее рабочему способу воспроизведения.

## Impact

Что мы имеем в итоге:
1. После того, как получилось проэксплуатировать уязвимости кука PHPSESSID в нашем браузере совпадает с кукой PHPSESSID в браузере жертвы;
2. Мы получаем полный доступ к аккаунту жертвы;
3. Повторяя данные действия бесконечно (возможно каким-то образом можно сделать программную автоматизацию), мы можем рано или поздно попасть в админский аккаунт;
4. За время тестирования удалось зайти в несколько аккаунтов и вопспроизвести моим методом сразу с несколькими друзьями:

{F391881}

{F391883}

{F391885}

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
