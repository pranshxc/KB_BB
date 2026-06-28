---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-23_how-do-i-take-over-another-user-subdomain-name-worth-.md
original_filename: 2023-02-23_how-do-i-take-over-another-user-subdomain-name-worth-.md
title: How do I take over another user subdomain name worth $$$$
category: documents
detected_topics:
- command-injection
- otp
- csrf
tags:
- imported
- documents
- command-injection
- otp
- csrf
language: en
raw_sha256: db1acf3e0b4369b200f3794ecca104906b6fba4639964d081528f7bcd431498b
text_sha256: 7ea83af93da2e6d24a0c86495bed6a4834744226e839a7943bcfd3b69e14417f
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# How do I take over another user subdomain name worth $$$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-23_how-do-i-take-over-another-user-subdomain-name-worth-.md
- Source Type: markdown
- Detected Topics: command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `db1acf3e0b4369b200f3794ecca104906b6fba4639964d081528f7bcd431498b`
- Text SHA256: `7ea83af93da2e6d24a0c86495bed6a4834744226e839a7943bcfd3b69e14417f`


## Content

---
title: "How do I take over another user subdomain name worth $$$$"
page_title: "How to take over another users subdomain? Bug bounty writeup | by Parkerzanta | Medium"
url: "https://parkerzanta.medium.com/how-do-i-take-over-another-user-subdomain-name-worth-c66bb0c3f2f7"
authors: ["Parkerzanta (@parkerzanta)"]
bugs: ["Subdomain takeover"]
bounty: "1250"
publication_date: "2023-02-23"
added_date: "2023-02-28"
source: "pentester.land/writeups.json"
original_index: 1484
scraped_via: "browseros"
---

# How do I take over another user subdomain name worth $$$$

How to take over another users subdomain? Bug bounty writeup
Parkerzanta
Follow
3 min read
·
Feb 23, 2023

71

Press enter or click to view image in full size

Hello everyone

I would like to write down a finding regarding the takeover of another user’s Subdomain name. Previously I explained a little about how this website works.

So, the website that I’m testing has a feature to set each Subdomain name the same as Shopify
Users can change their subdomain name to another name, of course, they cannot change the subdomain name to one that already exists or is used by another user.

How can I take over another user’s subdomain name? As usual, I did a test on several features but found nothing, the feature that caught my attention was setting the Subdomain Name, users can change each subdomain name as follows

Press enter or click to view image in full size
Settings subdomain name

Like the image above Attacker is my Subdomain name, and it will look like https://attacker.redacted.com what if I change the subdomain name to another user’s Subdomain name? I try to do it then the response will look like the following “REDACTED Page URL has already been taken”

Press enter or click to view image in full size
Subdomain already been taken

So I tried adding SPACE at the end of the subdomain name, and it’s very surprising. I managed to change my Subdomain name to another user’s Subdomain name.

Get Parkerzanta’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Yep that’s right, I added a SPACE at the end of the subdomain name:p or with the following URL encode %20 on the Burp Suite request as follows

POST /xxx/campaigns/1232/settings HTTP/2
Host: redacted.com
Cookie: cokiedsfsd
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: */*;q=0.5, text/javascript, application/javascript
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://redacted.com/xxx/campaigns/1232/settings
X-Csrf-Token: KOFXStxcsdfcsdfVZ6WZsKJRGPg==
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 602
[....]

utf8=%E2%9C%93&_method=patch&authenticity_token=KOFXStcWdGPg%3D%3D&campaign[redacted_slug]=victim%20&commit=Save+and+Continue

The parameters “campaign[redacted_slug]” and “victim%20” are the subdomain name of the victim by adding space with the URL encoding, see the image below

Press enter or click to view image in full size
Request & respons

Response “202 Accepted” that I managed to change my subdomain name to the victim’s Subdomain name, the previous Subdomain name https://attacker.redacted.com successfully changed to the victim Subdomain name https://victim.redacted.com

I immediately reported my findings to their Team after 2 days of waiting for them to reply to my email, that the findings were valid and I was given a bounty of $1250

Press enter or click to view image in full size
Bounty awarded

Thank you for reading my writing, stay focused on your program and test all available features, don’t miss any little things.

Video PoC

Thank you for reading my writing, don’t forget to give your applause 👏
Follow me at https://x.com/parkerzanta

[!] The source of this article comes from Parkerzanta Blog which I wrote in English.

Press enter or click to view image in full size
