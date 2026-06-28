---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-18_weird-lfi-and-escalating-the-impact-from-high-to-critical.md
original_filename: 2023-09-18_weird-lfi-and-escalating-the-impact-from-high-to-critical.md
title: Weird LFI and escalating the impact from High to Critical
category: documents
detected_topics:
- path-traversal
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- path-traversal
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: fc637a2871633824a149bbf69a393f15fbac2e61cd726b9ef3d5e1d6d7498a43
text_sha256: 0f9ff6cf3f77e5b56198aa80e8d70e87196954eb1a558207f25f59cd655271d9
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Weird LFI and escalating the impact from High to Critical

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-18_weird-lfi-and-escalating-the-impact-from-high-to-critical.md
- Source Type: markdown
- Detected Topics: path-traversal, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `fc637a2871633824a149bbf69a393f15fbac2e61cd726b9ef3d5e1d6d7498a43`
- Text SHA256: `0f9ff6cf3f77e5b56198aa80e8d70e87196954eb1a558207f25f59cd655271d9`


## Content

---
title: "Weird LFI and escalating the impact from High to Critical"
url: "https://medium.com/@snoopy101/weird-lfi-and-escalating-the-impact-from-high-to-critical-3e804f5366e9"
authors: ["snoopy (@snoopy101101)"]
bugs: ["LFI"]
publication_date: "2023-09-18"
added_date: "2023-09-27"
source: "pentester.land/writeups.json"
original_index: 769
scraped_via: "browseros"
---

# Weird LFI and escalating the impact from High to Critical

Weird LFI and escalating the impact from High to Critical
snoopy
Follow
3 min read
·
Sep 19, 2023

352

4

Hey wonderful hackers. I was hacking on a VDP program and after a light recon I picked one subdomain to hunt.

I clicked around and used the website as intended but when I looked at the requests in burp, this request caught my eyes.

https://target.tld/api/whitelabel/getFile?file=favico
Press enter or click to view image in full size

So I tested for LFI and tried to get the /etc/passwd file, but the response was empty. I tried all bypasses but no luck.

I tried endpoints from Seclists and I got these files:

https://target.tld/api/whitelabel/getFile?file=../../../../../../../../../../../../etc/hosts
https://target.tld/api/whitelabel/getFile?file=../../../../../../../../../../../../var/log/dmesg
https://target.tld/api/whitelabel/getFile?file=../../../../../../../../../../../../etc/ssh/ssh_host_dsa_key
https://target.tld/api/whitelabel/getFile?file=../../../../../../../../../../../../var/log/dpkg.log
Press enter or click to view image in full size
/etc/hosts
Press enter or click to view image in full size
/etc/ssh/ssh_host_dsa_key
That's all. Nothing quite impactful.

Anyway this is an LFI and based on the wrong belief the impact is High, but I personally believe that the impact of LFI must be Critical.

Some examples of High impact LFIs:

U.S. Dept Of Defense disclosed on HackerOne: [Critical] Full local...
Description Hello. I discovered a Path Traversal issue on the https://██████████/ I was able to turn it to the local…

hackerone.com

U.S. Dept Of Defense disclosed on HackerOne: lfi in...
hi i found critcal lfi vulnerability poc: https://█████████/████████=/etc/passwd response:...

hackerone.com

Starbucks disclosed on HackerOne: Korea - LFI Server directory...
b4bilal discovered a misconfiguration when handling URI paths. This permitted an adversary to traverse the docroot and…

hackerone.com

They did it on my report too:
Press enter or click to view image in full size

I wanted to escalate this to Critical, so I had to find something, and It’s a little difficult by brute-forcing.

I fuzzed internal endpoints with special characters and unicodes and I found something interesting. The * character was returning a file in every directory. (I guess it was the first file. I still don’t know)

Get snoopy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I sent this request:

https://target.tld/api/whitelabel/getFile?file=../../../../../../../../../../../../../../../var/www/*

I got Database credentials:

Press enter or click to view image in full size
The password was too hard to guess :)

They were valid and I logged into the Database.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Source code disclosure:
Press enter or click to view image in full size
Press enter or click to view image in full size
Hello white box
Is it still “High” baby?
Press enter or click to view image in full size
Press enter or click to view image in full size
It’s a VDP, so there is no bounty :)

Story is over here, but I found another thing about that * behavior.

It can be used like this too: /etc/apache2/*SOME-STRING

If that string matches part of the file name in that directory, it returns the file. Like these examples:

Press enter or click to view image in full size
Press enter or click to view image in full size

I don’t know the reason still. Please tell me if you know. :)

Takeaway:

The impact of LFI vulnerability is definitely Critical.

Reach me at:

LinkedIn:

https://www.linkedin.com/in/ali-imani-2a896a266/

twitter:

https://twitter.com/snoopy101101

Thanks for reading. Love y’all.
