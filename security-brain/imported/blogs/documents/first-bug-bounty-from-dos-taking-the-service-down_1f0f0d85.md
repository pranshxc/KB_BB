---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-16_first-bug-bounty-from-dos-taking-the-service-down.md
original_filename: 2022-07-16_first-bug-bounty-from-dos-taking-the-service-down.md
title: 'First Bug Bounty from DOS: Taking the service down'
category: documents
detected_topics:
- command-injection
- mfa
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- mfa
- automation-abuse
- api-security
language: en
raw_sha256: 1f0f0d858d971d72751189c4257a4805480af328d587e96749fff69436349376
text_sha256: 14bbdbff30c36550f3c80b2c749b8becb70b5d3b5b528fd9f14518da4e4ad5f1
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# First Bug Bounty from DOS: Taking the service down

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-16_first-bug-bounty-from-dos-taking-the-service-down.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `1f0f0d858d971d72751189c4257a4805480af328d587e96749fff69436349376`
- Text SHA256: `14bbdbff30c36550f3c80b2c749b8becb70b5d3b5b528fd9f14518da4e4ad5f1`


## Content

---
title: "First Bug Bounty from DOS: Taking the service down"
url: "https://medium.com/@faique/first-bug-bounty-from-dos-taking-the-service-down-30f9ad4e0246"
authors: ["Faique (@imfaiqu3)"]
bugs: ["DoS"]
bounty: "200"
publication_date: "2022-07-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2444
scraped_via: "browseros"
---

# First Bug Bounty from DOS: Taking the service down

First Bug Bounty from DOS: Taking the service down
Faique
Follow
3 min read
·
Jul 16, 2022

170

4

Introduction

Hello friends, This is Faique, a security researcher & an ethical hacker from India, and this is a journey to my first bug bounty.
I can understand the pain and struggle newbie hunters face as I have gone through it. The past couple of months were not good for me as I was on bug bounties for almost a year but didn’t get any concrete results out of it, so this situation gave me a feeling of giving up, But yeah I stayed and the result is in front of you. For all newbie hunters, I have pro tips and resources for you at the bottom but for now, enjoy my write-up✌️

Found the target using google dorking, The target was similar to google map and had multiple domains in scope like

*.target.com
*.target.net
*.target.me

First of all, I gathered all subdomains and did some basic recon. Then I started to hunt for functionality-level bugs and didn’t find any. I got frustrated;( and stopped hunting that day.

The next day I grabbed a cup of coffee, did meditation and started to hunt again, gathered all waybackurls of domains, On analyzing the waybackurls I found photos.target.me domain had strange Urls, the link had width, height and q in the parameter.

Press enter or click to view image in full size

I quickly opened my Burp suite, Intercepted the request and send it to the repeater. So I could work more properly. I changed the parameter value of height and width from 500 to something very high like 1000000000000000000 and q value to 1000 and sent the request, After sending the request the response took too long to come. my hacker brain said to repeat this process multiple times and So I sent the request to intruder and set payload type to null payloads and the value of it to 1000

Press enter or click to view image in full size

After some requests, I started to get 502 & 503 errors. At that point I knew it is a DOS but to confirm that the service actually stopped working, I opened photos.target.me from other network and actually the website returned error.

Press enter or click to view image in full size

I was nervous as the service stopped working for around 10–15 mins and this could lead me to trouble as this service was used to fetch user images and all other images used in the sites *target.com, *target.net, But thankfully the service restarted to work.

Get Faique’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I stopped hunting as I didn’t want any trouble and Reported the bug and after around 3 days I got response from them

Press enter or click to view image in full size
Pro Tips:
Hunt using dork, Dork I use https://github.com/sushiwushi/bug-bounty-dorks/blob/master/dorks.txt
Don’t force yourself to do bug hunting
Go for both manual and automated hunting
Follow me on twitter as I’ll help you achieve it: https://twitter.com/imfaiqu3
Resources:

Youtube channels: RanaKhalil101, zwik ,InsiderPhD, FarahHawa, orwaatyat, etc.

Labs: portswigger, hackthebox, pentesterlab

Thanks for reading! Feel free to Dm me on Instagram or Twitter!

Instagram: https://www.instagram.com/faique.exe

Twitter: https://twitter.com/imfaiqu3

GitHub: https://github.com/faiqu3/

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!
