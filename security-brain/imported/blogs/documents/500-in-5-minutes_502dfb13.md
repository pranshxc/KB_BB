---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-01_500-in-5-minutes.md
original_filename: 2023-01-01_500-in-5-minutes.md
title: $500 in 5 minutes
category: documents
detected_topics:
- command-injection
- automation-abuse
tags:
- imported
- documents
- command-injection
- automation-abuse
language: en
raw_sha256: 502dfb13b70177de585c2ed33d5049a36a3bbf4dcc1f399ec3b87c3e558cdde1
text_sha256: 4d4bb5decf3a3abf3994dacfa27a7a3d170481c1f212bd98ecf6bd085ad7fad3
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# $500 in 5 minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-01_500-in-5-minutes.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `502dfb13b70177de585c2ed33d5049a36a3bbf4dcc1f399ec3b87c3e558cdde1`
- Text SHA256: `4d4bb5decf3a3abf3994dacfa27a7a3d170481c1f212bd98ecf6bd085ad7fad3`


## Content

---
title: "$500 in 5 minutes"
url: "https://medium.com/@coffeeaddict_exe/500-in-5-minutes-45977e89a337"
authors: ["CoffeeAddict"]
programs: ["Dropbox"]
bugs: ["Broken link hijacking"]
bounty: "500"
publication_date: "2023-01-01"
added_date: "2023-01-02"
source: "pentester.land/writeups.json"
original_index: 1715
scraped_via: "browseros"
---

# $500 in 5 minutes

$500 in 5 minutes
CoffeeAddict
Follow
2 min read
·
Jan 2, 2023

404

8

Extremely easy bug to find with good bounties.

Press enter or click to view image in full size
(Impersonation via Broken Link Hijacking)

Happy new year and hello 👋

This is my first bug bounty writeup, so I apologise if I make any mistakes. I hope this helps in your hunting methodology, so let’s get to it.

I have made this writeup to show how easy it is to find this bug and get that sweet bounty. The bug is impersonation via broken link hijacking.

It’s rated a P4 on Bugcrowd’s VRT, and I’m going to walk you through how I found it and some tools to help you find yours.

How i found it:

I was playing around on DropBox’s bug bounty program and noticed that there was a fairly recent update on their site and that there was another company, HelloSign, that had joined DropBox so I started looking into the social media icons and clicking on all of them when I saw that the Twitter account for HelloSign didn’t exist. So i took it over and made an account PoC.

( PoC video)

So it’s extremely simple to test for: simply locate the social media icons (usually at the bottom of the page) and click on all of them to see if the accounts exist; if not, you can perform a takeover by signing up in their username.

Get CoffeeAddict’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I reported it and got $300 from Dropbox, which was cool. After further testing on some of their subdomains, I found the same bug, but this time instead of Twitter, it was Facebook. I performed the exact same steps and reported it and got $200 for it.

Press enter or click to view image in full size

So in total a pretty good day with $500 in 5 minutes, so this is a good little bug to look out for.

Tool’s:

Looking out for this bug can get annoying if you have a large target with large subdomains, so there is a way to automate the process. There is a tool called SocialHunter that can automate this process. Props to an awesome hunter called at0m for a video on this tool: (https://www.youtube.com/watch?v=NSp4Mv2CfI8)

Press enter or click to view image in full size

Tool: https://github.com/utkusen/socialhunter

Thanks for reading hopefully this helps.

Best of luck ~ CoffeeAddict
