---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-30_developer-luminate-idor.md
original_filename: 2017-08-30_developer-luminate-idor.md
title: Developer Luminate IDOR
category: documents
detected_topics:
- idor
- command-injection
- otp
tags:
- imported
- documents
- idor
- command-injection
- otp
language: en
raw_sha256: 15c7c9ca2f26eadd6423b72814b9c97514d73379e7f5e68cc8217c59db86d40c
text_sha256: 6391c2baa50ecaa33b0f63dc9600148a937836111093ec9235b0fabc64b27480
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Developer Luminate IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-30_developer-luminate-idor.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `15c7c9ca2f26eadd6423b72814b9c97514d73379e7f5e68cc8217c59db86d40c`
- Text SHA256: `6391c2baa50ecaa33b0f63dc9600148a937836111093ec9235b0fabc64b27480`


## Content

---
title: "Developer Luminate IDOR"
url: "https://medium.com/@rojanrijal/developer-luminate-idor-42bd0d98e0c"
authors: ["Rojan Rijal (@uraniumhacker)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["IDOR"]
publication_date: "2017-08-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6117
scraped_via: "browseros"
---

# Developer Luminate IDOR

Developer Luminate IDOR
Rojan Rijal
Follow
2 min read
·
Aug 31, 2017

69

Continuing on my work in Yahoo’s bug bounty program, another app i tested was: Luminate Developer app. In this application, I can create apps that website admins can install to their store from Luminate app store. App makers can also use this app to see the statics of their apps: who installed it (emails and website of the admins).

When I started testing, I noticed that to retrieve the statics of the app, a certain JSON request was made. It was a GET request that would request the statistics based on the app token. This was the url that would retrieve the JSON file:

https://developers.commercecentral.luminate.com/admin/apps/[apptoken]/installs.json?random=true&start=0&limit=8&_=1502762696055

First, I created two different accounts (account A and account B) and created two apps (app 1 and app 2) to test out the IDOR. At first, when putting app token, from another account no error was thrown. After that, I decided to use my second account (account B) and installed that app (account 2) to a test commercial center account. Once the installation was done, we could test the IDOR and when we browsed to the link with account A, it successfully showed the installed statistics (cannot post pic here for privacy reasons).

Get Rojan Rijal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Next issue was to get the app token. For my test run, I already had the app token. How would an attacker get an app token of a well known app in Luminate?

To test this, I went to Luminate’s commercial central and installed an app. During installation, it was noted that when I browsed the installation page, it would use the following request:

GET /admin/apps/live/settings/[appname]?store_url=[store_url]&pid=YS.×tamp=1502936968&proxy_app=1&token=[token]&app_token=[app_token]&email=[user_email]&p=YS&id=[id]&signature=asdasd84949823asfasd HTTP/1.1
Host: embed.commercecentral.luminate.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://embed.commercecentral.luminate.com/admin/apps/[app_name]
Cookie: [redacted_cookies]
Connection: close
Upgrade-Insecure-Requests: 1

So now, we could grab the `app_token` from the url, and paste that to the JSON request. This would give list of all users who installed that app in their page.

Shoutout to Yahoo once again. :) I am looking forward to finding more bugs on their platform again.
Cheers!
uranium238 / Rojan Rijal

Originally published at medium.com on August 30, 2017 from my alternate account. Added here to make a collection of all my blogs.
