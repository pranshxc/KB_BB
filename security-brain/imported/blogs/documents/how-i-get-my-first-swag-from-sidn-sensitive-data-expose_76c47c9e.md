---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-29_how-i-get-my-first-swag-from-sidn-sensitive-data-expose.md
original_filename: 2020-01-29_how-i-get-my-first-swag-from-sidn-sensitive-data-expose.md
title: How I get my first SWAG from SIDN (Sensitive Data Expose)
category: documents
detected_topics:
- access-control
- command-injection
- information-disclosure
- api-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- information-disclosure
- api-security
- supply-chain
language: en
raw_sha256: 76c47c9eaaa5e3b9432f42093a6f9c9d8b544cdc77d1c7954359b2aa1e83e6f2
text_sha256: 11057051e7f8af9300c9d27a136fc985586a75ddfe43d5677d7fd06c47e60e2b
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I get my first SWAG from SIDN (Sensitive Data Expose)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-29_how-i-get-my-first-swag-from-sidn-sensitive-data-expose.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, information-disclosure, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `76c47c9eaaa5e3b9432f42093a6f9c9d8b544cdc77d1c7954359b2aa1e83e6f2`
- Text SHA256: `11057051e7f8af9300c9d27a136fc985586a75ddfe43d5677d7fd06c47e60e2b`


## Content

---
title: "How I get my first SWAG from SIDN (Sensitive Data Expose)"
url: "https://medium.com/@mehedi1194/how-i-get-my-first-swag-from-sidn-sensitive-data-expose-fc8e202fef85"
authors: ["Mehedi Hasan Remon (@mehedi1194)"]
programs: ["SIDN"]
bugs: ["Broken Access Control", "Information disclosure"]
publication_date: "2020-01-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4803
scraped_via: "browseros"
---

# How I get my first SWAG from SIDN (Sensitive Data Expose)

How I get my first SWAG from SIDN (Sensitive Data Expose)
Mehedi Hasan Remon
Follow
3 min read
·
Jan 29, 2020

371

5

بسم الله الرحمن الرحيم

Introduction

Assalamu Alaikum
(Peace Be Upon You)

I am Mehedi Hasan Remon.
Student of Computer Science Engineering. I am learning about Web Penetration Testing and doing Bug Bounty as a side activity.

Let's start the story

Background

I just woke up and start scrolling on my Facebook timeline. I saw someone posted in the Bug Bounty Poc group that he got a SWAG from SIDN for reporting a vulnerability. That T-Shirt was really awesome and I also have a friend Asif Farabi who has that same SWAG from SIDN. So my mind said
“Let’s Give it a Shot”

How I found the Bug

I fire up my Kali Linux, start my recon with Sublist3r

Get Mehedi Hasan Remon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

From Sublist3r I found an interesting domain called
mailman.sidn.nl

Press enter or click to view image in full size

After playing around the target I found a directory called
mailman.sidn.nl/pipermail
But there was a 403 for that directory

But then I put a ‘/’ after the pipermail directory
Like This: mailman.sidn.nl/pipermail/

It takes me inside the directory. Inside that directory, I found lots of private emails about the company. like their product relates emails, production emails, internal dev mails, etc.

Then immediately I send them that Bug Report and asked Allah for the success

Press enter or click to view image in full size

And then
Alhamdulillah (all praise is due to Allah)
Got this sweet SWAG

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Bug POC
Conclusion

Thanks for reading till the end. If you want something then just take the action for it. Don’t just keep thinking that I will do it, I will do it.
Work Hard
Try Insane
Rest of all your lord will decide

Be Secure Be Safe
Allah Hafiz (May Allah be your Protector)

Report: Jan / 21 / 2020
Trigger: Jan / 21 / 2020
Receive Swag: Jan / 29 / 2020
