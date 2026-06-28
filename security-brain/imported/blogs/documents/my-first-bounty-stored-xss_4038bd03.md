---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-14_my-first-bounty-stored-xss.md
original_filename: 2021-02-14_my-first-bounty-stored-xss.md
title: My first bounty (stored-xss)
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 4038bd03dbfc92c73396e8af5f8a5a25f480ae0dae786a93cd7ad97fc5af0c11
text_sha256: 37af2c33a57d8494b5e25825785afff0e8b9f3c0743deaaea96697cbf0c0788c
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# My first bounty (stored-xss)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-14_my-first-bounty-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `4038bd03dbfc92c73396e8af5f8a5a25f480ae0dae786a93cd7ad97fc5af0c11`
- Text SHA256: `37af2c33a57d8494b5e25825785afff0e8b9f3c0743deaaea96697cbf0c0788c`


## Content

---
title: "My first bounty (stored-xss)"
url: "https://karansh491.medium.com/my-first-bounty-stored-xss-96dea41fd9cf"
authors: ["Karan sharma (@karansh491)"]
bugs: ["Stored XSS"]
bounty: "1,000"
publication_date: "2021-02-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3908
scraped_via: "browseros"
---

# My first bounty (stored-xss)

Photo by Miguel Orós on Unsplash
My first bounty (stored-xss)
Karansh
Follow
2 min read
·
Feb 16, 2021

124

Hi i’m Karan sharma. My first bounty was based on stored-xss, let’s talk about it.

So i’m very new to bug bounty and I actually started hunting on paid targets a month ago via hackerone.

I picked a private target based on actual application’s functionality, as I suck at reconnaissance.

How I found the xss

I was testing as usual, getting familiar with different features of application.

But there was this feature where user can create hierarchal steps and can link those steps with other functions like displaying date and other stuff…

There was one more interesting feature where user can import & export the steps in form of XML files.

So I created some steps and exported it.

In XML file, each steps was a tag and bunch of metadata… I tried the classic xss payload but It breaks the XML formal.

Get Karansh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now what!!? Then I thought about encoding the special characters so it won’t break the structure; i.e. < will be &lt;

So final payload will be &lt;img src=x onerror=alert(document.domain)&gt;

After importing the XML file with payload, huh! It won’t trigger 🧐

At least not on same page, It actually triggered on different page where user can print the whole steps.

Scenario: Now attacker (any member with just import/export permission) can import the XML file and send the link of print-page to other members / victims including ADMIN (owner).

reward: $1000

I brought something with my first bounty, check it out here:

MacBook Air M1
A big thanks to some the people from #infosec community, these guys help me stay motivated:

hunter0x7, HusseiN98D and two friends of mine 🎃

Thank you for reading!
