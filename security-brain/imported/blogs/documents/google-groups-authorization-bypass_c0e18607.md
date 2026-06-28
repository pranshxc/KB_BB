---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-15_google-groups-authorization-bypass.md
original_filename: 2019-04-15_google-groups-authorization-bypass.md
title: Google Groups Authorization Bypass
category: documents
detected_topics:
- idor
- access-control
- command-injection
- rate-limit
- api-security
- supply-chain
tags:
- imported
- documents
- idor
- access-control
- command-injection
- rate-limit
- api-security
- supply-chain
language: en
raw_sha256: c0e186078e98bdede74731bf28557d39f626f537d69781e0c899c52f72cf9e9d
text_sha256: df69e2f2938341ecae64c359c664d2ff576ba6005f0b21fd331560001de76bf6
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Google Groups Authorization Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-15_google-groups-authorization-bypass.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, rate-limit, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `c0e186078e98bdede74731bf28557d39f626f537d69781e0c899c52f72cf9e9d`
- Text SHA256: `df69e2f2938341ecae64c359c664d2ff576ba6005f0b21fd331560001de76bf6`


## Content

---
title: "Google Groups Authorization Bypass"
url: "https://medium.com/@daniel.marad/post-komodosec-google-groups-authorization-bypass-500-bounty-adb371d16ab6"
authors: ["Daniel Marad"]
programs: ["Google"]
bugs: ["Broken authorization"]
bounty: "500"
publication_date: "2019-04-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5310
scraped_via: "browseros"
---

# Google Groups Authorization Bypass

Google Groups Authorization Bypass / $500 bounty|Komodosec
KomodoSec.com
Follow
4 min read
·
Apr 15, 2019

6

I’ve recently been playing around with Google services, poking here and there for security vulnerabilities. It’s been a quite a roller-coaster experience with some interesting results as well as some devastating rejections (I should definitely write a separate blog about those). Nevertheless, I’ve found one simple, but interesting auth-bypass on Google groups (that landed me a $500 bounty) that I think is worth sharing.

First things first: GWT

Have you ever heard of or played with Google Web Toolkit (GWT)? I have to admit that although it’s not exactly cutting-edge technology (in fact it’s been around from as early as 2006 and became open source in 2013), I had never really come across it before I started looking at Google products. When you first look at GWT HTTP requests they look, well… different. At first glance, they might even be intimidating. I mean, just look at this Googley witchcraft:

Googley witchcraft at its finest

Luckily, however, the age of GWT means that security research has already been done on it (I’ve even found an old OWASP ppt.), which helped me decipher some of the request elements.

Class enumeration is a nice start

Now that we have our bearings, let’s go back to Google-Groups. If you’ve never played with this service before, Google-Groups is basically a forum platform. You can create your own forums (‘groups’), invite participants to discuss topics, and manage the group’s permissions (decide who is allowed to view/update which thread). Oh, and yes, Google-Groups is built with GWT.

Generally speaking, my quick and dirty approach to manipulate GWT requests was to ‘stick to the middle,’ i.e. not to mess with the signature bit of the request (the pipe-separated numbers at the beginning and the end of the above body), but to stick to the parameters.

I quickly found a parameter worth manipulating. In the following GWT request, I discovered that the marked integer points to a specific class on the server-side:

Number ‘4’ points to ‘AbstractSearchKey’ class

Number ‘8’ points to ‘Shared.Categoty’ class

And so, I quickly launched a Burp-intruder session to extract classes’ names:

Want to add a caption to this image? Click the Settings icon.

Get KomodoSec.com’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While not a huge issue on its own (I’ve reported the issue to Google who justifiability deemed it “low risk”), it gave me the motivation to keep going and believing that I could find a gap in this GWT implementation.

Viewing other group’s data

Armed with my new confidence, I’ve looked back at the initial GWT request from before. One of the strings in the request was the name of a testing group I’d created:

yep, this ‘testestest….’ is the best name I could come-up with for my group

The response included basic information about the groups, including the group’s email, topic and description. But could I only view info about my own groups?

I quickly spawned a new group under a 2nd Google account (setting all permissions to ‘private,’ meaning that only invited users are allowed to view anything about the group), and then queried it from my 1st account. Turns out that authorization check was lacking, and I was able to extract some of the private group’s data:

Group’s data is available even without being a member

While auth-bypass is always nice, it’s not a critical issue. I wasn’t able to extract the group’s conversations, but only the group’s email and description (which might be sensitive). Still, it was my first GWT exploit (and one of my first Google bounties) and altogether quite a nice bug :)

Timeline:

January 21st — Bug reported to Google
January 21st — Bug was triaged
January 24th — Bug was accepted
February 5th — $500 bounty was granted

Originally published at www.komodosec.com.
