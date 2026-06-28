---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-31_download-this-tool-and-you-win.md
original_filename: 2019-10-31_download-this-tool-and-you-win.md
title: Download this tool and you win
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: cee8f56a664366e2c5c23ef549d62d36feb908ede4260516710d2f4dd8c2ba54
text_sha256: 6c1f2eda45c722a6e8f6fef06a8a7194bef644a6309ad3c0cc1fe50a09555e73
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Download this tool and you win

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-31_download-this-tool-and-you-win.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `cee8f56a664366e2c5c23ef549d62d36feb908ede4260516710d2f4dd8c2ba54`
- Text SHA256: `6c1f2eda45c722a6e8f6fef06a8a7194bef644a6309ad3c0cc1fe50a09555e73`


## Content

---
title: "Download this tool and you win"
url: "https://medium.com/@z0id/finding-open-redirects-like-a-pro-3b87fa474cfd"
authors: ["zoid (@z0idsec)"]
bugs: ["Open redirect"]
publication_date: "2019-10-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4962
scraped_via: "browseros"
---

# Download this tool and you win

Download this tool and you win
z0id
Follow
3 min read
·
Oct 31, 2019

76

Hi my name is 
z0id
 I am a security consultant at hackerone and bugcrowd. I would like to share with you how I found an interesting way to find open redirects with automation in python.

Story

I woke up one morning and I decided to find a creative way to look for unvalidated open redirects automatically so, I came up with a very good technique.

First let me explain my manual way of finding open redirects and we will go from there.

I start of by picking a target to do my recon phase on to find all sub domains I try to not focus on recon too much because I don’t really like it. Once I’ve collected all the sub domains I put them in burp for in scope items and start spidering away and mapping out the whole site.

I will then look for only 302 status codes in the response when I see that Location: / is getting reflected in the response header.

Press enter or click to view image in full size

I start spraying away some payloads with intruder.

Once I get a hit I take a picture for proof and make a video of my findings and report it with a nice detail Proof Of Concept (PoC).

How To Automate This

I found a way to automate this with exceptional results.

I started of searching for ways to scrape bugcrowd and hackerone until I came across:

arkadiyt/bounty-targets-data
This repo contains data dumps of Hackerone and Bugcrowd scopes (i.e. the domains that are eligible for bug bounty…

github.com

I download this and played around with some subdomain scanning with assetfinder.

I used the following bash alias to scan for subdomains from all of bugcrowd and hackerone’s programs.

Run it like:

Get z0id’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

afinderlist wildcards.txt

Press enter or click to view image in full size
Assetfinder bash alias

Then once the sub domain scan was finished I ran my tool that I have been developing against all the subdomains and I fuzzed the path for open redirects.

Press enter or click to view image in full size

`

Results:
Press enter or click to view image in full size
Open redirect scanner
Success Story:

I used this technique and I found an open redirect on VendHQ and it was a funny story because I reported it and they said it was out of scope so they put it as N/A. I was annoyed but I then moved on…… 3 days later….

They re-opened and they said:

Vendhq report approved

So, they accepted it and I was pretty much like:

They triage it and approved it I got some points unfortunately it was not a paid program but that does not matter. This pretty much made my day so I decided to ask if I could disclose it, and they allowed it.

Press enter or click to view image in full size
Open Redirect VendHQ Disclosure

I hope my technique helps and I hope you enjoyed this post, try out my technique give it a shot and experiment.

Takeaway

I would like to end this post by saying that if you find an open redirect in a parameter, sometimes you might be lucky to chain it with Server-Side Request Forgery (SSRF) for more impact so it’s good practice to test for that if you come across an open redirect.

I hope you enjoyed my post Have a nice day and happy bughunting :)
