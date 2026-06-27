---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '357213'
original_report_id: '357213'
title: Получаем все домены и поддомены icq с помощью amazonaws.com [config,txt]
team_handle: mailru
created_at: '2018-05-25T00:41:50.994Z'
disclosed_at: '2018-07-06T12:07:04.087Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
---

# Получаем все домены и поддомены icq с помощью amazonaws.com [config,txt]

## Metadata

- HackerOne Report ID: 357213
- Weakness: 
- Program: mailru
- Disclosed At: 2018-07-06T12:07:04.087Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Открытый доступ к config.txt на амазоне (где лежат все ваши домены и поддомены)

``{  "api.icq.net": "api.ic2ster.com",  "bos.icq.net": "bos.ic2ster.com",  "api.login.icq.net": "apilogin.ic2ster.com",  "icq.com": "www.ic2ster.com ",  "www.icq.com ": "www.ic2ster.com ",  "files.icq.com": "files-com.ic2ster.com",  "files.icq.net": "files-net.ic2ster.com",  "rapi.icq.net": "rapi.ic2ster.com",  "pymk.icq.net": "pymk.ic2ster.com",  "files-upload.icq.com": "files-upload.ic2ster.com",  "clientapi.icq.net": "clientapi.ic2ster.com", "store.icq.com": "store.ic2ster.com" }`` 

Ссылка: https://s3.amazonaws.com/icqlive/config.txt

Желательно сделать закрытым например как у Google
``<Code>AccessDenied</Code>``

## Impact

Открытый доступ к config.txt на амазоне (где лежат все ваши домены и поддомены)

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
