---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-14_how-i-was-able-to-pwned-30000-users-webhook.md
original_filename: 2019-03-14_how-i-was-able-to-pwned-30000-users-webhook.md
title: How I was able to pwned 30000+ user’s webhook
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
- webhooks
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
- webhooks
language: en
raw_sha256: 2bf272a526d6b6b40b5343827d0611f0b26ed0fa478947091bb5e49038018636
text_sha256: f56ccfac9051c0de58435ed5151f42d7082edee81b37d4ba64a6cb4d0faf0d1b
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to pwned 30000+ user’s webhook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-14_how-i-was-able-to-pwned-30000-users-webhook.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, webhooks
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `2bf272a526d6b6b40b5343827d0611f0b26ed0fa478947091bb5e49038018636`
- Text SHA256: `f56ccfac9051c0de58435ed5151f42d7082edee81b37d4ba64a6cb4d0faf0d1b`


## Content

---
title: "How I was able to pwned 30000+ user’s webhook"
url: "https://medium.com/@vis_hacker/how-i-was-able-to-pwned-30000-users-webhook-d26dc3420703"
authors: ["gujjuboy10x00 (@vis_hacker)"]
bugs: ["IDOR"]
publication_date: "2019-03-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5357
scraped_via: "browseros"
---

# How I was able to pwned 30000+ user’s webhook

How I was able to pwned 30000+ user’s webhook
Gujjuboy10x00
Follow
3 min read
·
Mar 14, 2019

227

Hello Guys !!

I am writing this report after a longtime about my finding on 1 private program. I got invite with one of private program(ex: xyz.com) on hackerone .

After looking into complete functionality of web application , i get to know that they have webhook functionality.

What is Webhooks?

A webhook (also called a web callback or HTTP push API) is a way for an app to provide other applications with real-time information. A webhook delivers data to other applications as it happens, meaning you get data immediately.

A web application implementing WebHooks will POST a message to a URL when certain things happen. WebHooks are a way to receive valuable information when it happens, rather than continually polling for that data and receiving nothing valuable most of the time.

After looking into webhook functionality in xyz application , which feature is used to add notification for all branches (CI/CD), where some ID (ex: 1588211) is generating in sequence on every different webhook.

Actually it was old target , still i tried to check for IDOR vulnerability as ID was generated for each webhooks and that was in sequence.

What is IDOR Vulnerability?

Insecure Direct Object References occur when an application provides direct access to objects based on user-supplied input. As a result of this vulnerability attackers can bypass authorization and access resources in the system directly, for example database records or files. if you want to know more on this refer here : IDOR vulnerability

Get Gujjuboy10x00’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

There is option to delete created webhooks for that user. which request looks like below

PUT /projects/322335/notifications HTTP/1.1 
Host: xyz.com 
Connection: close
Content-Length: 388
{"authenticity_token":"test","notification":{"notifier":"deletewebhook","branch":"admin","build_owner":"all",{"webhook_url":"https://1"},"enabled":false,"id":1588211,"description":"admin""}}

Now , we already know that ID in request body is incremental , so i created 1 more account and create few webhooks. so , by changing ID in above delete request i was able to delete another user’s webhook.

As this number is in sequence , attacker can just run burp intruder for $ID$ and can delete all user’s webhook running on. I was like wtf!!!!!!

Team replied within a day ,

Team fixed this issue within 2 days.

Thanks for reading guys , I always believed that sharing is caring. Hope You liked this finding. Many more are coming. Stay tuned. feel free to comment if you have any question , or shoot me DM in twitter (twitter.com/vis_hacker )
