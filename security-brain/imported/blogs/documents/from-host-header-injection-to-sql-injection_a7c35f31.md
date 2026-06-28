---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-05_from-host-header-injection-to-sql-injection.md
original_filename: 2020-07-05_from-host-header-injection-to-sql-injection.md
title: From Host Header injection to SQL injection
category: documents
detected_topics:
- sqli
- access-control
- command-injection
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- documents
- sqli
- access-control
- command-injection
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: a7c35f31336d5d33ca241f7704d848fc7d40d97e9977101d89a0aeb45ee3274c
text_sha256: 2fd721067f82050ffa9ca1908ebe9b59d09bbfb3dfd9e258ef38b670766425cb
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# From Host Header injection to SQL injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-05_from-host-header-injection-to-sql-injection.md
- Source Type: markdown
- Detected Topics: sqli, access-control, command-injection, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `a7c35f31336d5d33ca241f7704d848fc7d40d97e9977101d89a0aeb45ee3274c`
- Text SHA256: `2fd721067f82050ffa9ca1908ebe9b59d09bbfb3dfd9e258ef38b670766425cb`


## Content

---
title: "From Host Header injection to SQL injection"
url: "https://medium.com/@daoud_youssef/from-host-header-injection-to-sql-injection-e7c61a61b575"
authors: ["Daoud Youssef (@daoud_youssef)"]
bugs: ["Host header injection", "SQL injection"]
publication_date: "2020-07-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4438
scraped_via: "browseros"
---

# From Host Header injection to SQL injection

From Host Header injection to SQL injection
smacker dodi
Follow
4 min read
·
Jul 5, 2020

291

Press enter or click to view image in full size
Small issues lead to big Issues

Hi guys i hope that you all in good health

this write up about how a small vulnerabilities could leads to big one

I believe in automation so any mission i could automate i never do it manually so my whole recon phase is automated with bash script i made it myself to handle about 25 other tool and filter all their result into different text files . one of these tools is a simple bash script i made to iterate through subdomains list and send curl command for each subdomain and add custom headers to this curl command then search in the response if these headers exist in response header or response body .

while i was apply this technique to a program let’s call it somedomain.com i notice that X-Forwarded-Host Header in one of these subdomains which is dev-test.somedomain.com is reflected in the response headers ( exactly in the location header ) so if i inject this

X-Forwarded-Host: www.bing.com

this subdomain will redirect to www.bing.com .

I opened this subdomain in the browser while burp suite is on and the subdomain in normal condition redirect to www.somedomain.com without any body in the 302 response ( just headers ) but if i inject the header mentioned above it redirect to www.bing.com . so for these circumstances i have another bash script for this condition which will send this requests let’s say for two or three thousand time and then open the subdomain in the browser to check if the cache is poisoned and redirect to www.bing.com but this fails and the server was configures well for cache poisoning attacks and of course the program will never accept a bug that need MITM to inject this header in the victim’s browser so i think that i finished with this and ready to move for another issue . But

But then i noticed that when i inject this header the 302 response has a body which contain a form [ notice that in normal condition the response contain only response header with no response body ]

Get smacker dodi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So while intercepting the response with burp suite i changed the response code from 302 found to 200 Ok and remove the location header to stop redirect but the subdomain again redirect to www.bing.com .

i repeated the last step again and search in the body and i found this injected in the body

Press enter or click to view image in full size
The injected meta tag in body due to host header injection

So i deleted this meta tag in the burp suite and forwarded this response and in the browser i found my self in front of login form which in normal case i’m not suppose to reach but due to host header injection i could reach and access this form which was admin login form . so this form was sending the user and password over insecure protocol (HTTP) but this also is not acceptable by the program . the form also vulnerable to no rate limit on number of login but also rate limit issue is not acceptable by this program so finally i decided with no hope for something to happen to try SQLi payload

user : administrator’ or 1=1 --+
pass : any password

and bingo i found my self inside the admin dashboard . the subdomain was a dev test subdomain so no sensitive action or data inside the dashboard

i reported this to the program and they closed it as NA because they think that i reported host header injection through MITM . but when i send a detailed video that i don’t need a victim in this scenario and this is access control issue they accepted it and resolve it in 10 days but no bounty because it is VDP . but it is ok for me i am a good Samaritan :)

Takeaways :-

1- For Bug hunters don’t underestimate small bugs it could lead to bigger one

2- For developer and blue team apply defense in depth . do not assume attacker will not reach hidden forms or hidden pages and apply filters on the inputs of these pages and forms

Timeline :-

14 may : report

16 may : NA

18 may : reopen

24 may : resolved

thanks for reading :)
