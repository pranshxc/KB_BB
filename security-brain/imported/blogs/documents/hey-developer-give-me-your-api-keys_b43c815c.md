---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-18_hey-developer-give-me-your-api-keys.md
original_filename: 2018-07-18_hey-developer-give-me-your-api-keys.md
title: Hey Developer, Give me your API keys.!!
category: documents
detected_topics:
- api-security
- command-injection
- information-disclosure
- cloud-security
- mobile-security
tags:
- imported
- documents
- api-security
- command-injection
- information-disclosure
- cloud-security
- mobile-security
language: en
raw_sha256: b43c815cd9d4d7533bd814150eaacc47e3374014fbd5ad576f39088547cc5e31
text_sha256: 00132a2557da8dc8753edac0239c7360dbf4234c54c0e32a2e7965c0dde5a2b5
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: true
---

# Hey Developer, Give me your API keys.!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-18_hey-developer-give-me-your-api-keys.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, information-disclosure, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: True
- Raw SHA256: `b43c815cd9d4d7533bd814150eaacc47e3374014fbd5ad576f39088547cc5e31`
- Text SHA256: `00132a2557da8dc8753edac0239c7360dbf4234c54c0e32a2e7965c0dde5a2b5`


## Content

---
title: "Hey Developer, Give me your API keys.!!"
url: "https://medium.com/devanshwolf/hey-developer-give-me-your-api-keys-b8c99ab1c4f5"
authors: ["Devansh batham (@devanshwolf)"]
programs: ["Crowdin"]
bugs: ["Information disclosure"]
publication_date: "2018-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5803
scraped_via: "browseros"
---

# Hey Developer, Give me your API keys.!!

Hey Developer, Give me your API keys.!!
Devansh batham
Follow
4 min read
·
Jul 18, 2018

218

1

TL;DR

This is just another friendly article, without any secret “Ninja” techniques..!!

Credits : thanks to security team of Infoziant Labs for consistent support..!

DISCLAIMER : In this blog post I am not gonna talk about any advance stuff ,neither any secret techniques, this blog is all about , how developers sometimes make silly mistakes..(after all developers are human too :P )!!

Now, some of you might say , :

Okay, okay . Hold on ..!! and read the full article..!!

Every year we notice data breaches,hacks,ransomware attacks on big IT giants , In most of the hacks , the reasons are Server side system vulnerabilties,Client side flaws of the application, and social engineering too..!!

img src Feedyeti.com

But there are few cases in which the reasons of these kind of attacks are just some silly mistakes made by developers, Like : leaving their secret API keys,AWS secret Keys,Mysql credentials,their slack channel’s credentials in their public respositories,

even am not an expert though

Later on in this post I will show you one of my recent findings , which illustrates how I found a secret api key of Crowdin’s test project , and succesfully pwned their test project. [The issue is Fixed now]

What worse can be done..!

In the past I had seen some cases, where developers left hardcoded credentials in android application of their company , which later gave me access to their admin dashboard,

credits to the creator of this meme :p

Some developers encode the api keys using Base64, and think the attacker will not be able to find the API keys, I mean are they serious, Base64 encoding is not the solution to these issues, Base64 encoded API keys can easily be decoded..!!

CREDITS TO “Rojan Rijal” for his blog post : https://sites.google.com/securifyinc.com/rojanrijal/finding-leaked-sensitive-data

Now let me narrate an interesting incident..!

“How I got complete access to Crowdin’s testproject[RUBYTESTAPI]” ..!!

What Crowdin is ?

“Crowdin is a localization management platform designed to automate localization within agile software development. With more than 1,000, 000 user accounts, platform is used by development companies in 140 countries”.

‘-for more info about crowdin read this : https://www.crunchbase.com/organization/crowdin-'

I decided to test crowdin for vulnerabilties , because they offer cool goodies pack for valid vulnerabilties..!!

Get Devansh batham’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I started finding some code level bugs in their github respositories , Soon I ended up with a page that is discosing their secret API key , here : https://github.com/crowdin/crowdin-api/blob/master/bin/console

Press enter or click to view image in full size

api_key=***REDACTED***
project_id = ‘rubytestapi’
base_url = ‘https://api.crowdin.com'

Note : This API key is now expired,

As you can see above I got api_key and project_id .At that moment ,I have no idea , How I can use this api key for accessing their project.. So I started reading their API docs here : https://support.crowdin.com/api/api-integration-setup/

Soon I found that I can takeover their project : “rubytestapi” , using API_key,

After reading their API docs , I am all set to takeover their test project.

For enumerating Project Details of their project “rubytestapi” , the request will be :

GET https://api.crowdin.com/api/project/{project-identifier}/info?key={project-key}

NOTE : the project-identifier is “rubytestapi” and the project-key is “79323cdcd6b4566154c4fb9c6bbd3be1” ,

When I sent that GET request using burp , I got a 200 OK response , and complete details of their project(“rubytestapi”)

POC :

Press enter or click to view image in full size
full info of their project “rubytestapi”

Now what can I do with their project (“rubytestapi”)

I can add files,delete files,upload translation,check translation status, and many other things (see here : https://support.crowdin.com/api/info/), In short, I had complete access to their project,

credits to the creator of this meme :p

Soon after the discovery , I first sent an email to crowdin to confirm that the rubytestapi project is owned by them or not. And within few minutes I got this response :

So it is clear that the project is owned by crowdin..!!

, I reported the issue to them along with Proof of Concept, They triaged and fixed the report within 1 hour(Kudos to them for their awesome response time)

I was rewarded with their Goodies pack , and got listed in their hall of fame :

Press enter or click to view image in full size
https://crowdin.com/page/hall-of-fame

MESSAGE TO ALL DEVELOPERS OUT THERE : “BE CAREFUL WHILE HANDLING API KEYS”

Also check out these awesome blogposts,

https://sites.google.com/securifyinc.com/rojanrijal/finding-leaked-sensitive-data
https://medium.freecodecamp.org/discovering-the-hidden-mine-of-credentials-and-sensitive-information-8e5ccfef2724

want to chat.? connect with me

Twitter : @devanshwolf

Facebook : Devansh Batham

./rgds

Devansh Batham(Infoziant Labs)

Have some penetration testing or security projects ? Give a shout to Infoziant Labs(Tony@infoziant.com)
