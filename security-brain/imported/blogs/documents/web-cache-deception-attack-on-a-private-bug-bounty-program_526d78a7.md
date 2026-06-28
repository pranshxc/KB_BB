---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-01_web-cache-deception-attack-on-a-private-bug-bounty-program.md
original_filename: 2023-03-01_web-cache-deception-attack-on-a-private-bug-bounty-program.md
title: Web Cache Deception Attack on a private bug bounty program
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 526d78a79d1e08ff1401ee6d63b8419334ef9efa3cfbd20047a1b288f561bc24
text_sha256: 1963b3177fb7846180ad17085be4e29c4d58e154a27b57a4d8d43a93c0e5ec6d
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Web Cache Deception Attack on a private bug bounty program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-01_web-cache-deception-attack-on-a-private-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `526d78a79d1e08ff1401ee6d63b8419334ef9efa3cfbd20047a1b288f561bc24`
- Text SHA256: `1963b3177fb7846180ad17085be4e29c4d58e154a27b57a4d8d43a93c0e5ec6d`


## Content

---
title: "Web Cache Deception Attack on a private bug bounty program"
url: "https://medium.com/@snoopy101/web-cache-deception-attack-on-a-private-bug-bounty-program-52872cbdeedc"
authors: ["snoopy (@snoopy101101)"]
bugs: ["Web cache deception"]
publication_date: "2023-03-01"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1446
scraped_via: "browseros"
---

# Web Cache Deception Attack on a private bug bounty program

Web Cache Deception Attack on a private bug bounty program
snoopy
Follow
3 min read
·
Mar 1, 2023

642

9

Hi incredible hackers!

I’m about to tell you the story of one of the coolest bugs I’ve found on a private program which got duplicate, unfortunately.

Press enter or click to view image in full size

I was like:

Anyway I love hacking and as one of my heroes 
Sean (zseano)
 says: “Bounty/money is just a bonus”

Back to the vulnerability.

Web Cache Deception:

Cache Poisoning and Cache Deception
Discovery: Check HTTP headers Discovery: Caching 400 code Discovery: Identify and evaluate unkeyed inputs Elicit a…

book.hacktricks.xyz

The scope of the program is truly small which just contains the main website (www.target.tld) and the API subdomain (api.target.tld).

I was looking at my profile page on the main website and I refreshed the page and looked at my Burp’s history page and I realized that the profile information were shown on this API endpoint.

Press enter or click to view image in full size
Press enter or click to view image in full size
MISS

I looked at the response and that ‘Server-Timing: cdn-cache; desc=MISS’ caught my eyes.

Get snoopy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I had to test for 2 beautiful bugs:

Cache Poisoning Attack
Cache Deception Attack

Although I literally tried everything, it seems that the website isn’t vulnerable to the first bug.

So I went for the second vulnerability and I put ‘.css’ at the end of the URL.

Press enter or click to view image in full size

Damn! I was still able to see my information, so I checked the ‘Server-Timing’ response header, immediately.

Press enter or click to view image in full size
Yay! It says HIT baby

So now I just needed to send https://www.target.tld/api/users/WHATEVER/current/full.css to the victim for cache to be hit and open the link on my own browser before the cache expired to see the victim’s information. Pretty easy right?

Unfortunately no. It wasn’t that easy and the cache was expired so fast that I couldn’t see the information. In order to exploit the vulnerability I had to find a way to send multiple requests to the endpoint from victim’s behalf.

The scenario
The victim visits hacker’s website
The hacker’s website sends several requests to the https://www.target.tld/api/users/WHATEVER/current/full.css in order to poison the cache.
The hacker opens the link on his browser and the victim’s information is shown.
PoC:
Press enter or click to view image in full size
Sending numerous requests with JS on the hacker website

Note that the Chrome browser is the victim and the Firefox browser is the hacker:
