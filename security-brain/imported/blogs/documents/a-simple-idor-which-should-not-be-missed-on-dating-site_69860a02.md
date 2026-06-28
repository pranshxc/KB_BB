---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-26_a-simple-idor-which-should-not-be-missed-on-dating-site-.md
original_filename: 2020-07-26_a-simple-idor-which-should-not-be-missed-on-dating-site-.md
title: A Simple IDOR which should not be missed on dating site ;)
category: documents
detected_topics:
- api-security
- idor
- command-injection
- information-disclosure
tags:
- imported
- documents
- api-security
- idor
- command-injection
- information-disclosure
language: en
raw_sha256: 69860a02159b2769178a90827d2ba924757bc4609121c13a12e611a29bc3de08
text_sha256: 38d8736ee00a99cbd7f3e44470b2edc555096186be05656ad051a3b2ef515431
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# A Simple IDOR which should not be missed on dating site ;)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-26_a-simple-idor-which-should-not-be-missed-on-dating-site-.md
- Source Type: markdown
- Detected Topics: api-security, idor, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `69860a02159b2769178a90827d2ba924757bc4609121c13a12e611a29bc3de08`
- Text SHA256: `38d8736ee00a99cbd7f3e44470b2edc555096186be05656ad051a3b2ef515431`


## Content

---
title: "A Simple IDOR which should not be missed on dating site ;)"
url: "https://medium.com/@vneelam609/a-simple-idor-which-should-not-be-missed-on-dating-site-c500cba8e6c3"
authors: ["neelam"]
bugs: ["IDOR", "Information disclosure"]
publication_date: "2020-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4386
scraped_via: "browseros"
---

# A Simple IDOR which should not be missed on dating site ;)

Member-only story

neelam
Follow
3 min read
·
Jul 26, 2020

297

2

A Simple IDOR which should not be missed on dating App ;)

Hello Again!!!

I am writing this article to give you tips on finding simple vulnerabilities.

So let’s check out how I found idor!!

It was very easy to identify endpoint for idor but how you can make it acceptable is important :D

This dating app was showing the user’s details based on some random number in this case, I just needed to identify if it’s showing other user's details or not.

Although many API endpoints were having such issues but most of them were showing publicly disclosed information.

finally, I found one interesting endpoint where you can see the user’s list of details After looking at the response there were many things showing up about user which was already publicly known for example- user’s profile name, age, city, etc.

So as I keep scowling down I saw something interesting as shown in POC

Press enter or click to view image in full size
User 1

In user 1 you can see some of the unread messages, notifications, new visits etc were showing in response which was my currently logged in user details.

Press enter or click to view image in full size
User 2
