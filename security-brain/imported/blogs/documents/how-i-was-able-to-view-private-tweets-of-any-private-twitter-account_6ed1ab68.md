---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-10-06_how-i-was-able-to-view-private-tweets-of-any-private-twitter-account.md
original_filename: 2017-10-06_how-i-was-able-to-view-private-tweets-of-any-private-twitter-account.md
title: How I Was Able To View Private Tweets Of Any Private Twitter Account
category: documents
detected_topics:
- xss
- idor
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- idor
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 6ed1ab68cfa4b0659c72b7c4fc085ccf61e5bf270f5742e369ba8c38f8a1efa3
text_sha256: ae5a9e08645ebc04d55d79ea1676f3e2a816351c15fe3118b3427b30aee509ea
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I Was Able To View Private Tweets Of Any Private Twitter Account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-10-06_how-i-was-able-to-view-private-tweets-of-any-private-twitter-account.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `6ed1ab68cfa4b0659c72b7c4fc085ccf61e5bf270f5742e369ba8c38f8a1efa3`
- Text SHA256: `ae5a9e08645ebc04d55d79ea1676f3e2a816351c15fe3118b3427b30aee509ea`


## Content

---
title: "How I Was Able To View Private Tweets Of Any Private Twitter Account"
url: "https://medium.com/secjuice/how-i-was-able-to-view-private-tweets-of-any-private-twitter-account-86a9d2640ded"
authors: ["Cj Legacion (@LegacionCj)"]
programs: ["Twitter"]
bugs: ["IDOR"]
publication_date: "2017-10-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6086
scraped_via: "browseros"
---

# How I Was Able To View Private Tweets Of Any Private Twitter Account

Cj Legacion
 highlighted

Press enter or click to view image in full size
Image by Diego Monzon
How I Was Able To View Private Tweets Of Any Private Twitter Account
Cj Legacion
Follow
4 min read
·
Oct 6, 2017

633

11

Did you ever tried to set your twitter account as private? Did you ever tried to tweet about your grievance to your boss, office mate, or anyone?

What if, one of them saw your tweets against them? Will you still trust your Social Media Account’s security?

I discovered a bug that will let anyone view other’s private tweets. And it’s easy as 1, 2, 3.

During my bug hunting in Twitter, I saw one of their subdomain “https://ads.twitter.com” and that subdomain is for posting or campaigns ads and etc in Twitter.

Back then, I tested this subdomain before i found this bug(Maybe month of march). So i have an idea what’s the use of this subdomain. Also i found the “HTML Injection and Possible XSS using IE” on it that i didn’t saw it once i am trying it on march and urgently ask filedescriptor for confirmation and reported it to Twitter(Fixed and Rewarded me a bounty).

This is the POC and i just used that payload for demonstration only.

Press enter or click to view image in full size

So let’s back to our topic. While i am waiting to reply from filedescriptor for a confirmation about the “HTML Injection and Possible XSS using IE” .

I tried to create a “Ad Groups” just for testing if their’s another XSS on it but i didn’t find any XSS Vulnerability on it.

But wait! I saw something that might be interesting while moving my mouse cursor and accidentally pointed to “Settings Button or what you are going to call it” and it’s showing “New”

Because of that, it makes me feel confused because there’s so many reason the something bothering my mind like “If it’s tested and reported by the others”. Also you know Twitter Acknowledgement or Hall of Fame is in the top of the list of achievements by many bug bounty hunters.

Get Cj Legacion’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So the final decision is

So i tried to check it and saw the a request

“userId” got my attention and urgently created another account for testing and change the value of parameter “userId”

and the response of the request

As you can see the “@LegacionTesting” and “Cj Legacion Testing” makes me feel and punching the person beside me

Then urgently created a Video POC and reported to Twitter. After their first response. It’s just 13–15 minutes and it’s fixed(That’s was the fastest resolved of my reports)

Are you confused about how i do it? So this is my Video POC for you so you can clearly understand it.
Video POC:

So that’s how easy it is for someone/attacker to view other’s private tweets. Also that’s the reason how i got my first laptop.

This vulnerability might be currently fixed by Twitter, but always remember. Everything is possible. Never underestimate the power of man in finding loopholes to any Security.

I also want to thank @filedescriptor and 
Shawar Khan
 for giving me a inspiration to test the Twitter again.

Kindly share if you like my first write-up. Also if there’s something wrong about this write-up just comment below. Also follow me on my Twitter Account for more write-up Thanks!

Web Security Researcher,
Cj Legacion

Editors Note: Put a WEBGAP between you and the malware with a browser isolation technology or by leveraging a remote browser service.
