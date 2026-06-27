---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1081367'
original_report_id: '1081367'
title: crlf injection на https://bug.qiwi.com
weakness: CRLF Injection
team_handle: qiwi
created_at: '2021-01-19T11:44:26.068Z'
disclosed_at: '2021-03-31T07:59:00.719Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: '*.qiwi.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- crlf-injection
---

# crlf injection на https://bug.qiwi.com

## Metadata

- HackerOne Report ID: 1081367
- Weakness: CRLF Injection
- Program: qiwi
- Disclosed At: 2021-03-31T07:59:00.719Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

звдравствуйте.
я нашел crlf injection на https://bug.qiwi.com.
спомошъю этого злоумышленник может установить новые заголовки и  cookie загрезняя кэш

### инфа:
* site: ```https://bug.qiwi.com```
* path:  ```/landing/```
* payload:  ```/%0d%0aSet-Cookie:MyHeader=value```

### PoC:

```
https://bug.qiwi.com/landing//%0d%0aSet-Cookie:MyHeader=value
```

###  скриншоты

* burp
{F1163591}

* Browser
{F1163601}

{F1163602}

### попытка  xss

{F1163612}

просьба пересмотреть прикрепленные видео

## Impact

* Set malicious header and cookie
* cache poissening

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
