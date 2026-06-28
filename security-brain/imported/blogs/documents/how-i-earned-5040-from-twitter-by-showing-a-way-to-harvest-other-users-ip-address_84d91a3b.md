---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-07_how-i-earned-5040-from-twitter-by-showing-a-way-to-harvest-other-users-ip-addres.md
original_filename: 2018-11-07_how-i-earned-5040-from-twitter-by-showing-a-way-to-harvest-other-users-ip-addres.md
title: How I earned 5040$ from Twitter by showing a way to Harvest other users IP
  address
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 84d91a3b698ba77a80ddd35ea5897ae064b98de9a913b3d348fcdfb08bb37f17
text_sha256: f0f3a4f957a0dfd60d89dab59ccbd618674bfc3ccd1aa8812d2f1d27314ecbb8
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I earned 5040$ from Twitter by showing a way to Harvest other users IP address

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-07_how-i-earned-5040-from-twitter-by-showing-a-way-to-harvest-other-users-ip-addres.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `84d91a3b698ba77a80ddd35ea5897ae064b98de9a913b3d348fcdfb08bb37f17`
- Text SHA256: `f0f3a4f957a0dfd60d89dab59ccbd618674bfc3ccd1aa8812d2f1d27314ecbb8`


## Content

---
title: "How I earned 5040$ from Twitter by showing a way to Harvest other users IP address"
url: "https://medium.com/bugbountywriteup/how-i-earned-5040-from-twitter-by-showing-a-way-to-harvest-other-users-ip-address-e9f43c931e9a"
authors: ["Prial Islam Khan (@prial261)"]
programs: ["Twitter"]
bugs: ["Information disclosure"]
bounty: "5,040"
publication_date: "2018-11-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5602
scraped_via: "browseros"
---

# How I earned 5040$ from Twitter by showing a way to Harvest other users IP address

How I earned 5040$ from Twitter by showing a way to Harvest other users IP address
Prial Islam Khan
Follow
2 min read
·
Nov 8, 2018

300

1

Hi guys ,

This is Prial Islam a security researcher from Bangladesh . This is a old finding of mine adding into my blog . Recently I disclosed a POC on How I was able to get all vine users sensitive Information including Phone no/ IP Address / Emails and Many more what was reported to twitter and they patched it and rewarded me 7560$ . Those who missed it you can get the Orginal Report Here .

Today I am going to disclose another Information Disclosure vulnerability what was reported by me to Twitter Security team in their Bug Bounty Program in Hackerone and they Rewarded me with a amount of 5040$ for this report .

When I testing vine API Endpoints I noticed a Endpoint what uses in Vine Repost mechanism have a Parameter Named “ipAddress” with some plain Number value Like :- 2130706433 . We all know Ip Addresses look like :- 127.0.0.1 . But the value of the “ipAddress” looks invalid . Then when I tried to search about it on google I came to know that the value is valid . Actually it was Converted to IP Address to Long/Decimal format . So I used a Online Converter tools and was able to get the real Ip . ( Online Converter I used )

Vulnerable Endpoint : https://vine.co/api/timelines/users/<POST ID>

Get Prial Islam Khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Reproduce :

TO reproduce this issue victim User have to repost any vine in his timeline and a lot of vine users reposted many Vine post in their timeline .
So Copy a Reposted Vine POST ID and place it in the Endpoint and visit it . Example : https://vine.co/api/timelines/users/1293308695089926144
Now when I visited the link I got a response like below (The sensitive contents were removed by twitter security team ) :-
“repost”: { “username”: “██████”, “verified”: 0, “vanityUrls”: [], “created”: “█████”, “repostId”: ████████, “avatarUrl”: “██████”, “userId”: ████, “user”: { “username”: “█████████”, “verified”: 0, “vanityUrls”: [], “avatarUrl”: “█████████”, “userId”: ████, “private”: 0, “location”: █████████ }, “flags|platform_lo”: 1, “postId”: ███, “ipAddress”: 2130706433 , “flags|platform_hi”: 1 }
As you can see the ipAddress parameter value is converted now Just Use my give online tool to again convert it to valid ip address value .

I reported this issue in Jan 26th and they paid me 5040$ for reporting this on Feb 25th .

Press enter or click to view image in full size
$$$$ 👊

Thanks for reading . Happy Hunting .
