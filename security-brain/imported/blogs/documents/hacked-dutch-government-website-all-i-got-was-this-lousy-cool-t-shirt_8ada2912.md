---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-16_hacked-dutch-government-website-all-i-got-was-this-lousy-cool-t-shirt.md
original_filename: 2022-02-16_hacked-dutch-government-website-all-i-got-was-this-lousy-cool-t-shirt.md
title: Hacked Dutch Government Website. All I got was this l̶o̶u̶s̶y̶ cool T-Shirt.
category: documents
detected_topics:
- idor
- command-injection
- otp
- rate-limit
- information-disclosure
- api-security
tags:
- imported
- documents
- idor
- command-injection
- otp
- rate-limit
- information-disclosure
- api-security
language: en
raw_sha256: 8ada2912cfd4d3b4c1cd838f1d23748636689a1d5aed6965e4f58293a2642228
text_sha256: 5595ed546f903d22cc0b0b6ccfc47f471a187056d7c171db384eac42a27e4e97
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Hacked Dutch Government Website. All I got was this l̶o̶u̶s̶y̶ cool T-Shirt.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-16_hacked-dutch-government-website-all-i-got-was-this-lousy-cool-t-shirt.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, rate-limit, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `8ada2912cfd4d3b4c1cd838f1d23748636689a1d5aed6965e4f58293a2642228`
- Text SHA256: `5595ed546f903d22cc0b0b6ccfc47f471a187056d7c171db384eac42a27e4e97`


## Content

---
title: "Hacked Dutch Government Website. All I got was this l̶o̶u̶s̶y̶ cool T-Shirt."
url: "https://medium.com/@chander.romesh/hacked-dutch-government-website-all-i-got-was-this-l̶o̶u̶s̶y̶-cool-t-shirt-4fd62ed3e734"
authors: ["Romesh chander"]
programs: ["Dutch Government"]
bugs: ["Information disclosure"]
publication_date: "2022-02-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2901
scraped_via: "browseros"
---

# Hacked Dutch Government Website. All I got was this l̶o̶u̶s̶y̶ cool T-Shirt.

Hacked Dutch Government Website. All I got was this l̶o̶u̶s̶y̶ cool T-Shirt.
Romesh chander
Follow
3 min read
·
Feb 16, 2022

114

1

They are right. Persistence is the key !

The Dutch government give away cool T-shirt(swag) for the security researchers who reports vulnerability in their application. I so badly wanted it and started working for it.

It was not a easy journey for me to get here. Many of my reports got rejected or was marked duplicate. I pick targets from here https://gist.github.com/random-robbie/f985ad14fede2c04ac82dd89653f52ad . I thought maybe all the vulnerabilities have been reported and patched. I have seen most of the researchers reported not one but multiple vulnerabilities and so maybe I’m too late to try on .nl domain.

Press enter or click to view image in full size
Reply from Dutch government cert team

But you know what Rocky my man said “ It ain’t how hard you hit. Its about how hard you get hit and keep moving forward.

Press enter or click to view image in full size

So how I found it finally ?

I was looking at a random domain from https://gist.github.com/random-robbie/f985ad14fede2c04ac82dd89653f52ad . I picked one.

Get Romesh chander’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I used Knock.py tool https://github.com/guelfoweb/knock to enumerate the subdomains. cmd used for enumeration python3 knock.py -u exmaple.com

Press enter or click to view image in full size
This is just example image

After finding handful of subdomains. I looking for a interesting ones to do directory brute forcing .

I used dirsearch tool https://github.com/maurosoria/dirsearch and used seclist wordlist for enumeration. cmd used python3 dirsearch.py -u example.com /usr/share/seclist/common.txt.

Press enter or click to view image in full size
Fake Image

What's more important is to add Makefile into your wordlist. I added example.com/Makefile and there you go.

Press enter or click to view image in full size
Actual Image

Makefile had almost all important details. I was able to download Sql.DB and dump it . So i was not stopping here and checked other subdomains as well. Further pentesting I downloaded .htaccess and web.config files too.

Press enter or click to view image in full size
Actual image

Like they say persistence is the key ! I had many sleepless nights and testing zillion targets to enum subdomain and brute forcing dir before getting here. Here’s the token of appreciation from the Dutch government for responsibly disclosing the vulnerability.

Press enter or click to view image in full size
Press enter or click to view image in full size
