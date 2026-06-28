---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-03_forcing-for-a-bounty.md
original_filename: 2020-11-03_forcing-for-a-bounty.md
title: Forcing for a bounty$$
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 312ccc885456db9c69828bb1954b2531ceeb6ee73a71d2192b3e265cfb3c069c
text_sha256: 5c24674bd216f0f8d53fff0e52b6065b275d3a864a8b46f809ec963a693352de
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Forcing for a bounty$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-03_forcing-for-a-bounty.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `312ccc885456db9c69828bb1954b2531ceeb6ee73a71d2192b3e265cfb3c069c`
- Text SHA256: `5c24674bd216f0f8d53fff0e52b6065b275d3a864a8b46f809ec963a693352de`


## Content

---
title: "Forcing for a bounty$$"
url: "https://rafi-ahamed.medium.com/forcing-for-a-bounty-b637c468d7bd"
authors: ["Rafi Ahamed (Leonidas D. Ace)"]
bugs: ["Broken authorization"]
bounty: "500"
publication_date: "2020-11-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4160
scraped_via: "browseros"
---

# Forcing for a bounty$$

Forcing for a bounty$$
Rafi Ahamed (Leonidas D. Ace)
Follow
2 min read
·
Nov 3, 2020

192

1

Hola fellow researchers,

Myself, Rafi Ahamed. I am a Cyber Security Researcher from Bangladesh. I am a currently doing my BBA from University of Dhaka. But I do love nerdy stuffs. Let’s not waste any time & get down to our topic.

First of all, don’t get confused with the title. By forcing I actually meant Forced Browsing.

What is Forced Browsing?

F
orced browsing is an attack where the attacker aim to enumerate and access resources that are not referenced by the application, but are still accessible.

How did I find the bug?

Recently I was testing a private site in HackerOne and the site was selling educational videos. So, they allow an user a preview of the video without payment. But the preview was for only 15 seconds or less. Well, who cares about that right?

Actually, that’s where the $$$ lies.

Get Rafi Ahamed (Leonidas D. Ace)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As usual I turned on Interception using Burp Suite & noticed endpoints like below:

Press enter or click to view image in full size

But the endpoint was on another subdomain. By looking at the subdomain name it was understood that the organization uses this subdomain to store all it’s videos & other stuffs. So, I quickly visited the endpoint to see if I can find anything.

Press enter or click to view image in full size
The endpoint

But I got nothing. Got the same preview with the same duration.

Then I noticed that the endpoint has something like this

Press enter or click to view image in full size

I thought why not remove it & see what happens. I was surprised that I got the full video. Now I can watch any paid video without payment.

I quickly reported the bug to HackerOne & got a nice $500 bounty.

Reported: Sep 27th.

Triaged: Sep 28th.

Resolved: Oct 18th.

Hope you guys enjoyed this one . PM me at Facebook or LinkedIn anytime if you have any questions .

#Eat_sleep_hack_repeat
#Hack’em all
