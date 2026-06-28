---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-07_story-of-my-first-cash-bounty-on-hackerone.md
original_filename: 2021-06-07_story-of-my-first-cash-bounty-on-hackerone.md
title: Story of my first cash bounty on hackerone.
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 0bce6dcafa91acb5ce6b378ea7028b9b4c90391a9432fc78e2a6fcb91e9ccdcb
text_sha256: 94ec5928a0255f7f4e8295a128a22de1bfb6825661701a590d492815da09c228
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Story of my first cash bounty on hackerone.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-07_story-of-my-first-cash-bounty-on-hackerone.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `0bce6dcafa91acb5ce6b378ea7028b9b4c90391a9432fc78e2a6fcb91e9ccdcb`
- Text SHA256: `94ec5928a0255f7f4e8295a128a22de1bfb6825661701a590d492815da09c228`


## Content

---
title: "Story of my first cash bounty on hackerone."
url: "https://vedanttekale20.medium.com/story-of-my-first-cash-bounty-on-hackerone-acad282ae962"
authors: ["Vedant Tekale (@_justYnot)"]
bugs: ["SSRF", "XSS"]
publication_date: "2021-06-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3593
scraped_via: "browseros"
---

# Story of my first cash bounty on hackerone.

Story of my first cash bounty on hackerone.
Vedant Tekale
Follow
4 min read
·
Jun 7, 2021

948

4

Hello again bugbounty community! My name is Vedant(Also known as Vegeta on Twitter😁) and I’m a cybersecurity enthusiast and an aspiring Bug hunter :) Today I’ll share with you a story about an interesting bug that I found recently which helped me get my first bounty on hackerone platform. I am sure you will like it, so without any further ado let’s get started.

Press enter or click to view image in full size
Part 1 : Backstory

Since I started learning about bug bounty I’ve always thought that Hackerone is the toughest platforms and it will be very hard to find a valid bug there. But in the beginning of this year I decided that I’ll focus more on Hackerone platform and try to get at least one bug triaged and yeah I did that. After dedicating almost 3 months on H1 I was ranked 53rd on country based leaderboard and that really boosted my confidence so my next goal was to get my first bounty so I decided to hack on a bug bounty program.

Part 2 : The discovery

So I chose a target which had only main web application in scope. Every time when I start the recon on such target I gather lots of endpoints using waybackurls, but this time I decided to try something else. I used Linkfinder tool for the first time and the command was,

python linkfinder.py -i https://example.com -d

When the execution completed I started going through the results one by one. There were lots of URLs and after almost 10 mins one URL got my attention it was like the following,

htttps://www.example.com/image?Id=somelinkwithouthttp.com

Get Vedant Tekale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So the above URL really got me curious as there was not http:// or https:// . After seeing such parameters which accept URLs as an argument most bug hunters will go for SSRF and I did the same. I quickly fired up the Burp collaborator copied one payload and without prepending http or https I just pasted it in that Id parameter and hit enter expecting for a SSRF but sadly I got the following response in my collaborator.

Press enter or click to view image in full size
😔

I got only DNS request 😔. After trying some things I got an idea. I decided to prepend @ symbol in my collaborator payload(I don’t know how I got that idea I just did it spontaneously😂) and I hit enter and this time surprisingly I got the following response,

Press enter or click to view image in full size
😁

The IP was of AWS so I tried to fetch the AWS-metadata and I tried lots and lots of different techniques(Like redirect, DNS rebinding etc.) for almost 3–4 days but nothing worked. I decided to report this anyways and after 2 days I got response from triager saying that I need to show the impact. I was really frustrated at this point.

Part 3 : The exploitation

So next day with fresh mind I decided to give it another try. This time I tried to chain the SSRF with some bug. As that parameter was fetching an image I tried to use the brutelogic’s XSS POC link. And guess what? It worked! The XSS popped up😁. I used the following payload:-

As the poc.svg was fetched successfully I tried to create a HTML file which contained a XSS payload to steal the victim’s session cookies. I created that file and used ngrok to host it on my local host. So for testing this exploit I created 2 accounts on that site and tried using that payload and yeah! It worked!!! I got the victim’s cookies😎. I used the following code:-

Press enter or click to view image in full size
😎

I quickly reported this to the program and within one day the report was triaged and after almost 20 days I was rewarded my very first bounty on 
HackerOne
 ! I learned lots of new things while finding and exploiting this issue. If you have any doubts regarding this write-up you can ping me here

I hope you learned something new by reading this write-up and if you want you can buymeacoffee 😇. Thank you for reading this. Until next time, good bye and happy hacking!
