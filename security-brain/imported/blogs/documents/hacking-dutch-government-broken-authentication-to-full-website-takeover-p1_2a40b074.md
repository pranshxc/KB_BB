---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-26_hacking-dutch-government-broken-authentication-to-full-website-takeover-p1.md
original_filename: 2022-11-26_hacking-dutch-government-broken-authentication-to-full-website-takeover-p1.md
title: Hacking Dutch Government-Broken Authentication To Full Website Takeover (P1)
category: documents
detected_topics:
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 2a40b074f4c0bc8f41816d89c60f2408b6302a93574f768711c282d483556424
text_sha256: 9d221f200a09e45ddbf22279e7c89b6991ec52abaae5db133a30f75db4e70363
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Dutch Government-Broken Authentication To Full Website Takeover (P1)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-26_hacking-dutch-government-broken-authentication-to-full-website-takeover-p1.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `2a40b074f4c0bc8f41816d89c60f2408b6302a93574f768711c282d483556424`
- Text SHA256: `9d221f200a09e45ddbf22279e7c89b6991ec52abaae5db133a30f75db4e70363`


## Content

---
title: "Hacking Dutch Government-Broken Authentication To Full Website Takeover (P1)"
page_title: "My experience on Hacking Dutch Government | by n0rmh3ll | System Weakness"
url: "https://v1dr4x.medium.com/hacking-dutch-government-broken-authentication-to-full-website-takeover-p1-9af477604d54"
authors: ["V1dr4X"]
programs: ["Dutch Government"]
bugs: ["Exposed registration page"]
publication_date: "2022-11-26"
added_date: "2022-11-26"
source: "pentester.land/writeups.json"
original_index: 1860
scraped_via: "browseros"
---

# Hacking Dutch Government-Broken Authentication To Full Website Takeover (P1)

My experience on Hacking Dutch Government
n0rmh3ll
Follow
3 min read
·
Nov 26, 2022

279

Dutch Government

Hey guys ,

Today i’m gonna share my experience on hacking dutch government website.

T-shirt

Everything started when i saw a guy posted on twitter that he hacked dutch government . He also posted the T-shirt he got . Just look at the Quote line. The word “government” was the killer one. So now what, I need this swag badly.

I researched online for the scope and resources for this and ended up in a github repo where there is 1500+ scopes and active hosts of Dutch Gov websites. repo here.

The scope was large , but finding the correct one for testing was a hard part. But wait , At this time i was ready to give anything for that swag.

My Approach

To be honest , i was so confused about these 1500 hosts. so what is did is randomly selected 10 websites and start working on it. I got nothing in first 5 websites. but i was not going to giveup.

Actual game

After a while i got an intresting website . that was a normal responsive website. what caught me at first glance is, it look like kinda old .

Press enter or click to view image in full size

So i started testing on it’s features.

Get n0rmh3ll’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It was kind of blog website. then i searched for hidden directories and found an ‘Admin panel.

Press enter or click to view image in full size
Admin

It says to login with Netlify. Finally found a login page

The login page was actually more intresting than any others

Login

There was a sign up option in their page. hmm thats quite intresting as i’m familier with such situations in ctf’s.

sign up

I sign it up using my email and password. Now i try to login once more with email and pass i’ve just sign up.

and Voilaa !! i’m in

I’m in there cms and i have full admin acess control over the webpage.Then i quickly made a pov and reported to dutch gov And After 10 days they confirmed and fixed this bug . They also offer a T-shirt for me

Any way that was an awsome experience for me.

This was just a beginning of my journey

Stay tuned !’

-n0rmh3ll
