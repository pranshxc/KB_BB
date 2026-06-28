---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-12_how-i-made-2000-with-url-redirection.md
original_filename: 2020-08-12_how-i-made-2000-with-url-redirection.md
title: How I made $2000 with URL REDIRECTION?
category: documents
detected_topics:
- sqli
- idor
- xss
- command-injection
- rate-limit
- information-disclosure
tags:
- imported
- documents
- sqli
- idor
- xss
- command-injection
- rate-limit
- information-disclosure
language: en
raw_sha256: b5f9fbed423065ee2e6a75c25b25e5dcbe7bd10430e047cc5ee385272f727a99
text_sha256: 8728dc4179287e778ffbf455d4291feb47333f8d26cecceabf352a813bbc209c
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How I made $2000 with URL REDIRECTION?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-12_how-i-made-2000-with-url-redirection.md
- Source Type: markdown
- Detected Topics: sqli, idor, xss, command-injection, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `b5f9fbed423065ee2e6a75c25b25e5dcbe7bd10430e047cc5ee385272f727a99`
- Text SHA256: `8728dc4179287e778ffbf455d4291feb47333f8d26cecceabf352a813bbc209c`


## Content

---
title: "How I made $2000 with URL REDIRECTION?"
url: "https://medium.com/@singh.simran7838/how-i-made-2000-with-url-redirection-b1b5f4e7a678"
authors: ["Simran Singh"]
bugs: ["Open redirect", "SQL injection"]
bounty: "2,000"
publication_date: "2020-08-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4331
scraped_via: "browseros"
---

# How I made $2000 with URL REDIRECTION?

How I made $2000 with URL REDIRECTION?
cybrr_warrior_official
Follow
2 min read
·
Aug 13, 2020

112

2

Hi this is Simran Singh (cybrr_warrior_official). This is my first bug bounty write-up. And in this article I’m going to tell you how I got 2000$ SQLi vulnerability in a private program.

I’m not going to reveal the name of the program. Because this can go against Program rules and policies.

Let’s say domain: example.com

So, at first I did testing as a normal test we usually do. I start doing nmap ports scanning, sub domain enumeration, directory listing, etc. etc. And I got some sub domains but got nothing like juicy stuff like things.

And at that time I thought its a wastage of time let’s think in a criminal way. And then a tool Arjun hits in my mind and I started discovering some parameters.

After that I got some SQLi vulnerable parameters on a sub domain, so let’s say

sub.example.com

And the whole URI string looks like this

https://sub.example.com/@someone’s_name/blog?pageid=143

After that I start performing some SQLi attempt using some payloads.

And saw there responses in burp suite but all the payloads are getting filtered. At time I am loosing my hope and shutdown my PC and Then i went to sleep.

But next day I again start gathering some more Information ab the target and I reviewed the program policy, and I saw there is URL Redirection is out of scope. But we are Security Researcher’s alway try to make things complex to easier. And then an Idea pop’s up in my mind let’s take a look towards redirect URL if there is any…..

And I found something like this:

Get cybrr_warrior_official’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://www.example.com/subscribe?r=https://sub.example.com/subscribe_to_newsletter/

And the sub domain in the destination URL endpoint is the same Sub domain on which I Tested SQL injections.

I’m excited ☺ now.

Let’s try whole the SQLi tests with URL Redirections.

And I started with Database check, then Table and columns. You know what happened next.

BANG BANG!

I made a POC video, take some screenshots, and reported to the program on 2nd August 2020.

And on 11th August 2020 I checked my inbox an e-mail was there unreaded.

Press enter or click to view image in full size

And all this happened because some people don’t know a domain name is also known as root domain

KYA BAAT HAI ….

KYA CHEEZ HAI PAISA….

$$$$$$$$$$$$$$$$$$$$$$$$$$$

Wanna tell you something:

Always try to thing in unique way, I know the basic XSS, RCE etc. The basic vulnerabilities is over but do not ever loose hope. Might be there is something on which other people’s not paying attention.

Sorry about the bad English.

I’m not good enough in English 😅😅😅…….
