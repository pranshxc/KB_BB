---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-30_stored-xss-at-httpswwwtiktokcom-the-name-of-the-attackers-account-carrying-xss-p.md
original_filename: 2022-11-30_stored-xss-at-httpswwwtiktokcom-the-name-of-the-attackers-account-carrying-xss-p.md
title: Stored XSS at https://www.tiktok.com/ the name of the attacker’s account carrying
  XSS payload will be triggered when the victim Send Video
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 05027c50db7f5200c30faece7e7591a3dfb916bd44b47035df24d18ae0776c7d
text_sha256: 15c398a933f013e2c3f1227426875f2f2766c0389b9b289b594c75290b38ba08
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS at https://www.tiktok.com/ the name of the attacker’s account carrying XSS payload will be triggered when the victim Send Video

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-30_stored-xss-at-httpswwwtiktokcom-the-name-of-the-attackers-account-carrying-xss-p.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `05027c50db7f5200c30faece7e7591a3dfb916bd44b47035df24d18ae0776c7d`
- Text SHA256: `15c398a933f013e2c3f1227426875f2f2766c0389b9b289b594c75290b38ba08`


## Content

---
title: "Stored XSS at https://www.tiktok.com/ the name of the attacker’s account carrying XSS payload will be triggered when the victim Send Video"
url: "https://aidilarf.medium.com/stored-xss-at-https-www-tiktok-com-11fed6db0590"
authors: ["Aidil Arief"]
programs: ["TikTok"]
bugs: ["Stored XSS"]
bounty: "500"
publication_date: "2022-11-30"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 1838
scraped_via: "browseros"
---

# Stored XSS at https://www.tiktok.com/ the name of the attacker’s account carrying XSS payload will be triggered when the victim Send Video

Stored XSS at https://www.tiktok.com/ the name of the attacker’s account carrying XSS payload will be triggered when the victim Send Video
Aidil Arief
Follow
3 min read
·
Nov 30, 2022

304

6

Hi everyone,

When I decided to do some Bug Hunting on the TikTok program, and I got some XSS Stored in a few months.

Press enter or click to view image in full size

After waiting for so long to disclose these findings, and finally, this article is disclosed.

Follow Me :)

Press enter or click to view image in full size

This finding is my first finding, but because there is a delay in the Disclosure and Fix process, the Disclosure of this finding is a bit late. Here are my other findings that have already been disclosed.

XSS Blind Stored at 2 Assets TikTok
Hi everyone,

aidilarf.medium.com

XSS Blind Stored at Asset Domain Android Apps TikTok
Hi everyone

aidilarf.medium.com

This finding started when I tried to rename my TikTok account to one that carries XSS payload.

Press enter or click to view image in full size

I think the way I did was a stupid and time consuming way to scan for vulnerable output.

Get Aidil Arief’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After a long time trying to find the output of the name that carries the XSS payload, and I can’t find any XSS vulnerabilities there.

I decided to pause for a moment by trying to look back at some of the existing features.

And until finally I saw a vulnerable output, where the name of the TikTok account carrying the XSS payload was treated as HTML.

Press enter or click to view image in full size

See the TikTok name output carrying the XSS payload is considered HTML. However when I try to use SCRIPT TAG. And the pop up doesn’t appear. I tried using another payload and see the result :

Press enter or click to view image in full size

And Pop Up appears.

I was very excited and immediately reported this to the TikTok Team.

Report :

TikTok disclosed on HackerOne: Stored XSS Payload when sending videos
A Cross-Site Scripting (XSS) payload was found via the text used when sending videos to a friend, which could have…

hackerone.com

Timeline :

Report : Apr 9th

Triaged : Apr 26th

Fix : Jul 8th

Resolved : Fixed
