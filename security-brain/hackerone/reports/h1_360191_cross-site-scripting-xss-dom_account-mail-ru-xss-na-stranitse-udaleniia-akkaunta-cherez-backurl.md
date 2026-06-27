---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '360191'
original_report_id: '360191'
title: '[account.mail.ru] XSS на странице удаления аккаунта через backUrl'
weakness: Cross-site Scripting (XSS) - DOM
team_handle: mailru
created_at: '2018-05-31T13:22:24.395Z'
disclosed_at: '2018-07-31T14:54:26.604Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: account.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# [account.mail.ru] XSS на странице удаления аккаунта через backUrl

## Metadata

- HackerOne Report ID: 360191
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: mailru
- Disclosed At: 2018-07-31T14:54:26.604Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Недостаточная валидация параметра **backUrl** даёт возможность указать javascript-ссылку:

https://account.mail.ru/user/delete?backUrl=javascript:alert(document.domain)

```javascript
getBackUrl: function (url) {
	return /^http/.test(url) ? url : (this.urlData.backUrl || this.config.get('backUrl') || 'https://e.mail.ru');
},
```

```javascript
exit: function (url) {
	window.location.href = this.getBackUrl(url);
 },
```

```javascript
onExit: function (event, ui) {
	this.unloadHandled = true;
	this.router.exit();
},
```

Domain, site, application
--
https://account.mail.ru/user/delete

Testing environment
--
Firefox 60.0
Chrome 66.0

Steps to reproduce
--
1. Заходим в аккаунт
2. Открываем https://account.mail.ru/user/delete?backUrl=javascript:alert(document.domain)
3. Нажимаем «Отменить»

Actual results
--
XSS

Expected results, security impact description and recommendations
--
Фильтровать javascript + проверять, что ссылка ведёт на домен mail.ru

PoC, exploit code, screenshots, video, references, additional resources
--
{F303613}

## Impact

XSS

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
