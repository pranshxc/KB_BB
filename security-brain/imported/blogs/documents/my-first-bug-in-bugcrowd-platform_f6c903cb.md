---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-21_my-first-bug-in-bugcrowd-platform.md
original_filename: 2022-12-21_my-first-bug-in-bugcrowd-platform.md
title: My First Bug In Bugcrowd Platform
category: documents
detected_topics:
- xss
- command-injection
- race-condition
tags:
- imported
- documents
- xss
- command-injection
- race-condition
language: en
raw_sha256: f6c903cb0cb7d096a992cfaf95bfd6d29753d4dd7bbcae7ed2291a4cf15ea159
text_sha256: 60f38dcf3813333524d1013d7797d248806206fb0be15506c4000321fb4edade
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# My First Bug In Bugcrowd Platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-21_my-first-bug-in-bugcrowd-platform.md
- Source Type: markdown
- Detected Topics: xss, command-injection, race-condition
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `f6c903cb0cb7d096a992cfaf95bfd6d29753d4dd7bbcae7ed2291a4cf15ea159`
- Text SHA256: `60f38dcf3813333524d1013d7797d248806206fb0be15506c4000321fb4edade`


## Content

---
title: "My First Bug In Bugcrowd Platform"
url: "https://medium.com/@EX_097/my-first-bug-in-bugcrowd-76decc1f9901"
authors: ["EX_097"]
bugs: ["Race condition"]
publication_date: "2022-12-21"
added_date: "2022-12-23"
source: "pentester.land/writeups.json"
original_index: 1754
scraped_via: "browseros"
---

# My First Bug In Bugcrowd Platform

My First Bug In Bugcrowd Platform
EX_097
Follow
2 min read
·
Dec 22, 2022

60

Hi Everybody

My name is Ahmed Nasreddin . I’m bug bounty hunter . today i will tell you about first bug in bugcrowd platform this is story about Race Condition Attack .

First What Is Race Condition Attack ?

A race condition attack happens when a computing system that’s designed to handle tasks in a specific sequence is forced to perform two or more operations simultaneously. Eventually, the application is forced to perform unintended actions. This leads the application to security exploitation.

The Story Of My Capture

My target is the public program in bugcrowd but the vulnerability is not fixed yet let’s name it : Target.com

This target have a small scope. and the vulnerability who reported is 14 reports. This is the reason why I don’t start searching for xss.

The first thing I advise you to do before you start looking for bugs is understand the site . So I created an account and started browsing the website. I found that this website gives you 30 days for experimentation. The website offers the service of creating database servers. You have a certain number of servers ’’10 serevers’’ that you can create. If you want to get more servers, you must upgrade your account, and you will have to pay more than $200 per month for that.

Get EX_097’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s Attacking

Since the target specific a number of servers that you can create, why don’t we try to bypass that ?

I deleted all the servers I created to understand the target. After that I created a new server but this time I intercepted the request by burp.

Press enter or click to view image in full size

Then I send the request to turbo intruder “Extension in burp”. from list of scripts i choose Race script and configuration it and started attack .

Press enter or click to view image in full size

When the attack ended, I refreshed the page and I found that 30 servers had been created
Quickly I create a report and reported the vulnerability after half time yes it’s triaged and it’s p3.

Press enter or click to view image in full size
Triaged Email

Now Goodbye to a new story : )

Linkedin : https://www.linkedin.com/in/ahmed-ali-2a9627141/
