---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-19_how-i-get-my-first-swag-from-sidn-sensitive-data-exposer.md
original_filename: 2022-02-19_how-i-get-my-first-swag-from-sidn-sensitive-data-exposer.md
title: How I get my first SWAG from SIDN (Sensitive Data Exposer)
category: documents
detected_topics:
- information-disclosure
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- information-disclosure
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 9837c61d8bc2a3267ca6144d2b93a7cd02fb47633700df756256ba65c3a1d7ed
text_sha256: 6c972b2d2715fe31f8667ed7f2f7d49ef750c95a12223d1b0acc3efaf4328d09
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# How I get my first SWAG from SIDN (Sensitive Data Exposer)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-19_how-i-get-my-first-swag-from-sidn-sensitive-data-exposer.md
- Source Type: markdown
- Detected Topics: information-disclosure, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `9837c61d8bc2a3267ca6144d2b93a7cd02fb47633700df756256ba65c3a1d7ed`
- Text SHA256: `6c972b2d2715fe31f8667ed7f2f7d49ef750c95a12223d1b0acc3efaf4328d09`


## Content

---
title: "How I get my first SWAG from SIDN (Sensitive Data Exposer)"
page_title: "How I get my first SWAG from SIDN (Sensitive Data Exposer) | remonsec"
url: "https://remonsec.com/posts/getting-first-swag-SIDN/"
final_url: "https://remonsec.com/posts/getting-first-swag-SIDN/"
authors: ["remonsec (@remonsec)"]
programs: ["SIDN"]
bugs: ["Directory listing", "Information disclosure", "403 bypass"]
publication_date: "2022-02-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2890
---

## How I get my first SWAG from SIDN (Sensitive Data Expose)__

**بسم الله الرحمن الرحيم**

##  Introduction __

Assalamu Alaikum (Peace Be Upon You)

I am Mehedi Hasan Remon. Student of Computer Science Engineering. I am learning about Web Penetration Testing and doing Bug Bounty as a side activity.

Let’s start the story

[](https://media2.giphy.com/media/XyaQAnihoZBU3GmFPl/giphy.webp)

## Background __

I just weak up and start scrolling on my Facebook timeline. I saw someone posted in the Bug Bounty Poc group that he got a SWAG from SIDN for reporting a vulnerability. That T-Shirt was really awesome and I also have a friend[**Asif Farabi**](https://www.facebook.com/asiffarabi000) who has that same SWAG from SIDN. So my mind said “Let’s Give it a Shot”

## How I found the Bug __

I fire up my Kali Linux, start my recon with[**Sublist3r**](https://github.com/aboul3la/Sublist3r)

From Sublist3r I found an interesting domain called mailman.sidn.nl

[](https://postimg.cc/v4hxHmqg)

After playing around the target I found a directory called mailman.sidn.nl/pipermail But there was a 403 for that directory

[](https://postimg.cc/Thby50NX)

But then I put a ‘/’ after the pipermail directory Like This: mailman.sidn.nl/pipermail/

[](https://postimg.cc/7JrZNvtr)

Boom … It takes me inside the directory. Inside that directory, I found lots of private emails about the company. like their product relates emails, production emails, internal dev mails, etc.

[](https://postimg.cc/bs8vDh2Q)

Then immediately I send them that Bug Report and asked Allah for the success

[](https://postimg.cc/Jtjnzntr)

And then Alhamdulillah (all praise is due to Allah) Got this sweet SWAG

[](https://postimg.cc/Js0MZ47B)

[](https://postimg.cc/YGz92rzD)

[](https://postimg.cc/3dnvCBpf)

## Bug POC __

[](https://www.youtube.com/watch?v=J30KmyQetO0)

## Conclusion __

Thanks for reading till the end. If you want something then just take the action for it. Don’t just keep thinking that I will do it, I will do it. Work Hard Try Insane Rest of all your lord will decide

Be Secure Be Safe Allah Hafiz (May Allah be your Protector)

Report: Jan / 21 / 2020 Trigger: Jan / 21 / 2020 Receive Swag: Jan / 29 / 2020

* * *

wanna support my work! well just buy me a coffee

[](https://www.buymeacoffee.com/remonsec)
