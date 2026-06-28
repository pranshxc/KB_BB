---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-07_from-android-static-analysis-to-rce-on-prod.md
original_filename: 2020-09-07_from-android-static-analysis-to-rce-on-prod.md
title: From Android Static Analysis to RCE on Prod
category: documents
detected_topics:
- information-disclosure
- api-security
- mobile-security
- idor
- command-injection
- cloud-security
tags:
- imported
- documents
- information-disclosure
- api-security
- mobile-security
- idor
- command-injection
- cloud-security
language: en
raw_sha256: a8a5b2b55e5f499eadf2ef77987c844a5c3d3b2a9463a2a4a13cd920dd6fab92
text_sha256: 2fb9e8572e8d7e5405553675c622bdc7d20a4e48baeb0f5383532d9c8c4dca36
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# From Android Static Analysis to RCE on Prod

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-07_from-android-static-analysis-to-rce-on-prod.md
- Source Type: markdown
- Detected Topics: information-disclosure, api-security, mobile-security, idor, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `a8a5b2b55e5f499eadf2ef77987c844a5c3d3b2a9463a2a4a13cd920dd6fab92`
- Text SHA256: `2fb9e8572e8d7e5405553675c622bdc7d20a4e48baeb0f5383532d9c8c4dca36`


## Content

---
title: "From Android Static Analysis to RCE on Prod"
page_title: "Android Static Analysis to RCE"
url: "https://blog.dixitaditya.com/from-android-app-to-rce/"
final_url: "https://blog.dixitaditya.com/android-static-analysis-to-rce"
authors: ["Aditya Dixit (@zombie007o)"]
bugs: ["RCE", "Directory listing", "Missing authentication"]
publication_date: "2020-09-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4274
---

# From Android Static Analysis to RCE on Production

UpdatedFebruary 3, 2022

•3 min read•[ __View as Markdown](/android-static-analysis-to-rce.md)

![From Android Static Analysis to RCE on Production](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1643881848300%2FN4bF8os1g.jpeg&w=3840&q=75)

[ A](https://hashnode.com/@adityadixit)

[Aditya Dixit](https://hashnode.com/@adityadixit)

[ __](https://twitter.com/zombie007o)[__](https://www.linkedin.com/in/ad17ya/)

I'm leading the Research at Credshields, and Pentest teams at Cobalt Labs and HackerOne. I occasionally blog about my findings and adventures in pentesting.

**TL;DR**  
We exploited an information disclosure in the mobile app to get an RCE on an internal server which was leveraged to the prod environment.

Let's call the organization " **Redacted Inc.".**  
Their in-scope apps and URL's are their Android apps, and two URL endpoints -

  * api.redacted.com
  * app.redacted.com

Any static analysis of the android application starts with decompiling the app and I use MobSF for doing that.  
One of the most eye-catching sections of a MobSF Report is the section that lists the files that might contain hardcoded sensitive information like usernames, constants, keys, passwords, etc which looks somewhat like this.

![mobsf](https://imgur.com/aWbFLbi.png)

The file I'm most concerned about here is the `Global.java`.

After opening the link it turns out that the file contains tons of hard-coded information used by the application some of which are API Keys, URLs to the application API's and a few other IP Addresses which seem **_unusual_**.

The part that got my attention is this (shown below) as it's evident from the parameter names that these are some internal server URLs and IPs.

![strings](https://imgur.com/gZ9wFt5.png)

Since most of them were AWS Public IP addresses, I ran a Port scan in the background and started browsing them one by one to see if I find anything useful on the server - 80/443.  
Surprisingly one of them had an open directory on the Webroot and an interesting path. Let's call that `admsystem`.

From the name and the contents, it looked like a directory listing for the admin panel of the website. This is in itself a serious issue but I thought of probing deeper to see if I can leverage anything inside to get more access to the server.

Browsing the directory and its contents an interesting file caught my attention - `/tools/cron/html/cron.html`

This page had a title of `Redacted Internal Cron Job UI` and looked like an internal admin panel to create Cron Jobs.

![cron](https://imgur.com/rkxNs4T.png)

To do a quick check if the commands are actually being executed on the server, I tried a simple curl instead of getting a full shell in their restricted environment which was out of scope.  
`curl http://my-server/test?out=`whoami`` and got a response on my server as`www-data`.

This is where I stopped all my attempts and the issue was reported. It should be noted that we are still in the internal domain of the application and this was not in scope.

This is where my teammate Selvie ([@FetaSelvie](https://twitter.com/FetaSelvie)) helped.

The next day when we were carrying out this Pentest, we were testing `app.redacted.com` and Selvie found a call to `api.redacted.com/admsystem/provider.php` which was vulnerable to an IDOR.

Seeing the path `admsystem` we remembered it appearing in the internal server as well.  
So she tried to reach the internal Cron portal and send the same request to `api.redacted.com/tools/cron/html/cron.html`

![rce](https://imgur.com/iL0ot5i.png)

And there we have it, RCE on the production server.

[#tutorial](/tag/tutorial)[#hacking](/tag/hacking)[#security](/tag/security)[#android](/tag/android)[#webdev](/tag/webdev)

 __2.3K views
