---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-25_weaponizing-xss-attacking-internal-system.md
original_filename: 2018-09-25_weaponizing-xss-attacking-internal-system.md
title: Weaponizing XSS Attacking Internal System
category: documents
detected_topics:
- xss
- sqli
- command-injection
tags:
- imported
- documents
- xss
- sqli
- command-injection
language: en
raw_sha256: bb0439e22aa14354b4c826c4467f38e15b6eb8cea72405c7b859f3f288bc0485
text_sha256: b28d6456009e4aa75bfaf9b332429a5550c8802201ab5136f9c0398124841de1
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Weaponizing XSS Attacking Internal System

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-25_weaponizing-xss-attacking-internal-system.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `bb0439e22aa14354b4c826c4467f38e15b6eb8cea72405c7b859f3f288bc0485`
- Text SHA256: `b28d6456009e4aa75bfaf9b332429a5550c8802201ab5136f9c0398124841de1`


## Content

---
title: "Weaponizing XSS Attacking Internal System"
url: "https://medium.com/@rahulraveendran06/weaponizing-xss-attacking-internal-domains-d8ba1cbd106d"
authors: ["Rahul R"]
bugs: ["Blind XSS"]
publication_date: "2018-09-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5682
scraped_via: "browseros"
---

# Weaponizing XSS Attacking Internal System

Weaponizing XSS Attacking Internal System
Rahul R
Follow
3 min read
·
Sep 25, 2018

380

1

Courtesy of BruteLogic ❤

Few week ago I was talking to a friend of mine when he gave me a subdomain that had an admin panel and asked me weather I could find a way to get inside, Why not give it a try.

So I stared my recon by doing Directory Scanning , Checking SQL injections , Checking if there is some vulnerable libraries and finally

Shit but I was curious to know more about it and I went to GOOGLE and searched for the company and gathered more info about the company even gave a connection request to the CTO via LinkedIn (we will get to the CTO in a minute)

While looking at the company website I saw a support panel where I can submit tickets somewhere in my head I was having a voice saying its vulnerable and I should test it.

Get Rahul R’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Hmm May be a Blind XSS so i went to my XSSHunter account and copied the payload and submitted the request I never had any hope of having a successful execution but the next day I logged in to my account to check if it was executed and BOOM .

I was able to grab the cookie of the user which I was able to impersonate and gain a valid session Boom inside Internal System.

Press enter or click to view image in full size

I registered an new account and submitted a Responsible Disclosure

After a Day I was greeted with one of the best messages that Ive ever got

Press enter or click to view image in full size
Press enter or click to view image in full size

This mail was actually by the CTO of the company a really cool guy who rewarded me for my finding,
