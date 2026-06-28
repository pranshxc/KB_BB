---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-21_google-assistant-bug-worth-31337-.md
original_filename: 2018-07-21_google-assistant-bug-worth-31337-.md
title: Google Assistant Bug Worth $3133.7 !
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 900edaf0d6eadc38cf70b5cbc427be3f57db29d25804f3e97161de6cadf959d3
text_sha256: a0e42b8879a8433f4a7e27bef4cd2b8d4b243530913662d8c2f23277ead96237
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Google Assistant Bug Worth $3133.7 !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-21_google-assistant-bug-worth-31337-.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `900edaf0d6eadc38cf70b5cbc427be3f57db29d25804f3e97161de6cadf959d3`
- Text SHA256: `a0e42b8879a8433f4a7e27bef4cd2b8d4b243530913662d8c2f23277ead96237`


## Content

---
title: "Google Assistant Bug Worth $3133.7 !"
url: "https://medium.com/bug-bounty-hunting/google-assistant-bug-worth-3133-7-830a03724a04"
authors: ["Circle Ninja (@circleninja)"]
programs: ["Google"]
bugs: ["Reflected XSS"]
bounty: "3,133.7"
publication_date: "2018-07-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5796
scraped_via: "browseros"
---

# Google Assistant Bug Worth $3133.7 !

Google Assistant Bug Worth $3133.7 !
Ronnie Joseph
Follow
2 min read
·
Jul 21, 2018

273

2

Hi hackers! Long time no see..

Press enter or click to view image in full size
Actions Google XSS

You may well be aware of Google Assistant . This is a writeup of reflected XSS which I found in console.actions.google.com .

My college Prof. asked me to conduct some useful workshop for students. After a quick search, I figured out on the workshop as “Making apps using Google Assistant”. The documentation provided was very easy to follow and so it would have been easily grasped by learners. So I was making a test app using Assistant Web Console.

I was very lucky to find the XSS as just after one week, Google started to extensively market Assistant via major youtube channels. :P

I will directly go the bug i.e XSS.

Get Ronnie Joseph’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

There were many options and inputs like App name, link ,description etc.

Press enter or click to view image in full size
New Assistant Console|XSS was in Old

I started saving some payloads on each field. I soon realized that no tags were filtered <> etc. But the XSS never popped. :(

After some time, I used data uri and base 64 encoding to create XSS . Clicking on the link got XSS.

The payload-

“><a href=”data:text/html;base64,PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=”>click</a>

By the way the workshop was a success by God’s grace! And true was someone who said help others, you will get your reward in unexpected ways.

You are always welcome to contribute in this not for profit publication. Please DM me on Twitter.
