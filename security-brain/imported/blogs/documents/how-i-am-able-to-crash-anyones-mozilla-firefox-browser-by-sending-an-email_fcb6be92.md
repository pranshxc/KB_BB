---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-30_how-i-am-able-to-crash-anyones-mozilla-firefox-browser-by-sending-an-email.md
original_filename: 2021-12-30_how-i-am-able-to-crash-anyones-mozilla-firefox-browser-by-sending-an-email.md
title: How I Am Able To Crash Anyone’s Mozilla Firefox Browser By Sending An Email
category: documents
detected_topics:
- command-injection
- automation-abuse
tags:
- imported
- documents
- command-injection
- automation-abuse
language: en
raw_sha256: fcb6be9244db0f20d792e287775fa62429c42f0a8340f31b88d6b87596d9e831
text_sha256: 3da0705a29d25d0c57c98aedf7bdc88c1b3387b8ed04fd5e856ea0ec0c2b2b48
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I Am Able To Crash Anyone’s Mozilla Firefox Browser By Sending An Email

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-30_how-i-am-able-to-crash-anyones-mozilla-firefox-browser-by-sending-an-email.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `fcb6be9244db0f20d792e287775fa62429c42f0a8340f31b88d6b87596d9e831`
- Text SHA256: `3da0705a29d25d0c57c98aedf7bdc88c1b3387b8ed04fd5e856ea0ec0c2b2b48`


## Content

---
title: "How I Am Able To Crash Anyone’s Mozilla Firefox Browser By Sending An Email"
page_title: "HOW I AM ABLE TO CRASH ANYONE’S MOZILLA FIREFOX BROWSER BY SENDING AN EMAIL | by Sam | InfoSec Write-ups"
url: "https://medium.com/@sam0-0/how-i-am-able-to-crash-anyones-mozilla-firefox-browser-by-sending-an-email-a12563cc8d79"
authors: ["Sam"]
programs: ["Mozilla"]
bugs: ["DoS"]
publication_date: "2021-12-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3049
scraped_via: "browseros"
---

# How I Am Able To Crash Anyone’s Mozilla Firefox Browser By Sending An Email

HOW I AM ABLE TO CRASH ANYONE’S MOZILLA FIREFOX BROWSER BY SENDING AN EMAIL
Sam
Follow
2 min read
·
Dec 30, 2021

60

Hi, Hope you guys are doing well, Here is the story of how I am able to crash anyone’s Mozilla firefox by just sending a single email.. let’s start.

I am hunting on google’s Gmail, And after 3 days of trying I am not able to find anything, then I just randomly thought to put a lot of emojis in a single email and send it to someone to see what happens. I just used a very large number of emojis and special characters like this :

You can download the payload file here: https://github.com/SAM0-0/payloads

Press enter or click to view image in full size

At first thought google can handle anything like this, Still, I tried to do it,

I added a lot of emojis to the title of the email and body of the email.

Get Sam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And sent it to my second account, I always use firefox So I opened the second email in hope that it will crash and boom💥. My firefox just crashed by just clicking on the received email. So I tested the same thing on chrome and what? It’s not working on chrome, Everything is just working smoothly, Then I tried on duckduckgo and boom 💥 , Crashed it, Then tried on people’s favorite browsers windows explorer, and EDGE both are crashing too, danggg.

And I was like :

I’ve reported this to firefox and they took it as a performance upgrade and not as a security issue😥, But they fixed it in firefox version 93 as a new upgrade, Yay!!!!!

Press enter or click to view image in full size

As they said firefox is loading every single emoji as an image, so it is the main cause of the crash, As I understood.

I hope you guys enjoyed the post! Stay tuned for more writeups. Will publish many soon.

Thanks for reading and please ignore any mistakes and my grammar too😅, You guyz can follow me on Twitter: @__sam0_0
